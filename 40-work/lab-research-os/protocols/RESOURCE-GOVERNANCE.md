# Resource governance and bounded retries

## Purpose

Spend reasoning, tool time and Human PI attention where they change scientific or operational outcomes. A failed action is not a reason to escalate the model or retry indefinitely.

## Failure budget

- The default budget is **three total attempts** for one logical target, desired outcome and failure class. Equivalent URLs, wrappers, browsers or download methods still count toward the same budget when they seek the same artifact and encounter the same underlying failure.
- Stop before the third attempt when direct evidence shows that another attempt cannot change the outcome. A fallback that changes the source, artifact or method materially is a new target, but the switch and prior failures remain in the run record.
- At the budget limit, preserve completed work and failure evidence, then replace the candidate, use a qualified fallback, or checkpoint the smallest continuation point. Do not buy another attempt by raising reasoning effort or model prestige.
- The limit applies across research, infrastructure, Skill/MCP, harness, connector, rendering, automation and release work. It is a maximum, not a requirement to retry.

## Lightweight cost-benefit check

Calculate this only after a failure when deciding whether to retry; successful and deterministic routine work needs no scorecard.

- Benefit `B` = scientific value (0–3) + direct Human PI/project relevance (0–3) + irreplaceability (0–2).
- Cost `C` = expected time/tool/model cost (1–3) + observed repeat-failure penalty (0–2).
- Expected value ratio `EVR = B / C`.

An ordinary retry requires a plausible path to a different outcome, `B >= 3`, and `EVR >= 1`. Prefer a lawful substitute when its expected value is equal or better. Record only the compact result (`B`, `C`, `EVR`, attempt count and disposition) when a retry or stop decision is material.

## Exceptional scientific extension

One additional bounded tranche of at most three attempts is allowed only when all of the following hold:

1. `B >= 7`;
2. the item is a major scientific finding or directly important to the Human PI's active research;
3. no scientifically equivalent lawful substitute is available;
4. the run record states the scientific value, irreplaceability, cost already spent, new method that could change the result, and the finite extension budget.

After that extension, stop and escalate only the consequential decision to the Human PI. Never continue an open-ended retry loop.

## Verification economy

Run one proportional verification pass after a changed input or real event. A failure may receive the smallest discriminating check within the same attempt budget. Do not rerun accepted checks, verify the verifier, or manufacture work merely to produce a PASS.
