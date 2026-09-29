"""Build a clean, allowlisted public-release tree without deleting an output."""

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path, PurePosixPath

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "release" / "public-release-manifest.json"
SCHEMA = ROOT / "schemas" / "public-release-manifest.schema.json"
PRIVATE_SOURCE_PREFIXES = ("artifacts/", "evidence/", "checkpoints/", "incidents/", "packets/")
SECRET_PATTERN = re.compile(
    rb"(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)"
)
# A Windows drive prefix must begin at a token boundary. Without the negative
# look-behind, the trailing ``s:/`` in ``https://`` is falsely classified as a
# local absolute path.
ABSOLUTE_PATH_PATTERN = re.compile(rb"(?:(?<![A-Za-z0-9+.-])[A-Za-z]:[\\/]|/Users/|/home/)")


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def relative_path(raw, label):
    path = PurePosixPath(raw.replace("\\", "/"))
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"Unsafe {label} path: {raw}")
    return path


def validate_manifest(value):
    schema = read_json(SCHEMA)
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(value), key=lambda error: str(list(error.path)))
    if errors:
        raise ValueError("; ".join(f"{list(error.path)}: {error.message}" for error in errors))

    targets = set()
    for entry in value["files"]:
        source = relative_path(entry["source"], "source")
        target = relative_path(entry["target"], "target")
        normalized_source = source.as_posix()
        if normalized_source.startswith(PRIVATE_SOURCE_PREFIXES):
            raise ValueError(f"Private/internal source is not exportable: {normalized_source}")
        if target.as_posix() in targets:
            raise ValueError(f"Duplicate release target: {target.as_posix()}")
        targets.add(target.as_posix())
        resolved = (ROOT / Path(*source.parts)).resolve()
        if not resolved.is_relative_to(ROOT) or not resolved.is_file():
            raise ValueError(f"Missing or escaped release source: {normalized_source}")

    if (value["license_spdx"] is None) != (value["license_source"] is None):
        raise ValueError("license_spdx and license_source must be set together")
    if value["license_source"] is not None:
        source = relative_path(value["license_source"], "license source")
        if not (ROOT / Path(*source.parts)).is_file():
            raise ValueError("Configured license source does not exist")
        if "LICENSE" not in targets:
            raise ValueError("A final license must be exported to LICENSE")
    return value


def inspect_sources(value):
    findings = []
    forbidden = [term.casefold().encode("utf-8") for term in value["forbidden_terms"]]
    for entry in value["files"]:
        source = relative_path(entry["source"], "source")
        path = ROOT / Path(*source.parts)
        data = path.read_bytes()
        folded = data.lower()
        if SECRET_PATTERN.search(data):
            findings.append(f"secret-pattern:{source.as_posix()}")
        if ABSOLUTE_PATH_PATTERN.search(data):
            findings.append(f"absolute-path:{source.as_posix()}")
        for term in forbidden:
            if term in folded:
                findings.append(f"forbidden-term:{source.as_posix()}")
                break
    if findings:
        raise ValueError("Release source inspection failed: " + ", ".join(findings))
    return value


def status(value):
    blockers = []
    if value["license_spdx"] is None:
        blockers.append("license_not_selected")
    return {
        "result": "RELEASE_READY" if not blockers else "DRAFT_READY",
        "release_name": value["release_name"],
        "version": value["version"],
        "files": len(value["files"]),
        "blockers": blockers,
    }


def build(value, output, draft=False):
    current = status(value)
    if current["blockers"] and not draft:
        raise ValueError("Final build held: " + ", ".join(current["blockers"]))
    output = Path(output).resolve()
    if output.exists() and any(output.iterdir()):
        raise ValueError("Output directory must be absent or empty; existing content is never cleared")
    output.mkdir(parents=True, exist_ok=True)

    records = []
    for entry in value["files"]:
        source = relative_path(entry["source"], "source")
        target = relative_path(entry["target"], "target")
        source_path = ROOT / Path(*source.parts)
        target_path = output / Path(*target.parts)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, target_path)
        data = target_path.read_bytes()
        records.append({"path": target.as_posix(), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})

    if draft:
        marker = output / "DRAFT-NOT-FOR-PUBLICATION.md"
        marker.write_text(
            "# Draft release\n\nThis export has passed the allowlist and privacy checks, but no project license has been selected. Do not publish it as a final release.\n",
            encoding="utf-8",
        )
        data = marker.read_bytes()
        records.append({"path": marker.name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})

    release_record = {
        "release_name": value["release_name"],
        "version": value["version"],
        "license_spdx": value["license_spdx"],
        "draft": draft,
        "files": sorted(records, key=lambda item: item["path"]),
        "digest_scope": "Exact bytes of this exported tree only; not semantic correctness, provenance or publication authorization."
    }
    (output / "RELEASE-MANIFEST.json").write_text(
        json.dumps(release_record, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    return {**current, "output": str(output), "draft": draft, "exported_files": len(records)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["check", "build"])
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--output")
    parser.add_argument("--draft", action="store_true")
    args = parser.parse_args()

    value = inspect_sources(validate_manifest(read_json(args.manifest)))
    if args.command == "check":
        result = status(value)
    else:
        if not args.output:
            parser.error("--output required for build")
        result = build(value, args.output, draft=args.draft)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"result": "FAIL", "error": str(exc)}, ensure_ascii=False))
        sys.exit(1)
