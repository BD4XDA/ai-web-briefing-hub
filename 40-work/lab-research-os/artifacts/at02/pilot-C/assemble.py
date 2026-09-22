import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = Path(r"C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os")
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def utc(): return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
raw = OUT / "raw-capture.json"
idx = OUT / "index-snapshot.md"
execution = OUT / "execution.json"
collector = OUT / "collector.py"
cap = json.loads(raw.read_text(encoding="utf-8"))
captured = cap["captured_at"]
evidence = [
    {"id":"ev-pilot-C-capture","kind":"evidence","path":str(raw),"sha256":sha(raw),"captured_at":captured,"locator":"raw-capture.json; complete bounded machine capture","scope":"top-level listing and 00_总索引 metadata through depth 2","sensitivity":"local-metadata","collector":"collector.py"},
    {"id":"ev-pilot-C-index","kind":"evidence","path":str(idx),"sha256":sha(idx),"captured_at":captured,"locator":"index-snapshot.md; exact bytes of one safe text index","scope":"explicit index structure/association only; no paper bodies","sensitivity":"local-metadata","collector":"collector.py"}
]
workspace = {
    "id":"workspace-pilot-C-literature-index","label":"Pilot C 00_总索引 literature area","observed_at":captured,"status":"observed","evidence_ids":["ev-pilot-C-capture","ev-pilot-C-index"],
    "facts":["The packet-preferred 00_总索引 directory exists.","The bounded area contains one regular Markdown index file at depth 1.","The safe index explicitly presents itself as a daily literature index and records archive status fields."],
    "unknowns":["Drive-wide corpus contents and coverage are unknown.","No scientific content was read or inferred from filenames.","No duplicate candidate was established from the bounded sample."],"kind":"workspace","root_path":cap["selection"]["selected_area"],"coverage":"bounded-sample","sampled_files":len(cap["selected_area_files"]),"duplicate_candidates":[]
}
project = {
    "id":"project-pilot-C-literature-association","label":"Pilot C literature area association","observed_at":captured,"status":"unknown","evidence_ids":["ev-pilot-C-capture","ev-pilot-C-index"],
    "facts":["The safe index provides explicit index structure and archive-status fields within the selected literature area."],
    "unknowns":["A supported project identifier or repository association is not established by this bounded metadata capture."],"kind":"project","project_id":"unknown","root_path":cap["source_root"],"repository_path":"unestablished","root_discovery":"Packet-approved source root; 00_总索引 selected because it exists and is the preferred index area."
}
collection = {
    "task_id":"AT02-pilot-C","capture_method":"programmatic OS metadata capture by collector.py; safe index bytes copied verbatim","captured_at":captured,
    "selection":cap["selection"],"top_level_listing":cap["top_level_listing"],"selected_area_directories":cap["selected_area_directories"],"selected_area_files":cap["selected_area_files"],"safe_index":cap["safe_index"],
    "evidence_ids":["ev-pilot-C-capture","ev-pilot-C-index"],"omitted":["all non-selected literature areas","symlinked entries","depth > 2","PDFs and paper bodies","secret/auth/config values"],"unknowns":workspace["unknowns"]
}
bundle = {"task_id":"AT02-pilot-C","records":[workspace,project],"evidence":evidence,"reports":[]}
observations = {
    "task_id":"AT02-pilot-C","loaded_context":["CHECKPOINT.md latest 20260921T183240-2a5430059765","packets/at02-pilot-C.json and .md","protocols/AT02-PILOTS.md","decisions/0003-foundation-v0.1.md"],
    "necessary_context":["Packet-approved literature root and bounded selection rules","workspace/project/evidence/verification schemas"],"missing_context":["Independent DeepSeek verification, not run during collection"],"excess_context":[],"context_failure":None,
    "task_type":"bounded metadata collection","capability_required":"local filesystem metadata capture","requested_model":"none","requested_harness":"local Python process","routing_outcome":"executed locally without model call","routing_mismatch":None,
    "baseline_checkpoint":"20260921T183037-034ade6bf069","observed_checkpoint":"20260921T183240-2a5430059765","difference":"P2 dispatch checkpoint is newer and adds the pilot packets; no source-data change observed."
}
report = {"id":"verification-pilot-C-worker","claim":"Bounded metadata capture completed for the packet-preferred 00_总索引 area within the allowed literature root.","evidence_ids":["ev-pilot-C-capture","ev-pilot-C-index"],"verification_method":"Worker self-report of program-created capture and schema-shaped records; independent DeepSeek review pending.","result":"UNCERTAIN","confidence":0.7,"anomaly_conflict":["Independent verification has not yet occurred; candidate bundle reports intentionally empty per protocol."],"reviewer":"pilot-C-worker","model_reported":"none","harness":"local Python process","observed_at":utc()}
for name, value in [("collection.json",collection),("candidate-bundle.json",bundle),("observations.json",observations),("worker-report.json",report)]:
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
e = json.loads(execution.read_text(encoding="utf-8-sig")); e["collector_source_sha256"] = sha(collector); e["capture_evidence_sha256"]={"raw-capture.json":sha(raw),"index-snapshot.md":sha(idx)}
execution.write_text(json.dumps(e,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"records":2,"evidence":2,"reports":0,"collector_source_sha256":e["collector_source_sha256"]},ensure_ascii=False))
