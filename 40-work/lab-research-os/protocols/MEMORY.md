# Memory and instruction architecture

The canonical root is found by `.lab-project.json`; the Git root remains the ancestor `ai-web-briefing-hub`. These two roots serve different purposes. No new repository or harness was created.

| Layer | Owner | Read behavior | Write / promotion behavior |
|---|---|---|---|
| AGENTS.md | Architecture owner under PI authorization | On project entry | Stable procedure only; evidence-backed decision required |
| PROJECT.md | PI scope, architecture maintainer | On entry / scope change | Identity, authorized scope and constraints; no transient logs |
| checkpoints/LATEST.json + immutable snapshots | Current task owner, exclusive writer | `foundation.py show` verifies integrity | Compare-and-swap expected parent; CHECKPOINT.md and the generated section in SOL-AGENT.md are required readable projections |
| decisions/ | Decision owner | Only relevant decisions | Append new decision or supersede; preserve rationale |
| knowledge/ | Subject owner + verifier | Only relevant validated claims | Promote scoped fact from evidence + verification; retain uncertainty/recheck trigger |
| evidence/ | Collector | Read exact referenced record | Immutable observation with source locator, hash and time; reports alone are insufficient |
| incidents/ | Task/service owner | When failure discriminates current issue | Episode, hypotheses, attempts, correction and next check; not a global rule |
| artifacts/ | Assigned worker | Per packet | Draft/reviewed/integrated states explicit |
| IDEA-INBOX | Any agent may capture | During planning only | CAPTURE does not authorize execution |

## Harness adapters and discovery
Codex uses project AGENTS.md and an explicit task-root/read packet. Claude's local help verifies CLAUDE.md discovery; this project's adapter instructs an explicit read of AGENTS.md. Native @import was not verified and is not required. Claude `--safe-mode` intentionally skips native customizations, so its caller must supply the entire approved bounded packet and enforce permissions outside the model.

Installed DSH `dsh-agent-instructions` discovers AGENTS.md, CLAUDE.md and their local variants by walking `.git` root → cwd. Launch at this canonical root or explicitly specify/read it. DEEPSEEK.md remains a legacy handoff pointer; its automatic discovery is not assumed. Both thin adapters may be read by DSH, but only AGENTS.md defines the rule set.

Global instructions, harness sessions and auto-memory are preserved. They do not automatically become project truth, nor can project rules overrule runtime constraints or current user instructions. Config inspection is not a live prompt-injection test; the native-loader audit records the exact verification boundary.

## Conflict and crash behavior
Classify intent conflicts separately from fact conflicts. An actual configuration/log contradicting a checkpoint invalidates that checkpoint claim at that timestamp; it does not authorize configuration replacement. Collect a minimal discriminating observation, update incident/evidence, then advance the checkpoint.

Checkpoint snapshots are never replaced. LATEST is the commit point. A crash before updating LATEST leaves the prior snapshot authoritative, even if CHECKPOINT.md or the generated SOL-AGENT.md section was already rendered. `foundation.py show` reconstructs from the committed snapshot and validates its hash. Both readable projections must carry the committed ID after a successful checkpoint. An orphan snapshot can be inspected; do not delete it automatically. A stale writer reloads and reconciles, never force-writes.

## Promotion gates
Episode → knowledge requires a claim, scope, primary evidence, independent verification, owner acceptance and recheck trigger. Knowledge → stable rule additionally requires a demonstrated recurrent procedural need and conflict check with existing rules. Low confidence remains an open question; repetition or model consensus alone is not evidence.
