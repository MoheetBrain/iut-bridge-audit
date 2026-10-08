# Final bounded triangulation verdict

**Verdict D — ALTERNATIVE_PROOF_DISTINCT_FROM_IUT, at restricted scope. Decision: STOP.**

This verdict records an alternative labelled-norm lower estimate and an unestablished transfer. It does **not** certify Joshi's full alternative proof. Original IUT III Corollary 3.12 is neither independently proved nor refuted by this run. No essential IUT flaw, faithful IUT countermodel or prize relevance is established.

## What changed beyond Stage 14

The focused test had not already been done. Stage 14 inspected the final claimed inequality; this run traced the standard point, Tate data, period-ring lifts, crystalline unit classes, collation, tensor images and hull comparison. It recovered the j-squared sum with the standard **mth-coordinate** reference. It also proved a counterexample to Joshi's universal hull/convex-closure identification and checked two literal index/sign inconsistencies. It did not repeat the 372-family OpenAI screen or earlier localization/Rss/Hom constructions.

The central negative finding is precise: **9.8.1(7)'s identification of Joshi's collated locus with the original multiradial output has not been established with native marking, permitted choices and the original receiving normalization.** The numerical alternative was tested too: even granting his volume estimate as a source input at its own scope, the next inequality `b_J<=b_IUT` and identification `a_J=a_IUT` remain unverified. No impossibility theorem is inferred from that failure.

## Requested outcome fields

| Field | Finding |
|---|---|
| Repository | `MoheetBrain/iut-bridge-audit`; origin `https://github.com/MoheetBrain/iut-bridge-audit.git` |
| Branch | `codex/final-iut-proof-triangulation` |
| Actual starting state | Clean Stage 14 worktree at `09a6ce36ff1f055063fc65992487c39ecbf56987`, local/unpushed at start; verified descendant of original `dadb78da4beb66698b0fae39dac5aafa373e8150`. New isolated worktree `/Users/moheet/Documents/ChatGPT/IUT-final-proof-triangulation`. |
| Exact Joshi theorem tested | Construction III **2401.13508v4**, Theorem 9.11.1 and Corollary 9.11.1.1, pp.127–128; backwards through 9.8.1,9.9,9.10.7–8 and their immediate local/collation dependencies. |
| Match to original objects | Candidate containers and prime-strip objects; no complete theorem-preserving identification of the permitted output and its bounded normalization. |
| Does Xi supply native marking? | The period lift retains its selected quotient value; the separate unit cohomology class encodes q before collation. Native-marked membership or adequate comparison in the original receiving output is **not established**. |
| Does normalized bound transfer? | **No verified transfer.** Restricted norm estimate is recovered. Collated volume normalization and original `b_J<=b_IUT` are unresolved. |
| j-squared factors | Retained. With m=(ell-1)/2 and canonical coordinate m, their normalized average is `(m+1)(2m+1)/(6m^2)`; the raw average is of order m^2. This convention is not a proof of original degree compatibility. |
| First missing original inference | 9.8.1(7): source-permitted native/normalization-preserving comparison after cohomological collation. A weaker numerical comparison would suffice, but was not obtained. |
| Strongest proof/obstruction | Explicit `Q_3(sqrt(3))` tensor lattice: convex closure has index 3 in its holomorphic hull, refuting 9.10.8.1's universal minimal-convex assertion. One-sided containment can repair an internal lower-bound step, so this is not an essential IUT flaw. |
| Other printed issues | (9.9.4)'s literal reference contradicts its j=1 case; 9.11.1.1's printed negative absolute-value LHS is nonpositive while its negative-log-q RHS is positive at nonempty bad places. Corrections do not supply original transfer. |
| Prior inputs not independently verified | Full IUT anabelian/Kummer/evaluation and formal-quotient dependencies; Yamashita's recursive proof; Joshi's deeper untilt/Fargues–Fontaine/amphoric reconstruction and global initial-data existence proofs. No complete independent verification of 9.11.1's volume derivation or IV's abc proof. |
| Does original Corollary 3.12 now follow? | **No, from this audit's established inputs.** This does not assert nonexistence of a proof. |
| Essential flaw established? | **No.** Refuted assertions have the narrower Joshi/local/printed scope documented above. |
| Final verdict | **D**, restricted alternative-locus estimate; no established original-IUT transfer. |
| Decision | **STOP this research route.** Preserve the reports; no next stage, new generalized category or further OpenAI search. |
| Additional paid/cloud/GPU spend | **GBP 0**. No correspondence, submission or prize application. |

## Evidence and repository verification

The proofs and limitations are in [PROOF_OR_OBSTRUCTION](PROOF_OR_OBSTRUCTION.md); all numerical conventions and sign/index controls are in [NUMERICAL_COMPARISON](NUMERICAL_COMPARISON.md); the source types, crosswalk and byte pins are in [SOURCE_CROSSWALK](SOURCE_CROSSWALK.md). Source histories still list the February 2025 versions as latest on 8 October 2026.

The original checkout `/Users/moheet/Documents/ChatGPT/IUT 🧮` was snapshotted at **534 tracked paths**, including the pre-existing deletion `recovery/2026-09-21/README.md`. The Stage 14 checkout and unrelated Superlinear/Hodge projects are preserved. Exactly these four new Markdown reports are intended for the new commit. No source pin, historical report or STATUS file is replaced.

Validation completed on 8 October 2026:

* `python3 scripts/verify_sources.py`: PASS, 18 pinned source/metadata records and 202 archived LANA files.
* `python3 scripts/validate_ledgers.py`: PASS, schemas, source locators, evidence labels, foreign keys, nine-step/DAG and generated-view checks.
* Temporary exact arithmetic: PASS, 44 permitted-prime coefficient controls, determinant -12/index 3 and 27/81 reduction image, excluded idempotent and both surjective projections; sign-domain and tensor nonadditivity controls. The general arguments are written in the reports.
* Artifact checks: exactly four files, 9 valid local links, balanced display/fence delimiters and 17 unique equation tags. Fresh explicit III v4 download matches its recorded SHA-256. Git ancestry and absence of an existing remote continuation branch were checked.
* Preservation: all 534 original tracked paths and the original branch, HEAD and status match the initial snapshot. The Stage 14 checkout remains clean at 09a6ce3.

No complete Lean/LANA build, exhaustive dependency verification or independent specialist certification was performed. Passing these checks does not certify the mathematical bridge. The final containing commit and remote SHA verification are returned in the final chat response; the four reports are the only new tracked files in that commit. Pushing the new branch also carries its inherited Stage 14 ancestor without modifying the separate Stage 14 branch.
