# IUT III xi-e → xi-f: bounded prove-or-break audit

Prepared by **Astra (Codex)**, 2026-09-21. Scope: one implication in the proof of IUT III, Corollary 3.12. This is a source reconstruction and scope decision, not an independently verified IUT result.

**Decision: TARGET_NOT_YET_FORMALIZABLE_WITHOUT_LARGER_IUT_DEPENDENCY. Apply the kill rule and stop this bounded attack.** This verdict concerns the reconstruction completed here. It does not assert that the implication is intrinsically unformalizable, false, or absent from IUT.

The exact numerical conclusion is accessible. The complete structured antecedent is not reconstructed. In particular, a formal quotient of collections of local/global Frobenioid objects with Galois/unit actions cannot be replaced here by a set of arbitrary scalar maps. The source expressly requires the structure that such a replacement would discard.

## 1. Scope, provenance, and limits

The recovered repository already contains a root-level Stage-1 audit. It was used as a retrieval index, not independent mathematical evidence. No separate Stage-0 package establishing GO—CONDITIONAL was located in the inspected project locations; that status is supplied by the request. This directory records a fresh check of the critical passages, explicit CSV registries, all twelve directed formulation comparisons, and the stricter stop decision requested now. It does not overwrite the recovered audit.

Six principal PDFs were fetched again from their primary URLs on 2026-09-21; every SHA-256 matched the recovered copy. The two inspected public Lean repository heads also matched the recovered snapshots. See [source map](IUT_STAGE1_SOURCE_MAP.md) for pages, hashes, URLs, read depth, and unexpanded dependencies. The source map does **not** claim complete recursive dependency coverage.

No cloud resources, brute-force search, new Lean development, other mathematical programme, or Superlinear modification was used. Existing unrelated changes in this IUT working tree are outside this audit.

## 2. The exact outer types

Let `a` denote the source's `−|log(q)|`, and `b` its `−|log(Θ)|`. These are names for specified normalized log-volumes, not permission to substitute arbitrary real numbers for the underlying arithmetic data.

At the statement of Corollary 3.12, III pp. 173–174:

- `a : ℝ` is the procession-normalized mono-analytic log-volume of the q-pilot image under the prescribed Kummer representation. The q-pilot is **not** subjected to Ind1, Ind2, Ind3. The source has `|log(q)| > 0`, hence `a < 0`.
- `b : ℝ ∪ {+∞}` is the normalized log-volume of the holomorphic hull of the union of the possible Θ-pilot images, subject to Ind1, Ind2, Ind3.
- The source's preliminary argument, p. 175, asserts finiteness using compactness of the relevant hulls. The nontrivial case has `b < 0`; finite `b ≥ 0` already gives `a ≤ b`. This audit records, but does not independently re-prove, that preliminary compactness assertion.

At xi-d, p. 183, after this reduction, the types really are

```text
a : ℝ
b : ℝ
OutVol := { t : ℝ | t ≤ b } : Set ℝ.
C_xif := a ∈ OutVol.
```

The relation `C_xif ↔ a ≤ b` is **DEFINITIONAL_EQUALITY** by set-membership unfolding. Thus the provisional membership target is correct **at this stage of the source**, not as a replacement for its upstream structures. The conclusion of the whole corollary additionally includes finiteness; the xi-e → xi-f target does not prove that preliminary claim anew.

`OutVol` is explicitly a numerical down-set. It has **not** been established in this audit as `IMAGE(L, A)` for a fully specified admissible-output type `A` and a map `L : A → ℝ`. In particular, the definition does not prove attainment of every real number below `b` by a structured output. The source allows approximation in xi-f. These distinctions preclude silently strengthening the target to exact output attainment.

The q-pilot itself is an object, up to **ISOMORPHISM**, of a global realified Frobenioid determined by prime-strip data (II, Definition 4.9(viii), p. 158). It is not a real number until the stipulated degree/log-volume construction is applied. The Θ-pilot and q-pilot have distinct native arithmetic realizations. The Θ-link is a full poly-**ISOMORPHISM** of the specified prime-strips, not an equality of their native ring structures or native numerical degree maps.

## 3. What xi-e actually says

Source: III pp. 183–184, read with xi-b–d pp. 181–183, Theorem 3.11 pp. 153–159, Remark 3.11.1 pp. 159–166, and Remark 3.9.5 pp. 126–145.

Faithful structured prose, retaining unresolved construction interfaces:

1. Fix the input `F^{⊩▶×μ}` prime-strip with its q-pilot realization in the arithmetic holomorphic structure of the 1-column. Its normalized pilot volume is the fixed `a` (**MAP**, followed by **PROPOSITIONAL_EQUALITY** to the prescribed value).
2. Apply the particular multiradial construction, enlarge through the holomorphic hull, pass through the normalized determinant construction, and use the 1-column log-Kummer correspondence to account for the vertical shift (**MAP**, **IMAGE**, and the specified **BOUNDED_INDETERMINACY** relations).
3. IPL supplies the operation-induced full poly-**ISOMORPHISM** relations between the value-group prime-strip portions of the output possibilities and the input. The unit portion carries the additional indeterminacy data; it is not removed from the preceding construction.
4. SHE says that these operations are expressible and executable relative to the 1-column arithmetic holomorphic structure, including its imposed input-volume condition (**LOGICAL_CONJUNCTION_OF_STRUCTURES**).
5. The source describes the numerical output possibilities as `OutVol`, with the preceding structured IPL and SHE properties. Xi-e does not present an independent, fully expanded set-theoretic contract whose symbols are only `A`, `L`, `a`, and `b`.

This is more specific than arbitrary output/input isomorphism. It is also not a derivation of numerical membership from mere executability. The construction and its claimed joint structure must remain part of the antecedent.

### The strongest upstream passage must not be deleted

Remark 3.9.5(ix), pp. 141–144, is central. The source describes local quotient categories, local/global collections with localization isomorphisms, faithful local Galois and unit actions, and compatibility through the log-Kummer correspondence. It then asserts a closed construction carrying the Θ-intertwining, with indeterminacies, and the fixed q-intertwining jointly (**LOGICAL_CONJUNCTION_OF_STRUCTURES**). The log-volume operation is deliberately applied after these stages because it forgets unit/Galois data (iQ5).

The audit cannot omit that assertion and call the remaining scalar facts “all pre-xi-f premises.” Conversely, treating that assertion as an axiom already guaranteeing native q-volume coverage would assume the disputed content. The formal quotient and its numerical consequence require a precise construction interface before either move can be justified.

The source's explanatory remarks can contain mathematical arguments. Their classification as `EXPLANATORY_REMARK` in the ledger is a source-genre distinction, not a finding that they are invalid or have no proof content.

## 4. H_pre: explicit incompleteness declaration

**A complete, faithful `H_pre` was not obtained.** No claim of `H_pre ⊬ C_xif` is made.

The [premise ledger](IUT_STAGE1_PREMISES.csv) separates source definitions, numbered theorems, prior properties, explanatory remarks, and interpretations. Its `PRE_XIF` rows form an **extracted ledger** `H_extracted`, not a complete formal conjunction. `H_pre` remains the intended conjunction of all genuinely established source facts with their actual domains, quantified choices, and compatibility conditions. Later explanations and the conclusion in xi-f/xi-g are not silently added to it.

The [object registry](IUT_STAGE1_OBJECT_REGISTRY.csv) marks source-dependent types and unresolved interfaces. In particular, `O33` and `O35` are proposed audit interfaces, not objects claimed to have been extracted completely from IUT. The graph is a source/dependency graph, not a certified proof graph.

The unresolved boundary is concrete:

- Formal quotient semantics for the pair of categories in cQ3, including structure poly-morphisms, local/global localization, and correlated choices; this is not simply a quotient set with an arbitrary representative selector.
- The exact input/output contract of the composite hull, approximant, determinant, and log-shift construction, with the Galois/unit data required by cQ3/cQ4.
- The numerical interpretation of the resulting joint q/Θ structure in the prescribed native q normalization. Invariance under the correctly scoped log-links is available in the source; arbitrary log-region measure preservation is not.

Expanding these interfaces calls back into II Definition 4.9/Corollary 4.10, Frobenioid/local-global constructions, and the log-Kummer machinery underlying III Theorem 3.11 and Remark 3.9.5. That is the larger dependency boundary triggering the requested kill rule. This audit does not claim to know a lower bound on the number of pages needed by an expert.

## 5. Proof attempt and first unsupported step

The following records the attempted reconstruction. “Source theorem” here means use of a stated theorem with its original hypotheses, not a fresh independent verification of its proof.

| Step | Input facts | Rule/theorem | Output / audit disposition |
|---|---|---|---|
| 1 | A source instance and the finite-case reduction, P01, P22–P24 | Definitions in the corollary and prior finite-case property | `a,b : ℝ`; the target can be typed. |
| 2 | P25, `OutVol := {t | t ≤ b}` | Definition unfolding | `C_xif ↔ a ≤ b`. |
| 3 | P04–P09, P10–P21, P26–P28 | The stated constructions and their precise source-level assertions | A source-described multiradial/hull/determinant/log-Kummer construction, with operation-induced IPL and SHE. No scalar abstraction substituted. |
| **4 — STOP** | In particular P14–P18 and P27–P28 | Would require a source-faithful interpretation of the formal quotient and joint q/Θ structure | **Not reconstructed:** a typed admissible-output interface and a demonstrated consequence that the fixed native q volume is covered (possibly approximately) by its bounded output volumes. |

Step 4 is the first unsupported step **in this reconstruction**, not a proved invalid inference in Mochizuki's mathematics. Step 3 records the source assertions; it does not silently certify their conversion into a complete formal antecedent. The failure is therefore earlier than a valid countermodel test of `H_pre ⇒ C_xif`.

The xi-g claim of two equivalent computations is downstream of xi-f (III pp. 184–185). Using it to justify step 4 would import the conclusion's explanation as an independent pre-xi-f premise. This audit does not do that.

### An elementary conditional lemma, and its strict limitation

Let `A` be any type, `L : A → ℝ`, and `a,b : ℝ`. Suppose:

```text
UB:     ∀ x : A, L(x) ≤ b
APX:    ∀ ε : ℝ, ε > 0 → ∃ x : A, a − ε ≤ L(x).
```

Then `a ≤ b`. Proof: if `a > b`, put `ε = (a−b)/2 > 0`. APX supplies `x` with `a−ε ≤ L(x)`. UB gives `a−ε ≤ b`. But `a−ε = (a+b)/2 > b`, a contradiction. Membership in `OutVol` follows by definition unfolding.

Every step is elementary real-order reasoning. It proves **only this conditional lemma**. It does not establish source-faithful `A`, `L`, UB, or APX. No Lean wrapper would change that. In particular APX is not declared the exact missing IUT premise.

## 6. P*: no exact missing-premise verdict

**P_STAR: NOT_IDENTIFIED_AS_A_SOURCE_FAITHFUL_PROPOSITION.**

**P_STAR_SOURCE_STATUS: UNABLE_TO_DETERMINE.**

APX is a sufficient scalar candidate in a separately specified interface. Exact attainment and domination are stronger alternatives. None has been established as necessary, weakest, or the precise residual obligation of the published construction. The [missing-premise analysis](IUT_STAGE1_MISSING_PREMISE.md) proves the elementary relationships and explains why choosing the numerical down-set as the output domain makes APX equivalent to the conclusion itself.

The source chain contains substantial, explicit assertions of the intended joint construction. Therefore `NOT_FOUND` would misreport the search. The recursive dependency chain has not been fully discharged, so this audit cannot assert that IUT nowhere proves a precise P*. Outcome C is unavailable.

## 7. Four formulations, kept distinct

**A — Printed IUT.** The particular prime-strip algorithm of Theorem 3.11, followed by the formal quotient/hull/determinant/log-Kummer construction in Remark 3.9.5 and the IPL/SHE assertions, is used to conclude native numerical membership. Its numerical conclusion is precise; its complete structured antecedent remains unexpanded here.

**B — Later Mochizuki explanations.** Essential Logical Structure §3.10, especially Stp7–8 and FxGl/NoCmpIss/Englf, retains a fixed Θ-link gluing and expands the possibilities on its Θ side. The claim is preservation of a **LOGICAL_CONJUNCTION_OF_STRUCTURES**, eventual descent to a numerical container, and synchronized indeterminacies. It explicitly rejects treating the intended construction as two arbitrary maps needing an additional comparison. The April 2026 note reorganizes the proof: HDD is the composite of hull+det with descent (**DEFINITIONAL_EQUALITY**); the informal “3.11.5” moves hull+det into the antecedent and isolates a final SHE+IPL comparison. This is a decomposition proposal, not a new numbered theorem supplying all interfaces.

**C — Scholze–Stix.** §2.2 compares abstract generators, concrete divisors, and normalized real lines. The q side and Θ side use different arithmetic scales; their proposed hexagon has nontrivial scalar monodromy, and a correction of order ℓ² would destroy the intended estimate. The scalar diagram calculation is distinct from proof that the diagram faithfully represents the whole printed mechanism.

**D — LANA.** §9.2 proposes `∃ suitable S, η^q = η_S^anab` (9-1), an equality of the constructed comparison maps after the stipulated domain/target interpretations (**PROPOSITIONAL_EQUALITY**). The target uses adelic measurable regions modulo equality of volume (**SAME_EQUIVALENCE_CLASS**), with distinguished pilots. The predicate “suitable,” the anabelian construction, and consistent pointed normalization are substantive. One cannot erase the distinguished points and infer the equality from bare **ISOMORPHISM** of real lines. §10.5 reports no proof of (9-1) at that time; §§10.2–10.4 say that the noncommuting Scholze–Stix diagram alone does not establish a defect in the intended mechanism.

Here arrows ask whether the **load-bearing formulation**, with its actual structures, translates to and implies the other. They do not compare four already typed Boolean propositions with fixed truth values. `NOT_YET_FORMALIZABLE` refers to this audit's missing faithful translation, not an impossibility claim.

| Arrow | Classification | Reason |
|---|---|---|
| A → B | NOT_YET_FORMALIZABLE | Source asserts continuity; formal-quotient to synchronized-construction translation is unexpanded. |
| B → A | NOT_YET_FORMALIZABLE | Later interface is not independently instantiated in the complete printed data. |
| A → C | NOT_YET_FORMALIZABLE | No preservation/reflection theorem licenses the scalar compression. |
| C → A | NOT_YET_FORMALIZABLE | A scalar obstruction has not been realized with all A structures. |
| A → D | NOT_YET_FORMALIZABLE | No fully typed translation to suitable `S` and the η comparison is proved here. |
| D → A | NOT_YET_FORMALIZABLE | Its intended numerical role is described; the full hypotheses/output-family translation is unproved. |
| B → C | NOT_YET_FORMALIZABLE | The fixed gluing and label/indeterminacy operations are not translated into C. |
| C → B | NOT_YET_FORMALIZABLE | C does not reconstruct the synchronized structured construction. |
| B → D | NOT_YET_FORMALIZABLE | B rejects the two-map framing; no faithful equivalence to D is established. |
| D → B | NOT_YET_FORMALIZABLE | No theorem reconstructs B's gluing/descent package from (9-1). |
| C → D | UNPROVED | Noncommutation of C's hexagon does not by itself decide D's map equality. |
| D → C | UNPROVED | The η equality would not by itself require commutation of C's different hexagon. |

No pairwise equivalence is established. Different presentations alone do not prove `NOT_EQUIVALENT`. A failed reconstruction alone does not prove `REFUTED`. Neither author's status nor institutional authority supplies a translation theorem.

## 8. Countermodel and Lean gates

At Level 0 (sets/maps), one can refute the weakened assertion that arbitrary isomorphism plus executability forces numeric coverage. At Level 1, arbitrary scalar automorphisms of a real line illustrate the danger of conflating isomorphism with native degree equality. These are not countermodels to the actual `H_pre` and are not promoted to deliverables.

The structured premise test fails before a faithful model is available: such simplifications discard Galois/unit actions, the particular formal quotient, global/local degree constraints, and synchronized choices. Levels 2–6 were not expanded into a new programme. No countermodel satisfying every genuine pre-xi-f premise is claimed.

**Preservation lemma: NOT ESTABLISHED.** A theorem that actual IUT objects map to a weaker abstraction is not alone enough to lift an arbitrary abstract counterexample back: a suitable realization/reflection result, or a demonstrated transfer of the very asserted inference, is also needed. None is supplied here.

**Lean used for new mathematics: NO.** Existing public source was inspected without building it. At `lana-agents/iut` commit `2d8f000457da6447fa4df4bfec7365c1a49b6384`, `Iut/Cor312/Statement.lean` defines `Corollary312Variant : Prop`; its `iff` lemma only unfolds the definition. The file explicitly distinguishes its input region and interfaces from the printed algorithm. The official `iut4-sec1` snapshot is also not a completed proof of this bridge. Challenge-template `sorry`s are not evidence of a false theorem, and no repository-wide trust claim is made from a text search.

## 9. Consequences and stop decision

Failure classification: **TYPE D — EXPOSITORY / FORMALIZATION GAP IN THIS AUDIT**. No mathematical falsehood, invalid implication, or exact globally missing premise has been established.

The numerical comparison is necessary for the corollary's written conclusion and is used in the intended IUT route to abc. This does not mean that a particular proof formulation is necessary for every possible proof of the corollary or abc, and it does not adjudicate abc itself.

Prior-art risk is high: the target is already explicit in Scholze–Stix §2.2, Mochizuki's responses and later decompositions, and LANA §9–10. The elementary conditional lemma adds no claimed novelty. Prize relevance: **none established**; there is no essential-flaw candidate here.

**Stop the bounded IUT prize attack under the user's D kill rule.** This supersedes the recovered audit's suggestion to keep expanding a specification. Do not schedule another internal IUT stage. Beal or MUX would require a separately chosen task; neither was investigated and neither is recommended as promising on this evidence.

**TARGET_NOT_YET_FORMALIZABLE_WITHOUT_LARGER_IUT_DEPENDENCY**
