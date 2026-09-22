"""Bounded offline regression. Synthetic fixtures NEVER certify a real worker."""
import copy,hashlib,json,tempfile,unittest
from pathlib import Path
from local_repair import normalize,acceptance,bind_stream,bind_execution,review_gate
ROOT=Path(__file__).resolve().parents[2]
def digest(b):return hashlib.sha256(b).hexdigest()
def event(t,**kw):return {'type':'item.completed','item':{'id':'a','type':t,**kw}}
def good_review():return {'reason':{'kind':'completed'},'tool_calls':0,'text':json.dumps({'claim':'synthetic gate fixture only','evidence':'synthetic','verification_method':'fixture','result':'PASS','confidence':.9,'anomaly_conflict':[],'limitations':['NOT actual model evidence']})}
def evaluate(events=None,**overrides):
    params=dict(observation_present=True,candidate_exact=True,scope_by_action={'a':True},execution_status='SUCCESS',review_result='PASS',evidence_complete=True,checkpoint_equal=True,writeback_equal=True)
    params.update(overrides)
    return acceptance(normalize(events if events is not None else [event('command_execution',exit_code=0,command='synthetic-observation')]),**params)
class Regression(unittest.TestCase):
    def record(self,name,actual,expected,kind='synthetic'):
        print(json.dumps({'case':name,'fixture_kind':kind,'actual':actual,'expected':expected}))
        self.assertEqual(actual,expected)
    def test_A_original_event(self):
        raw=(ROOT/'artifacts/at05/worker.stdout').read_text(encoding='utf-8')
        events=[json.loads(s) for s in raw.splitlines()];n=normalize(events)
        self.record('A-original-actions',n['action_count'],0,'retained real AT05 events; offline replay only')
        self.assertTrue(n['diagnostics']);self.assertEqual(n['diagnostics'][0]['event']['item']['type'],'error')
        result=evaluate(events,observation_present=False,candidate_exact=None,execution_status='BLOCKED',review_result='UNCERTAIN')
        self.record('A-original-result',[result['result'],result['C1'],result['writeback_allowed']],['UNCERTAIN','NOT PROVEN',False],'offline replay, no historical-result rewrite')
    def test_B_positive(self):
        x=evaluate();self.record('B-all-conditions',[x['result'],x['writeback_allowed'],x['classification_correctness']],['PASS',True,'NOT_SELF_CERTIFIED'])
    def test_C_execution(self):
        for state,expected in [('BLOCKED','UNCERTAIN'),('FAIL','FAIL'),('TIMEOUT','FAIL')]:
            x=evaluate(observation_present=False,execution_status=state);self.record('C-'+state,[x['result'],x['writeback_allowed'],x['execution_status']],[expected,False,state])
        self.record('C-top-level-success-command-failed',evaluate([event('command_execution',exit_code=7)])['result'],'FAIL')
    def test_D_outside(self):
        for name in ['synthetic-destructive','synthetic-out-of-root']:
            x=evaluate([event('command_execution',exit_code=0,command=name)],scope_by_action={'a':False})
            self.record('D-'+name,[x['result'],x['writeback_allowed']],['FAIL',False])
    def test_E_types_order(self):
        for ev in [event('future_type'),{'type':'item.completed','item':[]},None,{'type':'alien'}]:
            self.record('E-unknown-or-malformed',evaluate([ev])['writeback_allowed'],False)
        evs=[event('warning',message='synthetic diagnostic'),event('file_change',changes=['synthetic-outside'])]
        n=normalize(evs);self.record('E-mixed-order',[x['kind'] for x in n['order']],['diagnostic','action'])
        self.record('E-mixed-action-not-hidden',evaluate(evs,scope_by_action={'a':False})['result'],'FAIL')
        evs=[{'type':'item.started','item':{'id':'a','type':'command_execution'}},event('command_execution',exit_code=0)]
        self.record('E-deduplicated-lifecycle',normalize(evs)['action_count'],1)
        self.record('E-started-not-completed',evaluate(evs[:1])['writeback_allowed'],False)
    def test_FG_streams(self):
        with tempfile.TemporaryDirectory(prefix='at07-synthetic-') as td:
            root=Path(td);p=root/'stream';p.write_bytes(b'captured stderr')
            def bind(**kw):
                args=dict(root=root,expected_hash=digest(p.read_bytes()),captured=True,truncated=False);args.update(kw)
                return bind_stream(p,**args)
            x=bind();self.record('F-nonempty',[x['status'],x['complete'],x['content']],['CAPTURED',True,'captured stderr'])
            p.write_bytes(b'');self.record('F-empty',bind()['status'],'EMPTY')
            self.record('F-not-captured',bind(captured=False)['status'],'NOT_CAPTURED')
            self.record('F-missing',bind_stream(root/'absent',root=root,expected_hash=digest(b''),captured=True,truncated=False)['status'],'MISSING')
            self.record('F-truncated',bind(truncated=True)['status'],'TRUNCATED')
            self.record('F-unspecified-capture',bind(truncated=None)['complete'],False)
            p.write_bytes(b'changed');self.record('G-tampered',bind(expected_hash=digest(b'original'))['status'],'TAMPERED')
            self.record('G-size',bind(max_bytes=2)['status'],'OVERSIZED')
            p.write_bytes(b'\xff');self.record('G-encoding',bind()['status'],'INVALID_ENCODING')
            p.write_bytes(('sk-'+'Z'*32).encode());x=bind();self.record('G-synthetic-secret',[x['status'],x['complete'],'content' in x],['WITHHELD_SAFETY',False,False])
            p.write_bytes(b'ordinary');self.record('G-explicit-withhold',bind(safety_withheld=True)['status'],'WITHHELD_SAFETY')
            self.record('G-outside-root',bind_stream(p,root=root/'restricted',expected_hash=digest(b'ordinary'),captured=True,truncated=False)['status'],'OUT_OF_SCOPE')
            rec={'pid':42,'stdout_sha256':digest(b'ordinary'),'stderr_sha256':digest(b'ordinary')}
            x=bind_execution(rec,p,p,root=root,capture_states={'stdout':{'captured':True,'truncated':False}})
            self.record('G-no-silent-empty-missing-receipt',[x['complete'],x['streams']['stderr']['status']],[False,'NOT_CAPTURED'])
    def test_H_review(self):
        self.record('H-positive-fixture',review_gate(good_review(),0),'PASS')
        variants=[None,{},dict(good_review(),text='not json'),dict(good_review(),tool_calls=1),dict(good_review(),tool_calls=False),dict(good_review(),reason={'kind':'max_tokens'})]
        for field,val in [('confidence',.79),('confidence',True),('anomaly_conflict',['unresolved']),('result','UNCERTAIN'),('result','other')]:
            w=good_review();r=json.loads(w['text']);r[field]=val;w['text']=json.dumps(r);variants.append(w)
        for i,w in enumerate(variants):
            rg=review_gate(w,0);self.record('H-reject-'+str(i),evaluate(review_result=rg)['writeback_allowed'],False)
    def test_I_stale_mismatch(self):
        for field in ['checkpoint_equal','writeback_equal']:
            x=evaluate(**{field:False});self.record('I-'+field,[x['result'],x['writeback_allowed']],['FAIL',False])
    def test_real_stream_binding(self):
        d=ROOT/'artifacts/at05';rec=json.loads((d/'worker-execution.json').read_text(encoding='utf-8'))
        package=bind_execution(rec,d/'worker.stdout',d/'worker.stderr',root=ROOT,capture_states={n:{'captured':True,'truncated':False} for n in ['stdout','stderr']})
        # Original process.communicate saved complete captured bytes before recording hashes.
        self.record('F5-original-streams-bound',package['complete'],True,'retained real stream bytes; no worker execution')
        self.assertIn('blocked by policy',package['streams']['stderr']['content'])
        self.assertEqual(package['streams']['stderr']['sha256'],rec['stderr_sha256'])
if __name__=='__main__':unittest.main(verbosity=2)
