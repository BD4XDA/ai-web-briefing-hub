import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools import capability_registry  # noqa: E402


class CapabilityRegistryTests(unittest.TestCase):
    def setUp(self):
        self.value = json.loads((ROOT / "config" / "capability-registry.json").read_text(encoding="utf-8"))

    def test_current_registry_validates(self):
        self.assertIs(capability_registry.validate(self.value), self.value)

    def test_duplicate_id_is_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["capabilities"][1]["id"] = bad["capabilities"][0]["id"]
        with self.assertRaisesRegex(ValueError, "unique"):
            capability_registry.validate(bad)

    def test_live_capability_requires_verification_time(self):
        bad = copy.deepcopy(self.value)
        bad["capabilities"][0]["last_verified"] = None
        with self.assertRaisesRegex(ValueError, "last_verified"):
            capability_registry.validate(bad)

    def test_automatic_upgrade_is_forbidden(self):
        bad = copy.deepcopy(self.value)
        bad["policy"]["automatic_upgrade"] = True
        with self.assertRaises(ValueError):
            capability_registry.validate(bad)


if __name__ == "__main__":
    unittest.main(verbosity=2)
