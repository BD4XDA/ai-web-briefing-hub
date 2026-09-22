# SOL-AGENT checkpoint mirror verification

Date: 2026-09-22

Claim: a Foundation checkpoint cannot advance `checkpoints/LATEST.json` unless the generated latest-checkpoint section in `SOL-AGENT.md` is written successfully.

Verification method: `python -m unittest discover -s tests -v` from the canonical Lab Research OS root.

Result: PASS. All 20 tests passed. The added cases verify normal mirror creation while preserving manual adapter content, rejection when `SOL-AGENT.md` is missing, and preservation of the prior committed `LATEST.json` when the Sol mirror replace operation fails.

Limitations: these are local deterministic tests of Foundation commit behavior. They do not authenticate an external Sol runtime or replace the immutable checkpoint snapshot and `LATEST.json` as canonical state.
