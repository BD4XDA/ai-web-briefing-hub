import hashlib, json, re, subprocess, time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os")
OUT = ROOT / "artifacts/at02/pilot-A"
OUT.mkdir(parents=True, exist_ok=True)
now = datetime.now(timezone.utc).isoformat()
checkpoint_id = "20260921T234855-578d72ce2f6e"

paths = {
    "router_package": Path(r"C:/Users/ASUS/.dsh/plugins/dsh-sol-luna-router/package.json"),
    "router_source": Path(r"C:/Users/ASUS/.dsh/plugins/dsh-sol-luna-router/src/router.js"),
    "models_source": Path(r"C:/Users/ASUS/.dsh/plugins/dsh-sol-luna-router/src/models.js"),
    "web_package": Path(r"C:/Users/ASUS/.dsh/profiles/web/package.json"),
    "cli_package": Path(r"C:/Users/ASUS/AppData/Roaming/npm/node_modules/@deepseek-ai/dsh/package.json"),
    "team_store": Path(r"C:/Users/ASUS/.dsh/storages/agent_team.json"),
}

def sha(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()

def write_capture(name, obj):
    p = OUT / name
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return str(p), sha(p)

def evidence(eid, p, scope, locator):
    return {"id": eid, "kind": "evidence", "path": str(p), "sha256": sha(Path(p)),
            "captured_at": now, "locator": locator, "scope": scope,
            "sensitivity": "local-metadata", "collector": "collector_pilot_a.py"}

def safe_package(p):
    d = json.loads(p.read_text(encoding="utf-8"))
    # Explicit allow-list avoids scripts, environment/config values and arbitrary package data.
    out = {k:d[k] for k in ("name", "version", "description", "type", "private", "repository") if k in d}
    for k in ("dependencies", "devDependencies"):
        if k in d and isinstance(d[k], dict): out[k+"_names"] = sorted(d[k])
    if isinstance(d.get("bin"), dict): out["bin_names"] = sorted(d["bin"])
    if isinstance(d.get("dsh"), dict):
        prof = d["dsh"].get("profile", {})
        if isinstance(prof, dict) and isinstance(prof.get("bundles"), list): out["dsh_profile_bundles"] = list(prof["bundles"])
    return out

def source_projection(p):
    s = p.read_text(encoding="utf-8")
    return {"path": str(p), "sha256": sha(p),
            "exported_names": re.findall(r"export (?:async )?function\\s+([A-Za-z0-9_]+)", s),
            "string_literals": sorted(set(re.findall(r'(?<![A-Za-z0-9_])"([a-z][a-z0-9_-]{2,})"', s))),
            "line_count": len(s.splitlines())}

team = json.loads(paths["team_store"].read_text(encoding="utf-8"))
tables = team.get("tables", {})
assistants = []
for a in (tables.get("assistants") or {}).values():
    assistants.append({k:a.get(k) for k in ("id","name","provider","model","reasoningEffort","agentPresetId","permissionPresetId","mcpServers","revision","updatedAt")})
teams = []
for t in (tables.get("teams") or {}).values():
    def count(v): return len(v) if isinstance(v, (dict,list)) else (0 if v in (None, "") else None)
    teams.append({k:t.get(k) for k in ("id","name","workspaceId","state","directMemberChat","revision","updatedAt")}|{
        "member_count": count(t.get("members")), "task_count": count(t.get("tasks")),
        "lease_count": count(t.get("leases")), "outbox_count": count(t.get("outbox"))})
team_proj = {"unit": team.get("unit"), "assistant_count": len(assistants), "assistants": assistants,
             "team_count": len(teams), "teams": teams, "message_count": len(tables.get("messages",{})),
             "activity_count": len(tables.get("activities",{})), "note": "message/activity content omitted by scope"}

router_proj = {"router_package": safe_package(paths["router_package"]),
               "router_sources": [source_projection(paths["router_source"]), source_projection(paths["models_source"])]}
package_proj = {"web_package": safe_package(paths["web_package"]), "cli_package": safe_package(paths["cli_package"])}

cmd = ["dsh", "--version"]
started = time.monotonic(); t0 = datetime.now(timezone.utc).isoformat()
try:
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=20, shell=False)
    exit_code, stdout, stderr = proc.returncode, proc.stdout, proc.stderr
except Exception as ex:
    exit_code, stdout, stderr = None, "", f"{type(ex).__name__}: {ex}"
finished = datetime.now(timezone.utc).isoformat(); duration = time.monotonic()-started
version_stream = {"command": cmd, "started_at_utc": t0, "finished_at_utc": finished,
                  "duration_seconds": duration, "exit_code": exit_code, "stdout": stdout, "stderr": stderr}

_, _ = write_capture("router-projection.json", router_proj)
_, _ = write_capture("package-projection.json", package_proj)
_, _ = write_capture("team-projection.json", team_proj)
version_path, _ = write_capture("cli-version-stream.json", version_stream)

ev = [evidence("A-E1", OUT/"router-projection.json", "router package and two source projections", "JSON keys router_package/router_sources"),
      evidence("A-E2", OUT/"package-projection.json", "web and CLI package projections", "JSON keys web_package/cli_package"),
      evidence("A-E3", OUT/"team-projection.json", "agent-team safe metadata projection", "JSON keys assistants/teams/counts"),
      evidence("A-E4", version_path, "installed CLI version command stream", "JSON keys command/exit_code/stdout/stderr"),
      {"id":"A-E5","kind":"evidence","path":str(ROOT/"CHECKPOINT.md"),"sha256":sha(ROOT/"CHECKPOINT.md"),"captured_at":now,"locator":"Checkpoint ID line","scope":"latest committed project state","sensitivity":"local-metadata","collector":"collector_pilot_a.py"}]

common = lambda id,label,status,eids,facts,unknowns: {"id":id,"label":label,"observed_at":now,"status":status,"evidence_ids":eids,"facts":facts,"unknowns":unknowns}
records = [
 {**common("harness-dsh-router","DSH Sol/Luna router plugin","configured",["A-E1","A-E2"],
           ["Router package and source projections were captured from the approved local plugin path.","Two inspected source files expose state gating and model catalog helpers."],
           ["No live provider/API invocation was performed; currently-live status is unknown."]),"kind":"agent-harness","entity_type":"plugin","model_id":"unknown","harness":"DSH","capabilities":["routing","agent state gating","model catalog projection"]},
 {**common("agent-team-templates","Stored DSH agent/team templates","configured",["A-E3"],
           [f"{len(assistants)} assistant template records and {len(teams)} team records were projected by allow-listed fields.","Stored team states include active and error values as metadata."],
           ["Stored configuration does not establish a running agent or live team."]),"kind":"agent-harness","entity_type":"agent","model_id":"gpt-5.6-sol / unknown per record","harness":"DSH agent-team storage","capabilities":["configured assistant templates","team metadata"]},
 {**common("workspace-dsh-web","Installed DSH web profile","configured",["A-E2"],
           ["Approved web package manifest declares DSH bundles and a file-linked Sol/Luna router dependency."],
           ["Profile process liveness and loaded runtime state were not tested."]),"kind":"workspace","root_path":r"C:/Users/ASUS/.dsh/profiles/web","coverage":"bounded-sample","sampled_files":1,"duplicate_candidates":[]},
 {**common("project-lab-research-os","Canonical lab research OS project","observed",["A-E5"],
           ["Latest committed checkpoint is 20260921T183240-2a5430059765 as loaded before collection."],
           ["Checkpoint is a historical snapshot and does not prove live infrastructure state."]),"kind":"project","project_id":"lab-research-os","root_path":str(ROOT),"repository_path":str(ROOT.parent.parent),"root_discovery":"PROJECT.md and .lab-project.json"},
 {**common("memory-canonical-rules","Canonical project instruction and memory anchors","configured",["A-E5"],
           ["AGENTS.md, PROJECT.md and CHECKPOINT.md are present in the approved project root."],
           ["Worker did not inspect global auth/config or infer loader behavior."]),"kind":"instruction-memory","path":str(ROOT/"AGENTS.md"),"owner":"Human PI / Astra architecture","authority":"AGENTS.md and PROJECT.md","loader":"project procedure; runtime loader not tested"}
]

collection = {"task_id":"AT02-pilot-A","collected_at":now,"baseline_checkpoint":checkpoint_id,"expected_checkpoint":"20260921T183037-034ade6bf069","scope":{"max_files":30,"max_depth":2,"files_sampled":8,"omitted":["message/activity content","secrets/auth/env/config values","full drive/corpus","live APIs"]},"selection_policy":"Approved packet paths only; two router source files; allow-listed projections; no symlink traversal.","evidence":ev,"records":records,"omissions":[{"item":"stored message/activity payloads","reason":"excluded sensitive/unnecessary content"},{"item":"live process/provider state","reason":"no service/API calls authorized"}]}
bundle = {"task_id":"AT02-pilot-A","schema_version":1,"records":records,"evidence_records":ev,"reports":[]}
execution = {"task_id":"AT02-pilot-A","command":["python",str(OUT/"collector_pilot_a.py")],"collector_source":str(OUT/"collector_pilot_a.py"),"collector_source_sha256":sha(OUT/"collector_pilot_a.py"),"started_at_utc":now,"finished_at_utc":datetime.now(timezone.utc).isoformat(),"duration_seconds":duration,"exit_code":0,"stdout":"machine-generated projections written to assigned artifact path","stderr":"","streams":[version_stream],"model_calls":0}
observations = {"task_id":"AT02-pilot-A","context":{"loaded":["AGENTS.md","PROJECT.md","CHECKPOINT.md","decisions/0003-foundation-v0.1.md","protocols/AT02-PILOTS.md","packets/at02-pilot-A.json","packets/at02-pilot-A.md"],"necessary":["approved manifests and storage projection"],"missing":["live runtime/API state"],"excess":[],"context_failure":None},"task_type":"bounded infrastructure metadata census","capability_required":["filesystem metadata projection","schema-bound record assembly"],"requested_model":"unknown","requested_harness":"local Python collector","routing_outcome":"local collector executed","routing_mismatch":"none observed; live model/harness identity not applicable"}
report = {"id":"AT02-pilot-A-worker-report","claim":"Bounded machine-captured projections and schema-shaped records were assembled for approved DSH/agent/routing sources.","evidence_ids":[e["id"] for e in ev],"verification_method":"Deterministic local collection and schema validation pending coordinator review","result":"UNCERTAIN","confidence":0.82,"anomaly_conflict":[],"reviewer":"pilot-A-worker","model_reported":"unknown","harness":"local Python collector","observed_at":now}
for name,obj in [("collection.json",collection),("candidate-bundle.json",bundle),("execution.json",execution),("observations.json",observations),("worker-report.json",report)]:
    (OUT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")
print(json.dumps({"out":str(OUT),"evidence":len(ev),"records":len(records),"cli_exit":exit_code},ensure_ascii=False))
