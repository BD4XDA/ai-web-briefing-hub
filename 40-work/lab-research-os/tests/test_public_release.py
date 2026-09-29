import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools import public_release  # noqa: E402


class PublicReleaseTests(unittest.TestCase):
    def setUp(self):
        self.value = json.loads((ROOT / "release" / "public-release-manifest.json").read_text(encoding="utf-8"))

    def test_current_manifest_is_clean_draft(self):
        public_release.inspect_sources(public_release.validate_manifest(self.value))
        self.assertEqual(public_release.status(self.value)["blockers"], ["license_not_selected"])

    def test_final_build_is_held_without_license(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "license_not_selected"):
                public_release.build(self.value, Path(directory) / "release")

    def test_draft_build_contains_only_allowlisted_files_and_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "release"
            result = public_release.build(self.value, output, draft=True)
            self.assertTrue(result["draft"])
            self.assertTrue((output / "DRAFT-NOT-FOR-PUBLICATION.md").is_file())
            receipt = json.loads((output / "RELEASE-MANIFEST.json").read_text(encoding="utf-8"))
            self.assertEqual(len(receipt["files"]), len(self.value["files"]) + 1)
            exported = {item["path"] for item in receipt["files"]}
            self.assertNotIn("artifacts", {Path(path).parts[0] for path in exported})

    def test_path_escape_is_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["files"][0]["source"] = "../secret.txt"
        with self.assertRaisesRegex(ValueError, "Unsafe source"):
            public_release.validate_manifest(bad)

    def test_web_url_is_not_a_windows_drive_path(self):
        self.assertIsNone(public_release.ABSOLUTE_PATH_PATTERN.search(b"https://example.org/research"))
        self.assertIsNotNone(public_release.ABSOLUTE_PATH_PATTERN.search(b'"D:/private/research"'))


if __name__ == "__main__":
    unittest.main(verbosity=2)
