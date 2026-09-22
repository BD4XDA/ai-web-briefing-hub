import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import foundation  # noqa: E402


FIELDS = foundation.FIELDS


def record(**overrides):
    value = {
        "priority": "P1",
        "status": "checkpointed",
        "current_verified_state": ["ready"],
        "completed": ["fixture"],
        "decisions": ["keep state"],
        "open_questions": [],
        "known_risks": [],
        "in_progress": [],
        "next_actions": ["resume"],
        "evidence_references": ["evidence/fixture.json"],
    }
    value.update(overrides)
    return value


class FoundationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / ".lab-project.json").write_text(
            '{"project_id":"lab-research-os"}', encoding="utf-8"
        )
        (self.root / "SOL-AGENT.md").write_text(
            "# Sol adapter\n\nStable manual content.\n", encoding="utf-8"
        )
        (self.root / "nested" / "child").mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def test_project_root_is_marker_identity_not_directory_name(self):
        self.assertEqual(self.root, foundation.project_root(self.root / "nested" / "child"))
        (self.root / ".lab-project.json").write_text(
            '{"project_id":"wrong-project"}', encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "Unexpected project identity"):
            foundation.project_root(self.root / "nested")

    def test_checkpoint_requires_all_fields_and_evidence(self):
        missing = record()
        missing.pop("evidence_references")
        with self.assertRaisesRegex(ValueError, "Missing continuity fields"):
            foundation.checkpoint(self.root, missing, "none")
        empty_evidence = record(evidence_references=[])
        with self.assertRaisesRegex(ValueError, "evidence references"):
            foundation.checkpoint(self.root, empty_evidence, "none")

    def test_normal_checkpoint_writes_and_current_verifies_hash(self):
        ident = foundation.checkpoint(self.root, record(), "none")
        current_id, current_record = foundation.current(self.root)
        self.assertEqual(ident, current_id)
        snapshot = self.root / "checkpoints" / f"{ident}.json"
        pointer = json.loads((self.root / "checkpoints" / "LATEST.json").read_text())
        self.assertEqual(pointer["id"], ident)
        self.assertEqual(pointer["sha256"], hashlib.sha256(snapshot.read_bytes()).hexdigest())
        self.assertEqual(current_record["parent"], None)
        sol = (self.root / "SOL-AGENT.md").read_text(encoding="utf-8")
        self.assertIn("Stable manual content.", sol)
        self.assertIn(f"Checkpoint ID: {ident}", sol)
        self.assertEqual(sol.count(foundation.SOL_START), 1)
        self.assertEqual(sol.count(foundation.SOL_END), 1)

    def test_stale_expected_rejected_and_old_state_remains(self):
        ident = foundation.checkpoint(self.root, record(), "none")
        with self.assertRaisesRegex(RuntimeError, "Stale writer"):
            foundation.checkpoint(self.root, record(completed=["must not commit"]), "none")
        self.assertEqual(foundation.current(self.root)[0], ident)
        self.assertNotIn("must not commit", json.dumps(foundation.current(self.root)[1]))

    def test_existing_writer_lock_is_rejected_and_preserved(self):
        checkpoints = self.root / "checkpoints"
        checkpoints.mkdir()
        lock = checkpoints / "writer.lock"
        lock.write_text("other-writer", encoding="ascii")
        with self.assertRaisesRegex(RuntimeError, "writer lock exists"):
            foundation.checkpoint(self.root, record(), "none")
        self.assertTrue(lock.exists())
        self.assertEqual(lock.read_text(encoding="ascii"), "other-writer")

    def test_snapshot_tampering_is_rejected(self):
        ident = foundation.checkpoint(self.root, record(), "none")
        snapshot = self.root / "checkpoints" / f"{ident}.json"
        snapshot.write_text(snapshot.read_text(encoding="utf-8") + "\n tampered", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "integrity conflict"):
            foundation.current(self.root)

    def test_checkpoint_replace_failure_does_not_advance_latest(self):
        old_id = foundation.checkpoint(self.root, record(), "none")
        latest = self.root / "checkpoints" / "LATEST.json"
        before = latest.read_bytes()
        real_replace = foundation.os.replace

        def fail_snapshot_replace(source, destination):
            if Path(destination) == self.root / "CHECKPOINT.md":
                raise OSError("simulated CHECKPOINT replace failure")
            return real_replace(source, destination)

        with mock.patch.object(foundation.os, "replace", side_effect=fail_snapshot_replace):
            with self.assertRaises(OSError):
                foundation.checkpoint(self.root, record(completed=["new state"]), old_id)
        self.assertEqual(latest.read_bytes(), before)
        self.assertEqual(foundation.current(self.root)[0], old_id)
        self.assertFalse((self.root / "checkpoints" / "writer.lock").exists())

    def test_sol_agent_replace_failure_does_not_advance_latest(self):
        old_id = foundation.checkpoint(self.root, record(), "none")
        latest = self.root / "checkpoints" / "LATEST.json"
        before = latest.read_bytes()
        real_replace = foundation.os.replace

        def fail_sol_replace(source, destination):
            if Path(destination) == self.root / "SOL-AGENT.md":
                raise OSError("simulated SOL-AGENT replace failure")
            return real_replace(source, destination)

        with mock.patch.object(foundation.os, "replace", side_effect=fail_sol_replace):
            with self.assertRaises(OSError):
                foundation.checkpoint(self.root, record(completed=["new state"]), old_id)
        self.assertEqual(latest.read_bytes(), before)
        self.assertEqual(foundation.current(self.root)[0], old_id)
        self.assertFalse((self.root / "checkpoints" / "writer.lock").exists())

    def test_checkpoint_requires_sol_agent(self):
        (self.root / "SOL-AGENT.md").unlink()
        with self.assertRaisesRegex(ValueError, "SOL-AGENT.md is required"):
            foundation.checkpoint(self.root, record(), "none")
        self.assertFalse((self.root / "checkpoints" / "LATEST.json").exists())

    def test_legacy_hub_current_backup_is_an_exact_prefix(self):
        backup = ROOT / "evidence" / "legacy" / "hub-CURRENT-before-20260921.md"
        hub_current = ROOT.parents[1] / "60-handoffs" / "CURRENT.md"
        self.assertTrue(backup.is_file())
        self.assertTrue(hub_current.is_file())
        old = backup.read_text(encoding="utf-8")
        current = hub_current.read_text(encoding="utf-8")
        self.assertTrue(current.startswith(old))


if __name__ == "__main__":
    unittest.main(verbosity=2)
