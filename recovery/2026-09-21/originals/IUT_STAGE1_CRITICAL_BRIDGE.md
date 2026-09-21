# IUT Stage 1: the xi-e → xi-f bridge

Prepared by Astra (OpenAI Codex), 21 September 2026. Bounded source audit; no claim to have settled IUT or abc.

**Outcome: TARGET_NOT_YET_FORMALIZABLE_WITHOUT_LARGER_IUT_DEPENDENCY.**

This is a statement about the completion boundary of this audit. The scalar conclusion has an unambiguous type. What is not yet available here is a complete, independently checked, source-faithful specification of the hypotheses and of the output construction needed to test that conclusion. Neither a proof nor a faithful countermodel was obtained. In particular, this report does **not** establish that a premise is absent from IUT.

The central correction to a simplistic audit is that the pre-xi-f material already asserts a closed-loop construction. IUT III, Remark 3.9.5(ix), pp. 141–144, especially p. 143, cannot be discarded from the premise inventory. Its assertion must be translated and its cited construction checked. Replacing it by an arbitrary isomorphism of real lines would change the problem.

Companion files:

- [Premise and source ledger](/Users/moheet/Documents/ChatGPT/IUT_CHALLENGER/IUT_STAGE1_SOURCE_MAP.csv)
- [Dependency graph and typed registry](/Users/moheet/Documents/ChatGPT/IUT_CHALLENGER/IUT_STAGE1_DEPENDENCY_GRAPH.json)
- [Candidate bridge and exact stopping point](/Users/moheet/Documents/ChatGPT/IUT_CHALLENGER/IUT_STAGE1_MISSING_PREMISE.md)

The ledger's exact-text cells contain short source markers or mathematical transcriptions, with their scope labeled explicitly. They do not reproduce full passages; the adjacent interpretations are this audit's analysis. The ledger and dependency graph are therefore an inspectable extraction aid, not a certified exhaustive formal premise set or proof graph.

## 1. Evidence and reading boundary

The following six required documents were read completely from their primary texts, including the critical diagrams. Page numbers below are **PDF/preprint page numbers**, not journal pagination.

| ID | Document and version used | Pages | Coverage |
|---|---|---:|---|
| III | [IUT III](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf), author's May 2020 version | 199 | Complete |
| CMT | [Comments on Scholze–Stix](https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-05.pdf), July 2018 | 8 | Complete |
| ELS | [Essential Logical Structure](https://www.kurims.kyoto-u.ac.jp/~motizuki/Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf), March 2024 | 167 | Complete |
| FORM | [Formalization of IUT](https://www.kurims.kyoto-u.ac.jp/~motizuki/Formalization%20of%20IUT%20%282026-04%29.pdf), April 2026 | 14 | Complete |
| SS | [Why abc is still a conjecture](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf), July 2018 | 10 | Complete |
| LANA | [Project LANA interim report](https://raw.githubusercontent.com/katobungen/LANA_report_202607/pdf/LANA_report_202607.pdf), updated 20 July 2026 | 50 | Complete |

Retrieved PDFs, extracted text, page images, byte counts and SHA-256 hashes are retained under `sources/` and `tmp/`. See `sources/retrieval.json` and `sources/dependency_retrieval.json`. Visual checks covered III pp. 143, 152, 183–185; FORM pp. 10–11; ELS pp. 151–152, 154; and LANA p. 46. This matters because text extraction loses arrows, superscripts, and the distinction between differently decorated prime-strips.

Selected directly relevant dependencies were also inspected: IUT I Definition 5.2; IUT II Definition 4.9 and Corollary 4.10; Frobenioids I Theorems 5.1–5.2 and 6.4; Frobenioids II Theorem 1.2 and Example 5.6; Absolute Anabelian Geometry III Propositions 5.7–5.8; Étale Theta Proposition 1.4; IUT IV's species definitions; and Alien Copies §3.11(v). These are **selected passages, not complete readings of those additional papers**. Their recursive dependencies have not all been discharged. Consequently the request to search every cited dependency to closure is not certified complete, and no exhaustive absence result is reported.

No existing Stage-0 package was located in the searched workspace, attachment, and Downloads locations. The audit therefore used the primary texts directly.

### Public Lean boundary

Two public repositories were inspected at pinned revisions:

- [LANA-Project/iut4-sec1](https://github.com/LANA-Project/iut4-sec1/tree/a7551d2f575b7e462cf9e82c587d9c6308e7b15c), revision `a7551d2f575b7e462cf9e82c587d9c6308e7b15c`. Its stated scope is IUT IV §1; it supplies no proof of this IUT III bridge.
- [lana-agents/iut](https://github.com/lana-agents/iut/tree/2d8f000457da6447fa4df4bfec7365c1a49b6384), revision `2d8f000457da6447fa4df4bfec7365c1a49b6384`. The relevant `Cor312` statement, left-hand side, right-hand side, and container/hull interface files were read. This is a distinct repository and is not silently treated as an official formalization of the critical inference.

In the second repository, `Corollary312Variant` **defines a proposition** `X.qPilot.lhs ≤ X.rhsData.rhs`. The accompanying definitional equivalence does not prove that proposition. In particular, the right-hand theta data and its admissibility/bounding properties are inputs to the interface; construction from the multiradial machinery is not established there. The hull interface proves useful properties under its supplied hypotheses, but that does not discharge the source-to-interface obligation.

The April document and July report describe incomplete or unpublished critical formalization work. That is a boundary on available evidence, not evidence that no further work exists. Neither repository was represented as a complete critical-bridge proof, and no complete repository build was claimed.

## 2. Stable outer target and unstable inner specification

Fix an admissible instance of the initial Θ-data and its log-theta-lattice. Write

\[
a:=qVol=-|\log(q)|,\qquad b:=-|\log(\Theta)|.
\]

After the finite-bound reduction in the printed proof, the outer types are

\[
a,b:\mathbb R,\quad OutVol:=\{x:\mathbb R\mid x\le b\}:\operatorname{Set}(\mathbb R).
\]

The relation defining `OutVol` is **DEFINITIONAL_EQUALITY**. The target relation is **MEMBERSHIP**, `a ∈ OutVol`; unfolding the definition gives a **PROPOSITIONAL_EQUALITY** of propositions with `a ≤ b`.

The notation `-|log(Θ)|` names the constructed bound. It must not be parsed as automatically the negative absolute value of a previously supplied real number. The statement of Corollary 3.12 initially allows an extended upper bound. If that bound is `+∞`, the scalar inequality is immediate; the nontrivial finite case is the one audited here. The source's finite-bound and sign reductions occur before xi-e.

**Locator correction:** the displayed definition of `OutVol` occurs in **xi-d, p. 183**, and is used in xi-e, pp. 183–184. The conclusion occurs in xi-f, p. 184. This does not change the requested target.

Do not equate the following merely because their notation involves real numbers:

1. the degree of a pilot object in a global realified Frobenioid;
2. the normalized log-volume of an admissible region;
3. a point of a value-group real line;
4. an equivalence class of measurable regions under equality of volume;
5. a member of the downset `OutVol`.

Each conversion requires an explicit map and a normalization/compatibility result. Also, `OutVol = {x | x ≤ b}` is not by itself a proof that every member is the log-volume of a separately specified admissible output object. That range or approximation assertion is one of the things a faithful specification must justify.

I use `H_source` for the ledger of source definitions and assertions. I reserve `H_IUT` for the desired fully typed, justified conjunction. This audit has **not** proved `H_source ≡ H_IUT` or supplied a complete formal `H_IUT`. Treating the strongest prose assertion in `H_source` as an axiom equal to `a ≤ b` would evade the task.

## 3. Object registry

The following are proposed interfaces, not a claim that all source constructions have been formalized. Relation tags have the exact meanings specified in the request. `OTHER_EXPLICITLY_DEFINED_RELATION` is used only with the predicate stated in the row. No unconstrained generic relation is used as a proof premise.

For precision, `PS` denotes the source's globally realified prime-strip data; decorations such as `F^{⊩▶×μ}` are retained when material. `Obj(C)` means objects of the indicated category; passing to isomorphism classes is a separate operation. `Region(V)` means regions satisfying the required local measurability and adelic restrictions, not all subsets.

| Object | Proposed type and retained data | Exact relation and obligation | Principal locators |
|---|---|---|---|
| InputPrimeStrip | `PS_{q,(1,0)}` of type `F^{⊩▶×μ}`: global realified Frobenioid, place index, local split/Kummer data, units modulo torsion, Galois actions and localization maps | **ISOMORPHISM** means an isomorphism of this collection of data, not only of its real line | II Def. 4.9(viii), p. 158; III xi-a–e |
| OutputPrimeStrip | Family of output `PS` data after construction; retain unit/Galois data through the hull and log-Kummer stages, then apply the specified value-part forgetful operation | **IMAGE_UNDER_MAP** only after that operation is typed; resulting `F^{⊩▶}` is not definitionally the input `F^{⊩▶×μ}` | III Rmk. 3.9.5(vii)–(ix); xi-d |
| qPilot | Distinguished object, up to **ISOMORPHISM**, of the input global realified Frobenioid; native right-column realization also retained | **IMAGE_UNDER_MAP** under the normalized degree/log-volume comparison gives `a` | II Def. 4.9(viii); III Def. 3.8; Prop. 3.9(iii) |
| thetaPilot | Distinguished object, up to **ISOMORPHISM**, in the left-column LGP construction before admissible indeterminacies | **IMAGE_UNDER_MAP** under the actual Θ comparison; cannot substitute equality of native arithmetic degrees | III Def. 3.8; Rmk. 3.8.1; CMT C12–C14 |
| IPL | The specified composite poly-isomorphism: a collection of compatible isomorphism composites through env/gau/LGP/lgp and Kummer constructions | **ISOMORPHISM** for its constituent composites, with specified provenance; not arbitrary existential isomorphism | III Rmk. 3.10.2, p. 152; Rmk. 3.11.1(iii) |
| SHE | Simultaneous construction in the right arithmetic holomorphic structure, with native input realization and correlated choices retained | **OTHER_EXPLICITLY_DEFINED_RELATION**: an execution diagram in the right-column structured category, including the fixed input realization and the hull/determinant/log-shift operations. The exact functors and coherence conditions remain to be instantiated | III Rmk. 3.11.1(iii), (v), (viii); xi-e |
| APT | Descent of a construction from the stronger input presentation to the permitted weaker input data | **OTHER_EXPLICITLY_DEFINED_RELATION**: a descended algorithm plus specified natural comparison to the original algorithm; this is not generally a map between underlying regions | III Rmk. 3.11.1(iv); ELS §3.9 |
| Ind1 | Automorphisms of the procession data and induced actions at the relevant stage | **SAME_ORBIT_UNDER_INDETERMINACY** only for the explicitly specified action | III Thm. 3.11(i), pp. 153–154 |
| Ind2 | Ism indeterminacy of unit/Kummer structures, with place and Galois constraints | **SAME_ORBIT_UNDER_INDETERMINACY** only for those Ism actions; not independent rescaling of all real lines | II Def. 4.9(i); III Thm. 3.11(i) |
| Ind3 | The stated one-sided compatibility conditions for log-shell realizations and their iterations | **OTHER_EXPLICITLY_DEFINED_RELATION**: the nonarchimedean inclusions and archimedean inclusion/surjection conditions of Prop. 3.5(ii), with iteration compatibility. No global group-action quotient is supplied here | III Prop. 3.5(ii); Thm. 3.11(ii) |
| LogKummer | Indexed local Kummer comparisons together with partially defined logarithm operations on units and the resulting log-shell constructions | **ISOMORPHISM** for specified Kummer comparisons; **IMAGE_UNDER_MAP** for logarithms on their stated domains. Commutation is not automatic | III Prop. 1.2; Rmk. 3.9.4; Rmk. 3.9.5(sQ4) |
| HolomorphicHull | Closure operation `φ` on admissible region data using the fixed right-column arithmetic structure, with separate quotient/descent data | **MEMBERSHIP** for points in `φ(P)`; **OTHER_EXPLICITLY_DEFINED_RELATION** for `P ⊆ φ(P)` and monotonicity. Hull existence alone does not prove input-pilot coverage | III Rmk. 3.9.5(i)–(vii) |
| Determinant | Determinant of localized arithmetic vector bundles, after the specified positive tensor power and inverse structure-sheaf twist; induced realified line-object data | **IMAGE_UNDER_MAP**; preservation of normalized degree is an additional **PROPOSITIONAL_EQUALITY**, not the definition of every determinant map | III Rmk. 3.9.5(Ob3)–(Ob4); xi-d |
| LogVolume | Normalized local volumes assembled with the packet/procession weights and global degree interpretation; quotient map to volume classes where applicable | **IMAGE_UNDER_MAP**; equality under each permitted operation must be stated separately, and Ind3 may give a one-sided relation | III Props. 3.2, 3.9; Rmks. 3.9.4–3.9.7 |
| CommonContainer | At the geometric stage, the right tensor-packet ambient space and its region/category structures; at the scalar stage, the normalized real line | **MEMBERSHIP** or explicit inclusion at the relevant stage. The geometric container and scalar real line are different types | III xi-b–d; ELS §3.10 |
| OutputPossibilities | A correlated family of admissible output data modulo the source's specified formal indeterminacies, followed by volume comparison | **IMAGE_UNDER_MAP** once its domain and map are established; **APPROXIMATE_RELATION** for the candidate cofinal approximation below. A set of arbitrary regions is not a faithful replacement | III Rmk. 3.9.5(v), (viii)–(ix); xi-e–f |

The missing formal definitions in the SHE/APT/output rows are deliberately visible. Naming a record field `preserves_q` would not establish the corresponding source theorem. The registry is explicit enough to expose this obstruction; it is not a finished mathematical theory of the records.

## 4. Reconstructing xi-e without strengthening it

The ledger separates four levels: definitions; assertions before xi-f; later explanations; and the target itself. Later explanations may direct a search, but they are not silently inserted as earlier proved lemmas.

The typed reconstruction proceeds through these interfaces:

1. **Native input.** Choose the right-column prime-strip with its native q-pilot realization. Apply the degree/log-volume comparison to obtain `a : ℝ`. This retains a native realization, not just an abstract pilot isomorphism class.
2. **Construction comparison.** Use the actual Θ and IPL poly-isomorphism composites and Theorem 3.11's representation. The admissible choices must carry their correlations. An unrestricted Cartesian product of local choices is not assumed.
3. **Ambient realization.** Realize the region family in the right tensor-packet space with the source's unit/Galois structure and indeterminacies. The inclusions of regions here are **OTHER_EXPLICITLY_DEFINED_RELATION**, namely subset inclusion; intervening strip comparisons are **ISOMORPHISM**.
4. **Hull and determinant.** Apply the right arithmetic holomorphic hull, the weighted tensor/determinant construction, and the appropriate formal quotient. Preserve the data required for the log-Kummer operation before forgetting it.
5. **Vertical reconciliation.** Account for the one-step vertical offset between the unit data and its log-shell image. Use the established normalized comparison where applicable; do not replace the logarithm by a total, everywhere measure-preserving map.
6. **Scalar output.** Obtain the asserted output-volume family bounded by `b`, represented in xi-d/e by `OutVol`. The native input remains constrained to degree `a` while operations are executed in the right-column structure.

This inventory includes the assertion in Remark 3.9.5(ix) that the construction returns through the designated right-column structure, up to its formal quotient indeterminacies. It also includes xi-e's claim that the operations are executable subject to the fixed native input volume. Neither assertion has been replaced by the weaker claim that two abstract objects admit some isomorphism.

There is nevertheless an uncompleted **translation and verification obligation**: specify the admissibility predicate and construction/comparison maps so that retaining the native input constraint entails coverage of `a` by the output downset. Merely being defined on inputs of degree `a` is not, in general, the property that the output covers degree `a`. This elementary distinction diagnoses what the translation must prove; it does not show that the actual IUT construction lacks that property.

## 5. Weakest sufficient bridge: what can and cannot be claimed

There is no justified noncircular, source-specific `P*` in this audit because the full `H_IUT` and the admissible language for `P*` are not yet fixed.

In unrestricted propositional logic, the weakest sufficient extra assumption is `H_IUT → (a ≤ b)`. Under `H_IUT` this is equivalent to the desired conclusion, so it is disallowed as a substantive bridge. Selecting a purported weakest mathematical premise without specifying its language would hide this problem.

A useful **conditional interface** is the following. Suppose that a source-faithful type `A` of admissible outputs, a map `L : A → ℝ`, and

\[
(UB)\qquad \forall O:A,\ L(O)\le b
\]

have first been justified. Then the candidate

\[
(P_{\mathrm{approx}})\qquad
\forall\varepsilon>0\;\exists O:A,\quad a-\varepsilon\le L(O)
\]

is sufficient. This is an **APPROXIMATE_RELATION**, explicitly one-sided cofinal approximation from below; it does not require a representative attaining `a`.

Proof: if `a > b`, choose `ε = (a-b)/2`. A witness gives `L(O) ≥ (a+b)/2 > b`, contradicting `UB`. Thus `a ≤ b`, or **MEMBERSHIP** `a ∈ OutVol`.

An exact witness `L(O)=a` or an order witness `a≤L(O)` also suffices but imposes stronger witness requirements. The companion note gives the precise logical qualifications. These are mathematical interface lemmas, **not** proofs that IUT supplies `A`, `UB`, or `P_approx`.

**Search classification: FOUND_ONLY_AS_INFORMAL_EXPLANATION.** The closest candidate is not absent from the text: III Remark 3.9.5(ix), followed by Remark 3.11.1 and xi-e, already provides a construction-level explanation. ELS §3.10, especially Stp7–Stp8 and its discussion on pp. 151–156, and Alien Copies §3.11(v), pp. 143–146, explain the intended preservation further. Here “informal” means that this audit has not extracted and independently checked the exact typed preservation theorem; it does not mean that ordinary written mathematics must be Lean-verified to count as a proof. No circularity finding is asserted. Recursive dependency coverage remains incomplete.

## 6. A, B, C are not interchangeable by declaration

For this comparison:

- **A** is the author's construction-level requirement: simultaneous q and Θ constraints in the designated structured container, maintained through the synchronized permitted indeterminacies and operations.
- **B** is LANA's proposed comparison, particularly its §9.2 equation (9-1), p. 46: existence of a suitable region `S` with `η^q = η_S^anab` after the targets have been put in the prescribed comparison. The equality is **PROPOSITIONAL_EQUALITY** of specified maps, not an arbitrary real-line isomorphism. The meaning of “suitable” is essential.
- **C** is the printed conclusion `a ∈ OutVol`, with the actual pre-xi-f construction supplying its hypotheses. Its final scalar assertion is strictly less data than a complete map comparison.

| Implication | Status for the actual IUT formulations | Undischarged obligation |
|---|---|---|
| A → B | NOT_YET_FORMALIZABLE | Interpret the formal quotients and synchronization as exactly LANA's admissible `S` and comparison maps |
| B → A | NOT_YET_FORMALIZABLE | Recover the required structured construction and its coherence from the scalar/map formulation; equality of maps alone does not supply that recovery |
| A → C | NOT_YET_FORMALIZABLE | Check preservation of the native q constraint through the actual hull, determinant, formal quotient, and vertical reconciliation |
| C → A | NOT_YET_FORMALIZABLE | Specify A fully before testing whether a single inequality implies that much structured data |
| B → C | NOT_YET_FORMALIZABLE | Verify the source-faithful admissibility predicate, pilot evaluation and common volume normalization |
| C → B | NOT_YET_FORMALIZABLE | Specify B fully and justify any recovery of a comparison map and admissible witness from a scalar inequality |

These statuses do not claim that any implication is false. They describe the present source-to-formula boundary.

There is a simple conditional B → C lemma: if a suitable `S` determines an admissible output `O_S`, evaluation of `η_S^anab` at the pilot gives `L(O_S)`, evaluation of `η^q` gives `a` in one normalized scalar target, and those maps are equal, then `L(O_S)=a`; `UB` gives C. The pilot-evaluation and admissibility hypotheses must be proved for the real construction. This conditional lemma cannot be substituted for an unconditional claim about LANA's formulation.

The reverse implications are not licensed merely because that conditional lemma works. The author's criticism of a two-map framing must likewise be evaluated through an explicit translation, not used to dismiss B by authority. LANA's right-column comparison must not be conflated with the Scholze–Stix hexagon.

## 7. Proof attempt and first stopping point

The scalar last step closes under `UB + P_approx`. The source-specific proof does not reach those hypotheses here.

The attempted route is:

`native q realization → specified Θ/IPL construction → multiradial output → right hull → determinant/formal quotient → vertical log-Kummer reconciliation → normalized output volumes`.

The first unclosed obligation in this audit is at the combined construction described by **III Remark 3.9.5(ix), (cQ3)/(cQ4), pp. 141–144**, as applied in **xi-d/e, pp. 183–184**. It is necessary to show that its induced comparison retains the native q-pilot constraint in a sense strong enough to place its normalized degree in the downward closure of the closure of admissible output degrees. That could be witnessed by an actual output object, an order comparison, or an admissible approximating family. The source's formal quotient and vertical offset determine which is correct.

The derivation stops there. This is **not a demonstrated fatal step in the published proof**. The source asserts the relevant closure; the audit has not completed the exact interpretation and dependency proof of that assertion. Omitting it would make a refutation easier but would fail the preservation requirement.

## 8. Countermodel attempt and rejection boundary

Start at Layer 0. A sets/maps abstraction can retain a real number, a bounded output set, and an existential isomorphism. Such data readily permits an input above the output bound. It does not encode the specified composite, the pilot, the unit/Galois data, global localization, formal quotient, or native arithmetic realization. Therefore it is rejected **before** being called a model of `H_IUT`.

Increasing the abstraction level does not automatically repair this omission:

| Layer | Data that would have to be retained | Result here |
|---|---|---|
| 0: sets/maps | Actual operation domains, admissibility and correlated choices, plus interpretation of each premise | No faithful interpretation proved |
| 1: groups | Unit/torsion and value data, distinguished pilots, specified actions | Insufficient without further structure; no candidate certified |
| 2: topological groups | Galois actions, compact structures, partial log domains and normalized measures | No complete predicate-preservation proof |
| 3: categories/groupoids | Frobenioids, localization, poly-isomorphism composites, formal quotient and descent coherence | Closest structural interface inspected; faithful output specification unresolved |
| 4: valued fields | Native arithmetic holomorphic realizations and local compatibility, without imposing a spurious common field | No model constructed |
| 5: arithmetic geometry | Global product formula, degree normalization and local/global coherence | No model constructed |
| 6: Hodge-theater machinery | Actual admissible initial data and complete construction | No model constructed |

There is a further logical requirement beyond a one-way preservation map. Suppose every actual instance maps to an abstract instance satisfying the translated premises. An arbitrary abstract counterexample need not lie in that image. To refute the actual theorem using that counterexample requires a realization/lifting theorem, or another argument transferring failure back to an actual instance. Conversely, a countermodel to a faithfully translated **formal consequence of premises** can refute that abstract consequence, but only after the premise translation and intended scope are justified. Neither certification is supplied here.

No scalar-linear `(Lin)` model, arbitrary rescaling, or unsupported monodromy calculation is presented as an IUT counterexample. The Scholze–Stix objection and the author's response remain distinct source positions in the ledger; neither receives a verdict by attribution alone.

**Faithful countermodel found: NO.**

## 9. Lean decision, remaining work, and scope

No Lean file was created. The real-order interface lemma is stable, but the requested theorem's core input/output predicates are not yet faithfully specified here. A file assuming `preserves_q` or `P_approx` and then proving `a ≤ b` would prove a conditional real-order lemma while concealing the requested work. The user specifically conditioned the Lean skeleton on a stable mathematical target.

The bounded next action, **not started by this audit**, is to obtain or independently specify the local/global formal quotient and its induced comparison in Remark 3.9.5(ix), including (cQ3), (cQ4), the retained unit/Galois structures, determinant normalization, and vertical shift. The acceptance test is a documented interpretation into the native q-constrained output family. Only then should the actual A/B/C translations and a Lean theorem be attempted.

This report does not certify the target as permanently unformalizable, claim an exact premise is missing from IUT, or imply a flaw/prize result. It records why neither proof nor refutation is justified by this audit's completed work.

All new files are outside Superlinear. No parity work, cloud computation, repository modification, or next research stage was performed. Incremental external compute spend: **GBP 0**. This is not an accounting of the user's pre-existing subscription or inference charges.
