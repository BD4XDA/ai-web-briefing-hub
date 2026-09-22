import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import contracts  # noqa: E402

REAL_SCHEMA_CHECK = contracts.schema_check


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.evidence_dir = self.root / "evidence"
        self.evidence_dir.mkdir()
        (self.root / ".lab-project.json").write_text(
            '{"project_id":"lab-research-os"}', encoding="utf-8"
        )
        self.evidence_file = self.evidence_dir / "fixture.txt"
        self.evidence_file.write_text("stable evidence\n", encoding="utf-8")
        self.packet = self.make_packet()
        self.evidence = self.make_evidence()
        self.report = self.make_report()

    def tearDown(self):
        self.tmp.cleanup()

    def make_packet(self, **changes):
        packet = {
            "task_id": "contract-test",
            "project_id": "lab-research-os",
            "project_root": str(self.root),
            "expected_checkpoint": "none",
            "owner": "worker",
            "objective": "validate contracts",
            "allowed_read_roots": [str(self.evidence_dir)],
            "write_paths": [str(self.root / "evidence" / "out.json")],
            "excluded_scope": ["models"],
            "input_evidence_ids": [],
            "acceptance_criteria": ["deterministic"],
            "verification_route": "unittest",
            "budget": {"max_files": 5, "max_depth": 2, "max_model_calls": 0},
            "resume_action": "reload packet",
        }
        packet.update(changes)
        return packet

    def make_evidence(self, **changes):
        value = {
            "id": "ev-1",
            "kind": "evidence",
            "path": str(self.evidence_file),
            "sha256": hashlib.sha256(self.evidence_file.read_bytes()).hexdigest(),
            "captured_at": "2026-09-21T13:00:00+08:00",
            "locator": "fixture.txt",
            "scope": "temporary fixture",
            "sensitivity": "sanitized-log",
            "collector": "unittest",
        }
        value.update(changes)
        return value

    def make_report(self, **changes):
        value = {
            "id": "report-1",
            "claim": "validator accepts the valid bundle",
            "evidence_ids": ["ev-1"],
            "verification_method": "deterministic unit test",
            "result": "PASS",
            "confidence": 0.95,
            "anomaly_conflict": [],
            "reviewer": "test-worker",
            "model_reported": "local-test",
            "harness": "unittest",
            "observed_at": "2026-09-21T13:00:00+08:00",
        }
        value.update(changes)
        return value

    def valid_bundle(self, **report_changes):
        return {
            "task_id": self.packet["task_id"],
            "records": [{"id": "inventory-1", "kind": "project", "evidence_ids": ["ev-1"]}],
            "evidence": [self.evidence],
            "reports": [self.make_report(**report_changes)],
        }

    def with_mock_inventory_schema(self, bundle):
        def dispatch(kind, value):
            if kind == "project":
                return None  # P3 project schema is absent; inventory shape is mocked only.
            return REAL_SCHEMA_CHECK(kind, value)

        return mock.patch.object(contracts, "schema_check", side_effect=dispatch)

    def test_valid_packet_and_bundle(self):
        self.assertEqual(contracts.packet_check(self.packet), self.root)
        with self.with_mock_inventory_schema(self.valid_bundle()):
            result = contracts.bundle_check(self.valid_bundle(), self.packet)
        self.assertEqual(result["result"], "PASS")

    def test_packet_root_identity_mismatch_is_rejected(self):
        bad = self.make_packet(project_id="other-project")
        with self.assertRaisesRegex(ValueError, "project_id"):
            contracts.packet_check(bad)

    def test_write_path_escape_is_rejected(self):
        bad = self.make_packet(write_paths=[str(self.root.parent / "escape.json")])
        with self.assertRaisesRegex(ValueError, "outside canonical project"):
            contracts.packet_check(bad)

    def test_evidence_hash_mismatch_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "integrity conflict"):
            contracts.evidence_check(self.make_evidence(sha256="0" * 64), [str(self.evidence_dir)])

    def test_evidence_outside_approved_root_and_resolved_traversal_are_rejected(self):
        outside = self.root / "outside.txt"
        outside.write_text("outside", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "outside approved roots"):
            contracts.evidence_check(self.make_evidence(path=str(outside)), [str(self.evidence_dir)])
        traversal = self.evidence_dir / ".." / "outside.txt"
        with self.assertRaisesRegex(ValueError, "outside approved roots"):
            contracts.evidence_check(self.make_evidence(path=str(traversal)), [str(self.evidence_dir)])

    def test_malformed_report_is_rejected_by_real_schema(self):
        malformed = self.make_report()
        malformed.pop("reviewer")
        with self.assertRaises(ValueError):
            contracts.schema_check("verification", malformed)

    def test_missing_evidence_reference_is_rejected(self):
        bundle = self.valid_bundle()
        bundle["reports"][0]["evidence_ids"] = ["missing"]
        with self.with_mock_inventory_schema(bundle):
            with self.assertRaisesRegex(ValueError, "Unresolved report evidence"):
                contracts.bundle_check(bundle, self.packet)

    def test_fail_uncertain_low_confidence_and_unresolved_anomaly_are_blocked(self):
        cases = [
            {"result": "FAIL"},
            {"result": "UNCERTAIN"},
            {"confidence": 0.79},
            {"anomaly_conflict": ["open conflict"]},
        ]
        for changes in cases:
            with self.subTest(changes=changes):
                bundle = self.valid_bundle(**changes)
                with self.with_mock_inventory_schema(bundle):
                    with self.assertRaisesRegex(ValueError, "Integration held"):
                        contracts.bundle_check(bundle, self.packet)

    def test_evidence_count_over_budget_is_rejected(self):
        second = self.evidence_dir / "second.txt"
        second.write_text("second evidence\n", encoding="utf-8")
        bundle = self.valid_bundle()
        bundle["evidence"].append(self.make_evidence(
            id="ev-2", path=str(second), sha256=hashlib.sha256(second.read_bytes()).hexdigest()
        ))
        bundle["reports"][0]["evidence_ids"] = ["ev-1", "ev-2"]
        with self.with_mock_inventory_schema(bundle):
            with self.assertRaisesRegex(ValueError, "budget"):
                contracts.bundle_check(bundle, self.make_packet(
                    budget={"max_files": 1, "max_depth": 2, "max_model_calls": 0}
                ))

    def test_record_evidence_must_be_covered_by_report(self):
        second = self.evidence_dir / "second.txt"
        second.write_text("second evidence\n", encoding="utf-8")
        bundle = self.valid_bundle()
        bundle["evidence"].append(self.make_evidence(
            id="ev-2", path=str(second), sha256=hashlib.sha256(second.read_bytes()).hexdigest()
        ))
        bundle["records"][0]["evidence_ids"] = ["ev-2"]
        with self.with_mock_inventory_schema(bundle):
            with self.assertRaisesRegex(ValueError, "covered"):
                contracts.bundle_check(bundle, self.packet)


if __name__ == "__main__":
    unittest.main(verbosity=2)
