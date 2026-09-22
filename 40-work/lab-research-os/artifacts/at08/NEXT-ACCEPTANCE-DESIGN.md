# AT08 next-gate decision — no execution or review scheduled

**Recommendation: C. EVIDENCE-ONLY IMPROVEMENT JUSTIFIED.**
Available evidence does not demonstrate a new local F5/F6 implementation defect requiring revision. Correct the evidence/claim boundary before deciding whether code needs to change. This is not acceptance and not a prediction of a higher reviewer score.

AT07 PASS0.72 with nonempty anomaly list remains a correctly blocked acceptance. F5/F6 remain DISABLED_NOT_ACCEPTED. No original anomaly is removed and no confidence score is recalculated.

## Why evidence first
Unknown events already produce writeback_allowed=false. Oversized/invalid-encoding streams already deny completeness. The scope document already states no-anomaly. These do not justify changes merely to obtain a different review. Limited secret screening and trusted capture require an explicit bounded input/producer contract; arbitrary logs, fabricated flags or unbound scope=True are not qualified. No actual leak, forged capture or incorrect live scope was established by the supplied historical evidence.

Mandatory evidence prerequisites (potential false-acceptance paths if ignored):
- Bind permitted telemetry/data classes and withheld/unknown-safety handling to the actual future producer. Completeness is not a universal secret-free assertion.
- Bind capture state/receipt to the actual process/request/EOF rather than trusting unlocated declarations.
- Bind action-scope inputs to deterministic path facts and the observed policy decision; a caller's True is not policy evidence.
- Obtain the F4 decision-path observation contract in F4-OBSERVABILITY-DESIGN.md. Historical evidence is NOT CURRENTLY RECOVERABLE.

If these checks later expose contradictory capture/scope or unsafe transmission, pause and propose an evidenced minimal local revision. Do not silently modify code while preparing a review package.

## Next bounded acceptance package — design only
1. **Claim manifest**: exact local F5/F6 claim and allowed input/caller assumptions, exclusions, implementation/test hashes, and unchanged acceptance criteria. Separate byte identity, capture completeness, transmission safety, action scope and policy authorization.
2. **Anomaly disposition**: original AT07 response unmodified plus ANOMALY-ADJUDICATION.json, with every original quote. Supply exact code/stream/source references for each disposition; do not erase concerns or ask a reviewer to rubber-stamp this adjudication.
3. **Existing regression evidence**: reuse the unchanged 9-group/45-assertion capture, test source and raw output already bound to code. No rerun solely for reassurance. Synthetic fixtures remain explicitly labeled.
4. **Targeted additional evidence, only if separately authorized**: producer capability/decision boundary record; actual capture lifecycle and source/data-class contract; one scoped check that scope flags derive from actual action/path/policy evidence. Do not claim these exist now.
5. **Required negative conditions**: unknown or missing policy event; mismatched request/session/source hash; missing EOF versus legitimately empty; withheld/unknown-safety source; scope unknown/conflicting; unexpected real action; missing observation; malformed/incomplete/low-confidence/tool-using review; stale checkpoint/unequal writeback. Reuse existing matching controls. Run new deterministic cases only for newly introduced capture/projection responsibilities; never execute destructive examples. Any failure remains unaccepted.
6. **Raw bindings**: provide the bodies the tool-less reviewer needs, not hash-only links. Each stream has source identity, byte count/hash, encoding, capture/truncation/safety status and projection references. Missing/oversized/withheld stays explicitly incomplete. Include the F4 request→policy→decision→execution relation, not an inferred explanation.
7. **Package completeness before review**: verify all prerequisites, exact bodies, code/evidence bindings, explicit limitations and safe transmission. If any prerequisite is missing, do not schedule/send another review.
8. **Unchanged review gate**: one separately authorized independent evidence review only after blockers are addressed; PASS, confidence>=0.80, completed, zero tool calls, no unresolved consequential anomaly; preserve the current conservative nonempty-anomaly blocking behavior. No threshold change, no repeated review until PASS, no automatic exception promotion.

## Successor gate
**NOT READY.**
Reasons: F4 observability not implemented/established; repairs unaccepted; no actual caller/capture integration evidence; AT07 acceptance remains FAIL. Local tests do not remove these prerequisites.

A future successor needs its own predeclared packet and separate authorization after all prior gates are met. This document is NOT an executable successor packet. No worker/model run, adoption, policy edit, Foundation change or review is scheduled.

## Exact next action
Seek a separately bounded authorization for **read-only capability assessment of the producer-side policy/capture observation points**, with required non-secret fields listed in F4-OBSERVABILITY-DESIGN.md; do not rerun known-empty history queries. Then produce the input/capture/scope evidence contract needed above. If capability is absent, return a recorder-only proposal, not a changed policy or launched successor. Keep disabled repairs and C1/C2/P5/P6 unchanged.

