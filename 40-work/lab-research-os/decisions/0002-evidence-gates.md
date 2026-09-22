# 0002 — Bounded handoff and evidence gates

Status: accepted for foundation v1, 2026-09-21. Owner: Astra under ASTRA TIME 01.

Use JSON Schema Draft 2020-12 with the already installed jsonschema 4.26.0; no dependency install or upgrade. Schema loading is local. Contracts check packet identity, bounded local evidence paths, byte hashes, reference resolution and explicit acceptance gates. They do not execute arbitrary commands, infer science, authenticate a model name or sandbox workers.

DeepSeek reviews compact deterministic evidence separately from the executing worker. Owner review is required before integration; a PASS without valid evidence is rejected. Root architecture accepts independent passing tests without routine duplicate runs.

No live scheduler, global router, full Context Compiler or automatic heterogeneous board is implied. L0–L3 is a written decision protocol at this stage. Keep implementation and future architecture visibly separate.

Rollback: cease using new contracts and restore the previous committed checkpoint via a new superseding checkpoint; preserve old snapshots/evidence. No harness defaults were changed.
