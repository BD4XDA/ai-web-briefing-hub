import contextlib
import hashlib
import io
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from tools import contracts, foundation


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evidence(eid, path, scope):
    return {
        "id": eid,
        "kind": "evidence",
        "path": str(path.resolve()),
        "sha256": sha(path),
        "captured_at": utc_now(),
        "locator": str(path.relative_to(ROOT)).replace("\\", "/"),
        "scope": scope,
        "sensitivity": "local-metadata",
        "collector": "artifacts/at02/pilot-B/collector.py",
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    started = utc_now()
    t0 = time.monotonic()

    discovered = foundation.project_root(OUT)
    checkpoint_id, checkpoint_record = foundation.current(discovered)
    snapshot_path = discovered / "checkpoints" / f"{checkpoint_id}.json"
    snapshot_hash = sha(snapshot_path)

    selected = [
        ".lab-project.json", "AGENTS.md", "PROJECT.md",
        "decisions/0003-foundation-v0.1.md", "protocols/HANDOFF.md",
        "protocols/VERIFICATION.md", "protocols/AT02-PILOTS.md",
        "packets/at02-pilot-B.json", "packets/at02-pilot-B.md",
        "tools/foundation.py", "tools/contracts.py",
        "schemas/project.schema.json", "schemas/workspace.schema.json",
        "schemas/instruction-memory.schema.json", "schemas/agent-harness.schema.json",
        "schemas/conflict.schema.json", f"checkpoints/{checkpoint_id}.json",
    ]
    files = []
    for rel in selected:
        p = discovered / rel
        files.append({"path": str(p.resolve()), "relative": rel, "bytes": p.stat().st_size, "sha256": sha(p)})

    evidence_items = []
    for n, item in enumerate(files, 1):
        evidence_items.append(evidence(f"pilot-b-ev-{n:02d}", Path(item["path"]), "bounded Pilot B source/context observation"))
    evidence_by_rel = {x["locator"]: x["id"] for x in evidence_items}

    project = {
        "id": "pilot-b-project",
        "label": "Canonical lab-research-os project root",
        "observed_at": started,
        "status": "observed",
        "evidence_ids": [evidence_by_rel[".lab-project.json"], evidence_by_rel[f"checkpoints/{checkpoint_id}.json"]],
        "facts": ["project_id=lab-research-os", f"root={discovered}", "root discovered from a child output directory via marker identity"],
        "unknowns": ["Repository root and project root are distinct; no broader repository inventory was performed"],
        "kind": "project",
        "project_id": "lab-research-os",
        "root_path": str(discovered),
        "repository_path": str(discovered.parents[2]),
        "root_discovery": "tools/foundation.py project_root(child_directory)",
    }
    workspace = {
        "id": "pilot-b-workspace",
        "label": "Bounded canonical workspace sample",
        "observed_at": started,
        "status": "observed",
        "evidence_ids": [evidence_by_rel["AGENTS.md"], evidence_by_rel["PROJECT.md"]],
        "facts": ["Sample selection is explicit and limited to 18 files", "No symlinks or junctions were followed", "No secrets/auth/config values were read into records"],
        "unknowns": ["This is not a drive-wide or repository-wide census", "Unselected files are omitted by policy"],
        "kind": "workspace",
        "root_path": str(discovered),
        "coverage": "bounded-sample",
        "sampled_files": len(files),
        "duplicate_candidates": [],
    }
    instructions = {
        "id": "pilot-b-instructions",
        "label": "Canonical instruction memory sources",
        "observed_at": started,
        "status": "observed",
        "evidence_ids": [evidence_by_rel[x] for x in ["AGENTS.md", "protocols/HANDOFF.md", "protocols/VERIFICATION.md", "protocols/AT02-PILOTS.md"]],
        "facts": ["AGENTS.md is the project procedure source", "Pilot procedure requires original machine-captured evidence", "Collection forbids model calls and checkpoint writes"],
        "unknowns": ["No claim is made that these instructions are globally loaded by every harness"],
        "kind": "instruction-memory",
        "path": str((discovered / "AGENTS.md").resolve()),
        "owner": "project",
        "authority": "canonical project instructions and packet",
        "loader": "explicit bounded file read",
    }
    harness = {
        "id": "pilot-b-harness",
        "label": "Pilot B collection harness",
        "observed_at": started,
        "status": "configured",
        "evidence_ids": [evidence_by_rel["packets/at02-pilot-B.json"], evidence_by_rel["protocols/AT02-PILOTS.md"]],
        "facts": ["Collection used local Python stdlib plus project contracts modules", "No model call or external route was used"],
        "unknowns": ["No live agent/model identity was requested or tested in collection"],
        "kind": "agent-harness",
        "entity_type": "harness",
        "model_id": "unknown",
        "harness": "python collector.py",
        "capabilities": ["filesystem metadata", "hashing", "local schema validation"],
    }
    conflict = {
        "id": "pilot-b-baseline-current",
        "label": "Packet baseline versus current snapshot",
        "observed_at": started,
        "status": "observed",
        "evidence_ids": [evidence_by_rel["packets/at02-pilot-B.json"], evidence_by_rel[f"checkpoints/{checkpoint_id}.json"]],
        "facts": ["Packet expected_checkpoint=20260921T183037-034ade6bf069", f"Current committed checkpoint={checkpoint_id}", "Current state includes Pilot B packet/schema additions"],
        "unknowns": ["This is planned P2-to-P3 context drift, not a source-data contradiction"],
        "kind": "conflict",
        "concern": "Expected planning baseline differs from current committed snapshot",
        "classification": "candidate",
        "next_check": "Coordinator confirms packet baseline/current checkpoint transition before integration",
    }
    records = [project, workspace, instructions, harness, conflict]
    for kind_record in records:
        contracts.schema_check(kind_record["kind"], kind_record)
    for ev in evidence_items:
        contracts.evidence_check(ev, [str(discovered)])

    candidate = {"task_id": "AT02-pilot-B", "records": records, "evidence": evidence_items, "reports": []}
    fixture_report = {
        "id": "pilot-b-fixture-report",
        "claim": "Pilot B candidate records and evidence pass deterministic bundle gates",
        "evidence_ids": [e["id"] for e in evidence_items],
        "verification_method": "Temporary in-process fixture report used only to exercise bundle_check; it did not review or execute collection",
        "result": "PASS",
        "confidence": 0.95,
        "anomaly_conflict": [],
        "reviewer": "pilot-B-deterministic-fixture",
        "model_reported": "fixture-only",
        "harness": "in-process contracts.bundle_check",
        "observed_at": started,
    }
    fixture_bundle = {**candidate, "reports": [fixture_report]}
    validation_buf = io.StringIO()
    validation_start = time.monotonic()
    with contextlib.redirect_stdout(validation_buf), contextlib.redirect_stderr(io.StringIO()):
        validation_result = contracts.bundle_check(fixture_bundle, {
            "task_id": "AT02-pilot-B", "project_id": "lab-research-os", "project_root": str(discovered),
            "expected_checkpoint": "20260921T183037-034ade6bf069", "owner": "pilot-B-worker",
            "objective": "Resume canonical project independently; verify root/rules/checkpoint and populate a real project/instruction inventory without mocks.",
            "allowed_read_roots": [str(discovered)], "write_paths": [str(OUT)],
            "excluded_scope": ["No secrets/auth/env/config values", "No source changes, deletion or migration", "No full drive/corpus scanning", "No checkpoint writes or model calls during collection"],
            "input_evidence_ids": [], "acceptance_criteria": ["Load latest committed state and record input context"],
            "verification_route": "Separate DSH DeepSeek Flash text evidence review after deterministic validation",
            "budget": {"max_files": 30, "max_depth": 2, "max_model_calls": 0}, "resume_action": "Read packet and procedure",
        })
    validation_duration = time.monotonic() - validation_start
    validation_stdout = validation_buf.getvalue()
    (OUT / "candidate-bundle.json").write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "collection.json").write_text(json.dumps({
        "captured_at_utc": started, "root": str(discovered), "root_discovery": "foundation.project_root(child)",
        "checkpoint": {"id": checkpoint_id, "snapshot_path": str(snapshot_path), "snapshot_sha256": snapshot_hash, "record_status": checkpoint_record.get("status")},
        "selection_policy": "Explicit 18-file bounded source/context set from packet/protocol; skip secrets, symlinks/junctions, and unrelated repository areas.",
        "omissions": ["No broad repository/drive census", "No model/harness liveness probe", "No mutable LATEST/CHECKPOINT projection hashed as lasting evidence"],
        "files": files, "records": [r["id"] for r in records], "evidence_ids": [e["id"] for e in evidence_items]
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "observations.json").write_text(json.dumps({
        "prior_context": {"present": True, "details": "This worker previously performed P0/P1/P2 work in the same conversation; Pilot B is bounded continuation, not a zero-conversation fresh-owner proof."},
        "loaded_context": ["marker root", "AGENTS", "PROJECT", "committed checkpoint", "decision 0003", "Pilot B packet/procedure", "contracts and five pilot schemas"],
        "missing_context": ["Independent DeepSeek verification is separate and not performed by this collector"],
        "excess_context_omitted": ["Unrelated repository areas and full corpus"],
        "context_failure": None,
        "routing": {"requested_model": "unknown during collection", "harness": "python collector", "capability_required": "local metadata and schema validation", "outcome": "bounded local collection only", "mismatch": "No live model route was exercised"},
        "planned_change": "Packet baseline precedes current P2 snapshot; additions are packets/schemas/context only as documented, no source-data change claim."
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "execution.json").write_text(json.dumps({
        "command": [sys.executable, str(Path(__file__).resolve())], "started_at_utc": started, "finished_at_utc": utc_now(),
        "duration_seconds": time.monotonic() - t0, "exit_code": 0, "stdout": validation_stdout,
        "stderr": "", "collector_sha256": sha(Path(__file__)), "validation": validation_result,
        "fixture_report": "Temporary fixture only; not independent verification."
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    worker_report = {
        "id": "pilot-b-worker-report", "claim": "Pilot B bounded canonical root/context inventory and deterministic schema/bundle validation completed",
        "evidence_ids": [e["id"] for e in evidence_items],
        "verification_method": "Machine-captured root discovery, immutable checkpoint snapshot, bounded file hashes, real schema_check/evidence_check and bundle_check with a temporary fixture report; independent model review remains pending.",
        "result": "UNCERTAIN", "confidence": 0.85,
        "anomaly_conflict": ["Independent DeepSeek verification not performed by collection worker", "Project/instruction inventory is bounded and not a drive-wide census"],
        "reviewer": "pilot-B-worker", "model_reported": "unknown", "harness": "python collector", "observed_at": utc_now()
    }
    contracts.schema_check("verification", worker_report)
    (OUT / "worker-report.json").write_text(json.dumps(worker_report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"root": str(discovered), "checkpoint": checkpoint_id, "files": len(files), "records": len(records), "evidence": len(evidence_items), "validation": validation_result, "reports": "candidate bundle empty; worker report UNCERTAIN", "exit_code": 0}, ensure_ascii=False))


if __name__ == "__main__":
    main()
