"""Append and summarize privacy-minimal run-level cost telemetry."""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = ROOT / "artifacts" / "telemetry" / "run-cost.jsonl"
TOKEN_SOURCES = {"provider-reported", "harness-reported", "estimated", "unavailable"}


def nonnegative(value, label):
    if value is not None and value < 0:
        raise ValueError(f"{label} must be nonnegative")
    return value


def make_record(args):
    if args.token_source not in TOKEN_SOURCES:
        raise ValueError("invalid token source")
    if args.token_source == "estimated" and not args.estimate_method:
        raise ValueError("estimated tokens require --estimate-method")
    if args.token_source == "unavailable" and any(
        value is not None for value in (args.input_tokens, args.output_tokens, args.total_tokens)
    ):
        raise ValueError("unavailable token source cannot carry token counts")
    for label in (
        "input_tokens", "output_tokens", "total_tokens", "model_calls", "tool_calls",
        "failed_attempts", "high_reasoning_calls",
    ):
        nonnegative(getattr(args, label), label)
    if not 0 <= args.benefit <= 8:
        raise ValueError("benefit must be between 0 and 8")
    if not 1 <= args.cost <= 5:
        raise ValueError("cost must be between 1 and 5")
    total = args.total_tokens
    if total is None and args.input_tokens is not None and args.output_tokens is not None:
        total = args.input_tokens + args.output_tokens
    return {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "workload": args.workload,
        "trigger": args.trigger,
        "outcome": args.outcome,
        "model_routes": args.model_routes,
        "reasoning_effort": args.reasoning_effort,
        "tokens": {
            "input": args.input_tokens,
            "output": args.output_tokens,
            "total": total,
            "source": args.token_source,
            "estimate_method": args.estimate_method,
        },
        "model_calls": args.model_calls,
        "tool_calls": args.tool_calls,
        "failed_attempts": args.failed_attempts,
        "stop_rule_fired": args.stop_rule,
        "high_reasoning_calls": args.high_reasoning_calls,
        "benefit": args.benefit,
        "cost": args.cost,
        "evr": round(args.benefit / args.cost, 3),
        "useful_output": args.useful_output,
        "cheaper_route": args.cheaper_route,
        "notes": args.notes,
    }


def append_record(path, record):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.parent / ".run-cost.lock"
    deadline = time.monotonic() + 5
    descriptor = None
    while descriptor is None:
        try:
            descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise ValueError("cost telemetry writer lock is busy")
            time.sleep(0.05)
    try:
        os.write(descriptor, str(os.getpid()).encode("ascii"))
        os.close(descriptor)
        descriptor = None
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
    finally:
        if descriptor is not None:
            os.close(descriptor)
        lock.unlink(missing_ok=True)


def load_records(path, date=None):
    path = Path(path)
    if not path.is_file():
        return []
    records = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL record at line {number}: {exc}") from exc
        if date and not record.get("recorded_at", "").startswith(date):
            continue
        records.append(record)
    return records


def summarize(records):
    known = [record for record in records if record["tokens"]["source"] != "unavailable"]
    return {
        "records": len(records),
        "token_known_records": len(known),
        "token_unavailable_records": len(records) - len(known),
        "input_tokens_known": sum(record["tokens"].get("input") or 0 for record in known),
        "output_tokens_known": sum(record["tokens"].get("output") or 0 for record in known),
        "total_tokens_known": sum(record["tokens"].get("total") or 0 for record in known),
        "model_calls": sum(record.get("model_calls", 0) for record in records),
        "tool_calls": sum(record.get("tool_calls", 0) for record in records),
        "failed_attempts": sum(record.get("failed_attempts", 0) for record in records),
        "stop_rule_events": sum(bool(record.get("stop_rule_fired")) for record in records),
        "high_reasoning_calls": sum(record.get("high_reasoning_calls", 0) for record in records),
        "average_evr": round(sum(record.get("evr", 0) for record in records) / len(records), 3)
        if records else None,
        "routes": sorted({record.get("model_routes", "") for record in records if record.get("model_routes")}),
    }


def parser():
    root = argparse.ArgumentParser()
    root.add_argument("--ledger", default=str(DEFAULT_LEDGER))
    commands = root.add_subparsers(dest="command", required=True)
    record = commands.add_parser("record")
    record.add_argument("--workload", required=True)
    record.add_argument("--trigger", required=True)
    record.add_argument("--outcome", required=True)
    record.add_argument("--model-routes", required=True)
    record.add_argument("--reasoning-effort", default="not-applicable")
    record.add_argument("--input-tokens", type=int)
    record.add_argument("--output-tokens", type=int)
    record.add_argument("--total-tokens", type=int)
    record.add_argument("--token-source", required=True, choices=sorted(TOKEN_SOURCES))
    record.add_argument("--estimate-method")
    record.add_argument("--model-calls", type=int, default=0)
    record.add_argument("--tool-calls", type=int, default=0)
    record.add_argument("--failed-attempts", type=int, default=0)
    record.add_argument("--stop-rule", action="store_true")
    record.add_argument("--high-reasoning-calls", type=int, default=0)
    record.add_argument("--benefit", type=int, required=True)
    record.add_argument("--cost", type=int, required=True)
    record.add_argument("--useful-output", required=True)
    record.add_argument("--cheaper-route", default="none")
    record.add_argument("--notes", default="")
    show = commands.add_parser("show")
    show.add_argument("--date")
    return root


def main():
    args = parser().parse_args()
    if args.command == "record":
        record = make_record(args)
        append_record(args.ledger, record)
        result = {"result": "RECORDED", "workload": record["workload"], "evr": record["evr"]}
    else:
        result = summarize(load_records(args.ledger, args.date))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({"result": "FAIL", "error": str(exc)}, ensure_ascii=False))
        sys.exit(1)
