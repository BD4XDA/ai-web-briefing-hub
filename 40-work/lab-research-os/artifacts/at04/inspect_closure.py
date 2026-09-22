"""AT04 bounded read-only integrity inspection; no task/model/test execution."""
import hashlib, json, sys
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools'))
import foundation
def read(p): return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
started=datetime.now(timezone.utc).isoformat()
latest, state=foundation.current(ROOT)
chain=[]; ident=latest
while ident:
    p='checkpoints/'+ident+'.json'; obj=read(p)
    chain.append({'id':ident,'sha256':sha(p),'id_digest_matches':sha(p).startswith(ident.split('-')[-1]),'parent':obj.get('parent')})
    ident=obj.get('parent')
    if len(chain)>100: raise ValueError('unexpected checkpoint chain size')
required=['20260922T001120-06857fdd56f9','20260922T001240-6ee0580095c8']
taxonomy=read('artifacts/at03/FAILURE-TAXONOMY.json')
refs=[{'case':c['id'],'path':p,'exists':(ROOT/p).is_file()} for c in taxonomy['cases'] for p in c['evidence']]
base='artifacts/at03/autonomous-loop-01/'
wrapper=read(base+'review-response.json'); review=json.loads(wrapper['text'])
execution=read(base+'review-execution.json'); commit=read(base+'checkpoint-commit.json')
source='evidence/foundation-v0.1-manifest.json'; manifest=read(source)
candidate=read(base+'index.candidate.json'); target='artifacts/at03/manifest-index-v0.1.json'
snapshot=read(base+'source-manifest.snapshot.json')
expected={'project_id':read('.lab-project.json')['project_id'],'release':manifest['release'],'manifest_path':str((ROOT/source).resolve()).replace('\\','/'),'manifest_sha256':sha(source),'entry_count':len(manifest['files']),'entries':sorted([{'path':e['path'],'sha256':e['sha256']} for e in manifest['files']],key=lambda e:e['path'])}
checks={'latest_integrity_via_foundation_current':True,'p3_p4_in_committed_ancestry':all(i in [c['id'] for c in chain] for i in required),'checkpoint_id_digests':all(c['id_digest_matches'] for c in chain),'taxonomy_evidence_paths_exist':all(r['exists'] for r in refs),'candidate_exact_structure_and_values':candidate==expected,'source_snapshot_content_matches':snapshot['content']==manifest,'source_snapshot_hash_matches':snapshot['sha256']==sha(source),'writeback_exact_bytes':(ROOT/target).read_bytes()==(ROOT/base/'index.candidate.json').read_bytes(),'review_exit_zero':execution['exit_code']==0,'review_reason_completed':wrapper.get('reason',{}).get('kind')=='completed','review_tool_calls_zero':wrapper.get('tool_calls')==0,'review_pass_confidence_gate':review['result']=='PASS' and .8<=review['confidence']<=1 and review['anomaly_conflict']==[],'commit_exit_zero':commit['exit_code']==0,'worker_commit_is_current':commit['new_checkpoint']==latest,'worker_commit_parent_matches_packet':state['parent']==read('packets/at03-loop-01.json')['expected_checkpoint']}
out={'started_at_utc':started,'finished_at_utc':datetime.now(timezone.utc).isoformat(),'latest_at_inspection':latest,'checks':checks,'result':'PASS' if all(checks.values()) else 'FAIL','checkpoint_chain':chain,'taxonomy_reference_presence':refs,'bound_files':[{'path':p,'sha256':sha(p)} for p in [source,base+'run_loop.py',base+'context-load.json',base+'review-execution.json',base+'review-response.json',base+'review-prompt.txt',base+'checkpoint-commit.json',base+'index.candidate.json',target]],'scope':'Existing artifacts only; verifies neither scientific truth, live runtime, server model authenticity, original read timestamps nor fresh-context independence. No Foundation tests or model calls.'}
dest=ROOT/'artifacts/at04/integrity-inspection.json'
with dest.open('x',encoding='utf-8') as f: json.dump(out,f,ensure_ascii=False,indent=2)
print(json.dumps({'result':out['result'],'checks':checks},ensure_ascii=False))
