import argparse
import tempfile
import unittest
from pathlib import Path

from tools import cost_telemetry


class CostTelemetryTests(unittest.TestCase):
    def args(self, **changes):
        values = {
            "workload": "smoke",
            "trigger": "EVENT",
            "outcome": "PASS",
            "model_routes": "local",
            "reasoning_effort": "not-applicable",
            "input_tokens": None,
            "output_tokens": None,
            "total_tokens": None,
            "token_source": "unavailable",
            "estimate_method": None,
            "model_calls": 0,
            "tool_calls": 1,
            "failed_attempts": 0,
            "stop_rule": False,
            "high_reasoning_calls": 0,
            "benefit": 4,
            "cost": 2,
            "useful_output": "one bounded check",
            "cheaper_route": "none",
            "notes": "",
        }
        values.update(changes)
        return argparse.Namespace(**values)

    def test_record_round_trip_and_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.jsonl"
            record = cost_telemetry.make_record(self.args())
            cost_telemetry.append_record(path, record)
            summary = cost_telemetry.summarize(cost_telemetry.load_records(path))
            self.assertEqual(summary["records"], 1)
            self.assertEqual(summary["token_unavailable_records"], 1)
            self.assertEqual(summary["average_evr"], 2.0)

    def test_estimate_requires_method(self):
        with self.assertRaisesRegex(ValueError, "estimate-method"):
            cost_telemetry.make_record(self.args(token_source="estimated", total_tokens=100))

    def test_unavailable_rejects_false_precision(self):
        with self.assertRaisesRegex(ValueError, "cannot carry"):
            cost_telemetry.make_record(self.args(total_tokens=100))


if __name__ == "__main__":
    unittest.main(verbosity=2)
