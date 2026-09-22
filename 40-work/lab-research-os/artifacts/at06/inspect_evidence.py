"""AT06 read-only diagnosis of retained AT05 artifacts. Never imports/runs AT05 adapter."""
import json,hashlib,sqlite3,subprocess
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/at06'
def j(p):return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def sha(b):return hashlib.sha256(b).hexdigest()
start=datetime.now(timezone.utc).isoformat()
names=['artifacts/at05/experiment.py','artifacts/at05/worker.stdout','artifacts/at05/worker.stderr','artifacts/at05/worker-execution.json','artifacts/at05/launch-input.json','artifacts/at05/prelaunch-binding.json','artifacts/at05/review-prompt.txt','artifacts/at05/review-execution.json','artifacts/at05/review-response.json','artifacts/at05/automatic-acceptance.json','packets/at05-recovery-01.json','packets/at05-recovery-01.md','evidence/foundation-v0.1-manifest.json','tools/foundation.py']
bindings=[{'path':p,'sha256':sha((ROOT/p).read_bytes()),'bytes':(ROOT/p).stat().st_size} for p in names]
events=[json.loads(line) for line in (ROOT/'artifacts/at05/worker.stdout').read_text(encoding='utf-8').splitlines()]
package=json.loads((ROOT/'artifacts/at05/review-prompt.txt').read_text(encoding='utf-8').split('\n',1)[1])
ex=j('artifacts/at05/worker-execution.json');reviewex=j('artifacts/at05/review-execution.json')
stderr=(ROOT/'artifacts/at05/worker.stderr').read_bytes();stdout=(ROOT/'artifacts/at05/worker.stdout').read_bytes()
code=(ROOT/'artifacts/at05/experiment.py').read_text(encoding='utf-8').splitlines()
terms=['def observe','def process','def run','other_tools=','no_other_tool','det=','package=','review_prompt=','c2=','PYTHONDONTWRITEBYTECODE','for suffix','rec=','if sys.argv']
excerpts=[{'line':i,'text':s} for i,s in enumerate(code,1) if any(t in s for t in terms)]
pre=j('artifacts/at05/prelaunch-binding.json')
boundcode=next(f for f in pre['files'] if f['path'].replace('\\','/').endswith('/artifacts/at05/experiment.py'))
db=Path('C:/Users/ASUS/.codex/logs_2.sqlite')
con=sqlite3.connect(db.as_uri()+'?mode=ro',uri=True)
thread='01a0c6aa-340f-7703-8fe8-4256283b700d'
a=int(datetime.fromisoformat(ex['started_at_utc']).timestamp());b=int(datetime.fromisoformat(ex['finished_at_utc']).timestamp())+1
q1='SELECT target,count(*) FROM logs WHERE thread_id=? GROUP BY target'
q2="SELECT id,ts,level,target,thread_id,process_uuid FROM logs WHERE ts BETWEEN ? AND ? AND (target LIKE '%policy%' OR target LIKE '%approval%' OR target LIKE '%sandbox%' OR target LIKE '%tools::router%') LIMIT 40"
queries=[{'sql':q1,'params':[thread],'rows':con.execute(q1,(thread,)).fetchall()},{'sql':q2,'params':[a,b],'rows':con.execute(q2,(a,b)).fetchall()}];con.close()
help_capture=[]
for args in [['--help'],['exec','--help'],['debug','--help']]:
    begun=datetime.now(timezone.utc).isoformat();p=subprocess.run(['codex',*args],capture_output=True,text=True)
    help_capture.append({'command':['codex',*args],'started_at_utc':begun,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
result={'captured_at_utc':start,'kind':'static artifact diagnosis, not regression/model/worker execution','bindings':bindings,'at05_code_matches_prelaunch':sha((ROOT/'artifacts/at05/experiment.py').read_bytes())==boundcode['sha256'],'stream_hashes_match_execution_receipt':{'stdout':sha(stdout)==ex['stdout_sha256'],'stderr':sha(stderr)==ex['stderr_sha256']},'worker_finished_before_review_started':datetime.fromisoformat(ex['finished_at_utc'])<datetime.fromisoformat(reviewex['started_at_utc']),'raw_error_items':[e for e in events if e.get('item',{}).get('type')=='error'],'serialized_other_tools':package['other_tools'],'review_package_keys':list(package),'review_execution_receipt_keys':list(package['execution']),'raw_stderr_content_in_package':stderr.decode('utf-8') in json.dumps(package,ensure_ascii=False),'stderr_hash_in_package':ex['stderr_sha256'] in json.dumps(package),'code_excerpts':excerpts,'policy_log_queries':{'database':str(db),'readonly':True,'scope':'exact thread and worker time-window policy metadata only','queries':queries},'cli_help':help_capture,'foundation_manifest_paths':[f['path'] for f in j('evidence/foundation-v0.1-manifest.json')['files']],'original_index_target_present':(ROOT/'artifacts/at05/recovery-receipt.json').exists()}
with (OUT/'diagnostic-evidence.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:result[k] for k in ['at05_code_matches_prelaunch','stream_hashes_match_execution_receipt','worker_finished_before_review_started','raw_stderr_content_in_package','stderr_hash_in_package','original_index_target_present']}))
