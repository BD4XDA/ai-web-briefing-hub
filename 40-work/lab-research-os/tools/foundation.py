"""Project-owned append-only checkpoints; stdlib only, no network or harness imports."""
import argparse,hashlib,json,os,re,sys,time
from pathlib import Path
FIELDS=('current_verified_state','completed','decisions','open_questions','known_risks','in_progress','next_actions','evidence_references')
SOL_START='<!-- FOUNDATION-SOL-CHECKPOINT:START -->'
SOL_END='<!-- FOUNDATION-SOL-CHECKPOINT:END -->'
def project_root(start):
    p=Path(start).resolve()
    for candidate in (p,*p.parents):
        marker=candidate/'.lab-project.json'
        if marker.is_file():
            identity=json.loads(marker.read_text(encoding='utf-8'))
            if identity.get('project_id')!='lab-research-os':raise ValueError('Unexpected project identity')
            return candidate
    raise ValueError('Canonical root not found; do not infer from a directory name')
def canonical_bytes(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2).encode('utf-8')
def current(root):
    pointer=root/'checkpoints/LATEST.json'
    if not pointer.exists():return None,None
    ref=json.loads(pointer.read_text(encoding='utf-8'))
    ident=ref['id']
    if not re.fullmatch(r'[0-9]{8}T[0-9]{6}-[0-9a-f]{12}',ident):raise ValueError('Invalid checkpoint identity')
    raw=(root/'checkpoints'/(ident+'.json')).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=ref['sha256']:raise ValueError('Checkpoint integrity conflict')
    return ident,json.loads(raw)
def render(ident,record):
    parts=['# Lab Research OS · CHECKPOINT',f'Checkpoint ID: {ident}',f"Priority: {record['priority']} · Status: {record['status']}",'Canonical committed pointer: checkpoints/LATEST.json. If IDs differ, use tools/foundation.py show; do not guess.']
    for field in FIELDS:
        parts.extend(['','## '+field.replace('_',' ').title(),''])
        parts.extend('- '+str(x) for x in record[field])
    return '\n'.join(parts)+'\n'
def render_sol_checkpoint(ident,record):
    parts=[SOL_START,'## Latest Foundation checkpoint for Sol','',f'Checkpoint ID: {ident}',f"Priority: {record['priority']} · Status: {record['status']}",'Canonical committed pointer: `checkpoints/LATEST.json`. This generated mirror is required for Sol resume, but `tools/foundation.py show` remains authoritative if IDs differ.']
    for field in FIELDS:
        parts.extend(['','### '+field.replace('_',' ').title(),''])
        parts.extend('- '+str(x) for x in record[field])
    parts.extend(['',SOL_END,''])
    return '\n'.join(parts)
def render_sol_agent(root,ident,record):
    path=root/'SOL-AGENT.md'
    if not path.is_file():raise ValueError('SOL-AGENT.md is required for checkpoint mirroring')
    text=path.read_text(encoding='utf-8')
    starts=text.count(SOL_START);ends=text.count(SOL_END)
    if starts!=ends or starts>1:raise ValueError('Invalid SOL checkpoint mirror markers')
    block=render_sol_checkpoint(ident,record)
    if starts==0:return text.rstrip()+'\n\n'+block
    before,tail=text.split(SOL_START,1)
    _,after=tail.split(SOL_END,1)
    return before.rstrip()+'\n\n'+block+after.lstrip('\n')
def atomic_write(path,data):
    temp=path.with_name(path.name+'.tmp-'+str(os.getpid()))
    with temp.open('xb') as f:f.write(data);f.flush();os.fsync(f.fileno())
    os.replace(temp,path)
def checkpoint(root,record,expected):
    if set(FIELDS)-record.keys():raise ValueError('Missing continuity fields')
    if record.get('priority') not in ['P0','P1','P2','P3','EXIT']:raise ValueError('Unknown priority')
    if record.get('status') not in ['complete','in_progress','blocked','checkpointed']:raise ValueError('Unknown status')
    if any(not isinstance(record[f],list) or any(not isinstance(v,str) for v in record[f]) for f in FIELDS):raise ValueError('Continuity fields must be string arrays')
    if not record['evidence_references']:raise ValueError('Checkpoint requires evidence references')
    raw=canonical_bytes(record)
    if len(raw)>100000:raise ValueError('Checkpoint too large; reference artifacts instead')
    if re.search(rb'sk-[A-Za-z0-9_-]{16,}|Bearer\s+[A-Za-z0-9._-]{16,}',raw):raise ValueError('Potential secret rejected')
    directory=root/'checkpoints';directory.mkdir(exist_ok=True)
    lock=directory/'writer.lock'
    try:fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    except FileExistsError:raise RuntimeError('Checkpoint writer lock exists. Do not clear it automatically.')
    try:
        os.write(fd,str(os.getpid()).encode());os.close(fd)
        ident,_=current(root)
        if (ident or 'none')!=expected:raise RuntimeError('Stale writer: reload the committed checkpoint')
        record={**record,'parent':ident,'created_at':time.strftime('%Y-%m-%dT%H:%M:%S%z')}
        raw=canonical_bytes(record);digest=hashlib.sha256(raw).hexdigest()
        new=time.strftime('%Y%m%dT%H%M%S')+'-'+digest[:12]
        target=directory/(new+'.json')
        with target.open('xb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
        # Snapshot exists before projections; LATEST is the commit point.
        atomic_write(root/'CHECKPOINT.md',render(new,record).encode('utf-8'))
        atomic_write(root/'SOL-AGENT.md',render_sol_agent(root,new,record).encode('utf-8'))
        atomic_write(directory/'LATEST.json',canonical_bytes({'id':new,'sha256':digest}))
        return new
    finally:
        # Only this invocation's successfully acquired lock is removed.
        lock.unlink()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['show','checkpoint']);parser.add_argument('--root',default=str(Path(__file__).resolve().parents[1]));parser.add_argument('--input');parser.add_argument('--expected',default='none');args=parser.parse_args()
    root=project_root(args.root)
    if args.command=='show':
        ident,record=current(root)
        if not ident:raise SystemExit('No committed checkpoint')
        print(render(ident,record))
    else:
        if not args.input:parser.error('--input required')
        print(checkpoint(root,json.loads(Path(args.input).read_text(encoding='utf-8-sig')),args.expected))
if __name__=='__main__':main()
