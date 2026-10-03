# Native-to-hull clarification packet

**2026-10-03 | READY_FOR_SPECIALIST_CLARIFICATION | Draft only; not sent.**

This packet continues [E3d.3](../09_log_step_adequacy/DECISION.md) from `9419e5053e0ad0a90c95b6f70f5ff6ad66b7162d`, on `codex/native-hull-review`. No newer continuation was found after fetching origin. The preceding chat report is secondary project context, not independent replication. No missing remainder of a separate truncated report was inferred.

## Target and distinctions

**SOURCE STATEMENT.** In [Yamashita, Corollary 13.13](https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2018Jan19.pdf#page=352), pp.352-353, the target is

\[
a_q=-|\log q|\le b=-|\log\Theta|.
\]

The right side evaluates the holomorphic hull; the native q-pilot is excluded from the output indeterminacies. The proof, p.353, asserts containment of a region isomorphic to the q-pilot region.

**PROPOSED INTERPRETATION / notation for this question.** Distinguish:

- \(P_\Theta\): raw permitted output regions, with the stipulated coupled choices.
- \(H_\Theta=\operatorname{Hull}(\bigcup P_\Theta)\): the holomorphic hull, evaluated with the source's packet/procession normalization and permitted indeterminacies.
- \(V\): a selected region inside that hull, or a weaker formal/approximate comparison datum if that is the intended meaning.
- \(Rss\) representatives: numerical function classes; they are not automatically arithmetic regions or raw outputs.

We do not require \(V\in P_\Theta\), identify \(b\) with the supremum of raw-output values, or demand exact attainment, a canonical region, a global section, or transport of all determinant orbits.

## Bounded source check

**SOURCE STATEMENTS.** The proof invokes Theorem 13.12(1)-(3) and Remark 11.1.1. Definition 11.1, p.247, makes multiradiality fullness of the radial functor. Remark 11.1.1, p.248, supplies switching up to isomorphism. Theorem 13.12(3)(a)-(d), pp.349-351, states compatibility with the Θ-link and evaluation maps, including the prescribed indeterminacies. Its preceding paragraph, p.349, supplies log-volume compatibility and distinguishes MOD from mod.

**UNRESOLVED instantiation.** These are substantive ingredients. The bounded check has not identified the selected region's precise structure, its comparison with the fixed native region, and the jointly admissible choices making its containment and normalized evaluation hold together. The prose assertion is retained as a source claim; its brevity is not evidence against it.

[IUT III](../../sources/primary/IUT_III.pdf), Remark 3.9.4(iii)-(iv), pp.123-124, supplies the local numerical comparison. Ob9/Ob9-1, pp.138-139, permit intermediate non-hulls when comparing volume classes. Remark 3.9.5(ix), pp.143-144, asserts the native-constrained comparison before numerical forgetting. Theorem 3.11(ii), pp.155-156, retains precise log-volume compatibility. Xi-d through xi-f, pp.183-184, identify the concluding comparison, including possible approximation; they are not premises here.

## Positive local result already reconstructed

**ACCEPTED SOURCE INPUTS:** an injective compact ample unit chart \(S\), positive measure \(s\), and \(\mu(S)=\mu(\log_k S)=s\), with the source normalization.

**DERIVATION FROM THOSE INPUTS, already recorded in [LOCAL_CALCULATION](../09_log_step_adequacy/LOCAL_CALCULATION.md):**

\[
f\sim\frac{\int f}{s}\mathbf1_S
\longmapsto\frac{\int f}{s}\mathbf1_{\log_k S}.
\]

This preserves the integral and normalized log-volume. For the native ideal \(q^{Mr}\mathcal O_k\), the preserved value is

\[
-Mr\,\operatorname{ord}_v(q)\log p_v,
\]

where \(q\) is the prescribed root of the Tate parameter and \(M>0\) is the same permitted tensor exponent. No logarithm is applied to the nonunit pilot. This calculation is acknowledged, not re-proved or tested by a new p-adic experiment.

**Acceptance boundary:** the weighted function need not be a hull or an admissible arithmetic region. Native contextual labels do not prove algorithmic provenance. The generic chart has not been attached to the particular labeled Kummer unit-domain choice. One local equality supplies no global inequality.

## Comparison diagram

```text
P_Theta: raw regions -- union, holomorphic hull --> H_Theta -- LV --> b
                                                       ^
                                                       | containment asserted
R_q: native marked region .... selected comparison .... V
       |                                               .
       | local component, numerical quotient           . attachment unresolved
       v                                               v
   Rss(E_-) -------- Phi_log: numerical comparison --> Rss(E_+)
       ^                                               ^
       | quotient                                      | quotient
  1_(q^(Mr) O_k)                           (integral f / s) 1_log(S)
```

The lower row concerns one fixed local component. Dotted connections record the clarification sought, not constructed maps. A formal interpretation of \(V\) may replace the upper containment picture.

**DERIVATION / sufficient schematic test:** for source-admissible measurable regions and the applicable monotonicity, \(V\subseteq H_\Theta\) and \(a_q\le LV(V)\) imply \(a_q\le b\). Equality would suffice; so would admissible approximants with \(a_q-\varepsilon\le LV(V_\varepsilon)\le b\) for every \(\varepsilon>0\). Neither existence nor admissibility is defined by these inequalities or assumed here.

## Single clarification question

In Yamashita's Corollary 13.13 proof (p.353), which construction supplies the region inside the Θ-output hull compared with the native q-pilot region, what kind of isomorphism or weaker formal comparison is intended, and which preceding result, with its instantiation, ensures the native marking and normalized degree compatibility under jointly admissible choices?

We have reconstructed the local Rss numerical comparison, but not its attachment to this particular bounded hull/formal construction. An explicit construction, a theorem with its instantiation, a correction of this interpretation, or a weaker sufficient comparison would answer the question.

## What an answer changes

| Answer | Consequence for this audit |
|---|---|
| Explicit construction | Check its endpoints, native marking, normalization and coupled choices; credit exactly the scope established. |
| Named theorem with instantiation | Replace the unresolved attachment with that dependency once its hypotheses are checked. |
| Correction of our interpretation | Withdraw the excess requirement and revise this question; no source defect follows. |
| Weaker formal/approximate comparison | Use that comparison with its independently justified bound; do not demand an exact region. |

Absent such clarification, no W*, global section, admissible approximation sequence, or xi-f derivation has been obtained. No flaw or nonexistence result is claimed.

## Provenance and review gate

[SOURCE_MAP.csv](SOURCE_MAP.csv) records hashes, locators and access limits. IUT III is the pinned May 2020 author PDF. Yamashita's inspected 400-page author PDF is identified by URL and SHA-256; its front matter has placeholder publication dates. Printed/PDF pagination agrees at the cited passages. Pages 248, 349 and 353 were rendered and visually inspected. The statement prints apparent self-references to Theorem 13.13(1)/(2); the proof explicitly invokes Theorem 13.12. No silent emendation is used.

Artifact validation passed: 18 source pins/metadata records and 202 LANA files match their pinned archive; word limits, CSV schema, local links and whitespace checks passed. Pre-existing tracked files other than the two current-state notices retain their baseline contents or deletion. These are provenance and artifact checks, not mathematical verification.

Only the requested anchors and their immediate context were checked; underlying IUT dependencies were not recursively verified. The [request draft](REQUEST_DRAFT.txt) remains unsent. Obtaining an external answer requires authorization to send the final draft to a user-designated recipient through a specified channel. Additional paid-service/cloud/GPU spend: GBP 0. Stop at this review gate.
