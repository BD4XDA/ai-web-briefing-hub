# Decision 0004 · SOL-AGENT checkpoint mirror is mandatory

Status: approved by direct Human PI instruction, 2026-09-22.

Every completed work checkpoint must be written into `SOL-AGENT.md`. The project enforces this as a Foundation commit requirement: `tools/foundation.py checkpoint` renders the ordinary `CHECKPOINT.md` projection and the generated latest-checkpoint section in `SOL-AGENT.md` before advancing `checkpoints/LATEST.json`.

`checkpoints/LATEST.json` and its immutable hashed snapshot remain authoritative. The Sol section is a required fast-resume mirror, not an independent source of truth. Manual edits to that generated section do not commit state. Missing `SOL-AGENT.md`, malformed generated markers, or a failed mirror write prevents the checkpoint from committing.

This instruction supersedes the earlier procedure only where it said the Sol adapter must not carry checkpoint state. Stable Sol guidance remains manually maintained outside the generated marker block.
