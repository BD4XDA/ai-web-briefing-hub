"""Validate and display the project-owned model-routing manifest."""

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "model-routing.json"
SCHEMA = ROOT / "schemas" / "model-routing.schema.json"


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

    routes = value["routes"]
    roles = [route["role"] for route in routes]
    if len(roles) != len(set(roles)):
        raise ValueError("Route roles must be unique")

    route_by_role = {route["role"]: route for route in routes}
    for route in routes:
        allowed = set(route["allowed_efforts"])
        if route["default_effort"] not in allowed:
            raise ValueError(f"Default effort is not allowed for {route['role']}")
        if set(route["effort_rules"]) != allowed:
            raise ValueError(f"Effort rules must exactly cover allowed efforts for {route['role']}")
        target = route["escalate_to"]
        if target is not None and target not in route_by_role:
            raise ValueError(f"Unknown escalation target for {route['role']}: {target}")

    if "none" in route_by_role.get("astra", {}).get("allowed_efforts", []):
        raise ValueError("Astra cannot use none reasoning effort")
    sol = route_by_role.get("sol", {})
    if sol.get("model") == "gpt-6.1-sol" and "none" in sol.get("allowed_efforts", []):
        raise ValueError("GPT-6.1 Sol cannot use none reasoning effort")
    if value["runtime_policy"]["deepseek_policy"] != "external_unchanged":
        raise ValueError("DeepSeek policy must remain external_unchanged in this manifest")
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["validate", "show"])
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    args = parser.parse_args()

    value = validate(read_json(args.config))
    if args.command == "validate":
        result = {"result": "PASS", "policy_version": value["policy_version"], "routes": len(value["routes"])}
    else:
        result = {
            "policy_version": value["policy_version"],
            "routes": [
                {"role": route["role"], "model": route["model"], "default_effort": route["default_effort"]}
                for route in value["routes"]
            ],
            "deepseek_policy": value["runtime_policy"]["deepseek_policy"],
        }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"result": "FAIL", "error": str(exc)}, ensure_ascii=False))
        sys.exit(1)
