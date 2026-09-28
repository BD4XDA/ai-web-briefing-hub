import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools import model_routing  # noqa: E402


class ModelRoutingTests(unittest.TestCase):
    def setUp(self):
        self.value = json.loads((ROOT / "config" / "model-routing.json").read_text(encoding="utf-8"))

    def test_current_manifest_validates(self):
        self.assertIs(model_routing.validate(self.value), self.value)

    def test_default_effort_must_be_allowed(self):
        bad = copy.deepcopy(self.value)
        bad["routes"][0]["default_effort"] = "high"
        with self.assertRaisesRegex(ValueError, "Default effort"):
            model_routing.validate(bad)

    def test_duplicate_role_is_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["routes"][1]["role"] = bad["routes"][0]["role"]
        with self.assertRaisesRegex(ValueError, "unique"):
            model_routing.validate(bad)

    def test_deepseek_boundary_is_fixed(self):
        bad = copy.deepcopy(self.value)
        bad["runtime_policy"]["deepseek_policy"] = "managed_here"
        with self.assertRaises(ValueError):
            model_routing.validate(bad)


if __name__ == "__main__":
    unittest.main(verbosity=2)
