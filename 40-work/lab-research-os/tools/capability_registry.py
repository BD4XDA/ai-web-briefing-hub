"""Validate and summarize the need-driven capability registry."""

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "capability-registry.json"
SCHEMA = ROOT / "schemas" / "capability-registry.schema.json"


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def validate(value):
    schema = read_json(SCHEMA)
    Draft202012Validator.check_schema(schema)
    errors = sorted(
        Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER).iter_errors(value),
        key=lambda error: str(list(error.path)),
    )
    if errors:
        raise ValueError("; ".join(f"{list(error.path)}: {error.message}" for error in errors))

    ids = [item["id"] for item in value["capabilities"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Capability ids must be unique")
    if any(item["tier"] == "core" and item["update_policy"] == "no-update" for item in value["capabilities"]):
        raise ValueError("Core capabilities cannot opt out of update review")
    if any(item["availability"] == "live" and item["last_verified"] is None for item in value["capabilities"]):
        raise ValueError("Live capabilities require last_verified")
    return value


def summary(value):
    result = {"result": "PASS", "registry_version": value["registry_version"], "total": len(value["capabilities"])}
    for field in ("tier", "availability", "qualification"):
        counts = {}
        for item in value["capabilities"]:
            key = item[field]
            counts[key] = counts.get(key, 0) + 1
        result[f"by_{field}"] = counts
    result["blocked"] = [item["id"] for item in value["capabilities"] if item["qualification"] == "blocked"]
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["validate", "show"])
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    args = parser.parse_args()
    value = validate(read_json(args.config))
    print(json.dumps({"result": "PASS", "registry_version": value["registry_version"]} if args.command == "validate" else summary(value), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"result": "FAIL", "error": str(exc)}, ensure_ascii=False))
        sys.exit(1)
