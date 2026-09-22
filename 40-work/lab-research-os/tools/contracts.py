"""Local JSON Schema + evidence gates. Read-only; no remote schema retrieval."""
import argparse, hashlib, json, re, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
KINDS = {'evidence', 'verification', 'task-packet', 'exception',
         'agent-harness', 'workspace', 'project', 'instruction-memory', 'conflict'}

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def schema_check(kind, value):
    if kind not in KINDS:
        raise ValueError('Unknown record kind')
    schema = read(ROOT / 'schemas' / (kind + '.schema.json'))
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(value), key=lambda e: str(list(e.path)))
    if errors:
        raise ValueError('; '.join(str(list(e.path)) + ': ' + e.message for e in errors))

def packet_check(packet):
    schema_check('task-packet', packet)
    root = Path(packet['project_root']).resolve(strict=True)
    if read(root / '.lab-project.json')['project_id'] != packet['project_id']:
        raise ValueError('Project identity conflict')
    for raw in packet['allowed_read_roots'] + packet['write_paths']:
        if not Path(raw).is_absolute():
            raise ValueError('Scope paths must be absolute')
    for raw in packet['write_paths']:
        path = Path(raw).resolve()
        if not path.is_relative_to(root):
            raise ValueError('Write path outside canonical project')
    return root

def evidence_check(record, allowed_roots):
    schema_check('evidence', record)
    path = Path(record['path'])
    if not path.is_absolute():
        raise ValueError('Evidence path must be absolute')
    path = path.resolve(strict=True)
    roots = [Path(p).resolve(strict=True) for p in allowed_roots]
    if not any(path == p or path.is_relative_to(p) for p in roots):
        raise ValueError('Evidence path outside approved roots')
    if not path.is_file():
        raise ValueError('Evidence must be a file')
    if path.stat().st_size > 10_000_000:
        raise ValueError('Evidence exceeds v1 10 MB per-file budget')
    # Reading a file here checks bytes; its content is never printed.
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != record['sha256']:
        raise ValueError('Evidence integrity conflict: ' + record['id'])

def bundle_check(bundle, packet):
    packet_check(packet)
    if set(bundle) != {'task_id', 'records', 'evidence', 'reports'}:
        raise ValueError('Unknown or missing bundle fields')
    if bundle['task_id'] != packet['task_id']:
        raise ValueError('Task identity conflict')
    for field in ('records', 'evidence', 'reports'):
        if not isinstance(bundle[field], list) or not bundle[field]:
            raise ValueError('Bundle requires nonempty ' + field)
    if len(bundle['evidence']) > packet['budget']['max_files']:
        raise ValueError('Evidence exceeds task file budget')
    evidence_ids = set()
    for evidence in bundle['evidence']:
        evidence_check(evidence, packet['allowed_read_roots'])
        if evidence['id'] in evidence_ids:
            raise ValueError('Duplicate evidence ID')
        evidence_ids.add(evidence['id'])
    record_ids = set()
    for record in bundle['records']:
        if record.get('kind') not in KINDS - {'evidence', 'verification', 'task-packet', 'exception'}:
            raise ValueError('Invalid inventory kind')
        schema_check(record['kind'], record)
        if record['id'] in record_ids:
            raise ValueError('Duplicate record ID')
        record_ids.add(record['id'])
        if not set(record['evidence_ids']) <= evidence_ids:
            raise ValueError('Unresolved record evidence')
    report_ids = set()
    reviewed_evidence = set()
    for report in bundle['reports']:
        schema_check('verification', report)
        if report['id'] in report_ids:
            raise ValueError('Duplicate report ID')
        report_ids.add(report['id'])
        if not set(report['evidence_ids']) <= evidence_ids:
            raise ValueError('Unresolved report evidence')
        reviewed_evidence.update(report['evidence_ids'])
        if report['result'] != 'PASS' or report['confidence'] < 0.8 or report['anomaly_conflict']:
            raise ValueError('Integration held: unresolved verification')
    required_evidence = {ident for record in bundle['records'] for ident in record['evidence_ids']}
    if not required_evidence <= reviewed_evidence:
        raise ValueError('Integration held: record evidence not covered by reports')
    return {'result': 'PASS', 'task_id': packet['task_id'], 'records': len(record_ids),
            'evidence': len(evidence_ids), 'reports': len(report_ids),
            'limit': 'Structure, references, file integrity and gates only; not semantic truth or runtime isolation.'}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['packet', 'bundle', 'record'])
    parser.add_argument('path'); parser.add_argument('--packet'); parser.add_argument('--kind')
    args = parser.parse_args()
    value = read(args.path)
    if args.command == 'packet':
        packet_check(value); result = {'result': 'PASS', 'scope': 'packet structure and root'}
    elif args.command == 'bundle':
        if not args.packet: parser.error('--packet required')
        result = bundle_check(value, read(args.packet))
    else:
        schema_check(args.kind or value['kind'], value)
        result = {'result': 'PASS', 'scope': 'record structure only'}
    print(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    try: main()
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps({'result': 'FAIL', 'error': str(exc)}, ensure_ascii=False)); sys.exit(1)
