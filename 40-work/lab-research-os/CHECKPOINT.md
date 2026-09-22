# Lab Research OS · CHECKPOINT
Checkpoint ID: 20260922T155833-7fcdcab38f00
Priority: EXIT · Status: complete
Canonical committed pointer: checkpoints/LATEST.json. If IDs differ, use tools/foundation.py show; do not guess.

## Current Verified State

- Human PI instruction is active: agents do not calculate or recheck hashes by default.
- Direct inspection, Git status/diff, schema validation, targeted tests and source provenance are the preferred verification methods for ordinary local work.
- Digests remain justified only for explicit byte-identity claims, meaningful boundary crossings, immutable manifest/checkpoint contracts, or concrete tampering/staleness questions.
- Historical evidence contracts and the Foundation checkpoint integrity mechanism are unchanged; AT08 gate state and preliminary AT09 scope are unchanged.

## Completed

- Added evidence-proportionality rules to the shared and scoped AGENTS.md files.
- Updated the verification and handoff protocols to remove universal hash requirements for new work.
- Updated the Sol adapter so it cannot request hashes reflexively or overclaim what digest equality proves.
- Recorded Decision 0005 and a hub-level decision pointer without rewriting historical packets.

## Decisions

- Default to no new digest unless one of the four declared justifications applies.
- Do not repeat an accepted digest when inputs and the protected boundary are unchanged and no named contradiction exists.
- Hash equality is byte binding only; it does not prove provenance, completeness, semantic truth, safety or authorization.

## Open Questions


## Known Risks

- Historical artifacts still contain their original digest requirements and must not be mistaken for the new default.
- Preliminary untracked AT09 artifacts remain outside this policy-only change and are not promoted or accepted.

## In Progress


## Next Actions

- Apply evidence proportionality to all newly scoped tasks and reviews.
- Do not rerun accepted checks or recalculate digests solely for reassurance.

## Evidence References

- decisions/0005-evidence-proportionality.md
- AGENTS.md
- SOL-AGENT.md
- protocols/VERIFICATION.md
- protocols/HANDOFF.md
- ../../AGENTS.md
- ../../50-decisions/2026-09-22-evidence-proportionality.md
