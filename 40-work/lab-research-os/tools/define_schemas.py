"""Versioned local contract definitions; only creates missing schema files."""
import json
from pathlib import Path

S = {'type': 'string', 'minLength': 1}
STRINGS = {'type': 'array', 'items': S}
NONEMPTY = {**STRINGS, 'minItems': 1, 'uniqueItems': True}
CONFIDENCE = {'type': 'number', 'minimum': 0, 'maximum': 1}
def enum(*values): return {'type': 'string', 'enum': list(values)}
def object_schema(name, fields):
    return {'$schema': 'https://json-schema.org/draft/2020-12/schema',
            'title': name + ' v1', 'type': 'object',
            'properties': fields, 'required': list(fields), 'additionalProperties': False}

DEFINITIONS = {
 'evidence': {
   'id': S, 'kind': {'const': 'evidence'}, 'path': S,
   'sha256': {'type':'string','pattern':'^[0-9a-f]{64}$'},
   'captured_at': S, 'locator': S, 'scope': S,
   'sensitivity': enum('local-metadata','sanitized-log','public'),
   'collector': S},
 'verification': {
   'id': S, 'claim': S, 'evidence_ids': NONEMPTY, 'verification_method': S,
   'result': enum('PASS','FAIL','UNCERTAIN'), 'confidence': CONFIDENCE,
   'anomaly_conflict': STRINGS, 'reviewer': S, 'model_reported': S,
   'harness': S, 'observed_at': S},
 'task-packet': {
   'task_id': S, 'project_id': {'const':'lab-research-os'}, 'project_root': S,
   'expected_checkpoint': S, 'owner': S, 'objective': S,
   'allowed_read_roots': NONEMPTY, 'write_paths': NONEMPTY,
   'excluded_scope': NONEMPTY, 'input_evidence_ids': STRINGS,
   'acceptance_criteria': NONEMPTY, 'verification_route': S,
   'budget': object_schema('budget', {
       'max_files': {'type':'integer','minimum':1,'maximum':500},
       'max_depth': {'type':'integer','minimum':0,'maximum':8},
       'max_model_calls': {'type':'integer','minimum':0,'maximum':3}}),
   'resume_action': S},
 'exception': {
   'id': S, 'problem': S, 'evidence_ids': NONEMPTY,
   'conflicting_evidence_ids': STRINGS, 'attempts': NONEMPTY,
   'confidence': CONFIDENCE, 'possible_explanations': NONEMPTY,
   'consequence': S, 'recommended_next_check': S,
   'level': enum('L0','L1','L2','L3'), 'owner': S}
}

def write_definitions(names=None):
    directory=Path(__file__).resolve().parents[1]/'schemas';directory.mkdir(exist_ok=True)
    for name in names or DEFINITIONS:
        path=directory/(name+'.schema.json')
        with path.open('x',encoding='utf-8') as handle:
            json.dump(object_schema(name,DEFINITIONS[name]),handle,ensure_ascii=False,indent=2)
            handle.write('\n')

if __name__=='__main__': write_definitions()
