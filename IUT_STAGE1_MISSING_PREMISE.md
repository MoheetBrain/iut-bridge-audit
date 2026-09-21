# Candidate bridge and the unresolved source-faithfulness obligation

Prepared by Astra (OpenAI Codex), 21 September 2026.

This filename is part of the requested deliverables. It is **not** a finding that IUT has a missing premise. The selected outcome remains **TARGET_NOT_YET_FORMALIZABLE_WITHOUT_LARGER_IUT_DEPENDENCY**.

## 1. What has a stable type

In the finite case let `a = qVol : ℝ`, `b : ℝ`, and `OutVol = {x : ℝ | x ≤ b}`. The last relation is DEFINITIONAL_EQUALITY. The intended conclusion is MEMBERSHIP `a ∈ OutVol`.

For a separately justified admissible-output type `A` and normalized map `L : A → ℝ`, define

\[
UB(A,L,b):=\forall O:A,\ L(O)\le b.
\]

The quantifiers in `A` must include the actual constraints on choices and constructions. They cannot mean arbitrary regions, arbitrary isomorphisms, or independently chosen local representatives when the source requires correlation.

The following are three different candidate bridges:

\[
P_{=} := \exists O:A,\ L(O)=a,
\]

\[
P_{\ge} := \exists O:A,\ a\le L(O),
\]

\[
P_{\mathrm{approx}} := \forall\varepsilon\in\mathbb R_{>0}\;\exists O:A,
\quad a-\varepsilon\le L(O).
\]

`P_=` uses PROPOSITIONAL_EQUALITY of normalized reals; `P_≥` uses OTHER_EXPLICITLY_DEFINED_RELATION, the stated real order; `P_approx` uses APPROXIMATE_RELATION, defined by the displayed quantified formula. None is an untyped assertion of correspondence.

## 2. The sufficient order argument

`P_= ⇒ P_≥ ⇒ P_approx`. Under `UB`, each implies `a ≤ b`.

For the weakest of these three witness conditions, suppose `a > b` and set `ε = (a-b)/2 > 0`. Then `P_approx` supplies `O` with

\[
L(O)\ge a-\varepsilon=(a+b)/2>b,
\]

contrary to `UB`. This proof does not require attainment of a supremum or equality of representatives.

The witness conditions can differ. As examples of these elementary formulas only, take `a=0`:

- A single output of volume `1`, with `b=1`, satisfies `P_≥` but not `P_=`.
- Outputs `L(n)=-1/(n+1)` for natural numbers `n`, with `b=0`, satisfy `P_approx` but not `P_≥`.

These are **not countermodels of IUT** and are not used as abstractions of it. Their only purpose is to justify declining to demand exact attainment when approximation may suffice.

## 3. Why this is not an unconditional weakest P*

Let `Q` be `a ≤ b`. In unrestricted logic, any `P` satisfying `H ∧ P ⇒ Q` entails `H ⇒ Q`. Thus `H ⇒ Q` is a weakest sufficient condition, and under `H` it is equivalent to Q. This supplies no substantive proof and is prohibited as a replacement axiom.

To obtain a useful weakest bridge one must first specify:

1. the actual typed theory `H_IUT`;
2. the allowed language of bridge predicates;
3. what counts as an admissible realization, order comparison, or approximation;
4. the equivalences among representations that have already been proved.

Those choices are not settled in this audit. `P_approx` is the weakest **of the three displayed witness conditions**, not a theorem asserting a globally weakest noncircular IUT premise.

For example, if `A` is nonempty and `b = sup {L(O) | O : A}` is already justified as a finite least upper bound, then

\[
P_{\mathrm{approx}}\iff a\le b.
\]

The reverse direction follows from the defining supremum property applied below `b`. In that setting, assuming `P_approx` could simply rename the conclusion. A legitimate source proof must derive it from the structured construction. Also, an arbitrary upper bound `b` need not equal this supremum, so the reverse implication cannot be used without that additional hypothesis.

Equivalently, where the real image and closure are defined, `P_approx` says that `a` lies in the downward closure of the topological closure of `L(A)`. This is a scalar interpretation to be justified, not a replacement definition of the source's formal quotient.

## 4. Strongest relevant source evidence

The following locations must be included in a fair reconstruction:

- **IUT III, Remark 3.9.5(ix), pp. 141–144:** the construction through (sQ3)/(sQ4), with (cQ3)/(cQ4), explicitly asserts return through the right-column structure before discarding unit information at (sQ5).
- **IUT III, Remark 3.11.1(iii)–(viii), pp. 160–166:** IPL, SHE, APT, and the distinction between insufficient isolated interpretations and their intended combined use.
- **IUT III, Corollary 3.12, xi-d/e, pp. 183–184:** determinant and normalized volumes; execution subject to the native q-pilot constraint.
- **Essential Logical Structure, §3.10, Stp7–Stp8, pp. 151–156:** vertical-index treatment and intended simultaneous preservation; §3.11, pp. 163–164, further discusses reconstruction and gluing data.
- **Alien Copies, §3.11(v), pp. 143–146:** explanation in terms of the full prime-strip data and retained q/Θ structures.

The April 2026 discussion at pp. 10–11 reorganizes the target through the informal “3.11.5” interface. It does not supply an independently checked public derivation of that interface in the evidence inspected here. LANA §9.2, p. 46, proposes a precise-looking equality of two comparison maps but leaves the source-faithfulness and admissibility translation to be justified.

**Search category: FOUND_ONLY_AS_INFORMAL_EXPLANATION.** This categorizes the candidate preservation bridge as established **in this audit**. It does not downgrade every prose proof to non-proof, certify a circular argument, or assert exhaustive absence from all cited literature. Relevant assertions were found; their full mathematical dependency proof remains uncompleted here.

## 5. Exact proof frontier

The unresolved requirement is not merely existence of an isomorphism between prime-strips. It is the effect of the **specified composite and formal output construction** on a fixed native input realization, after permitted indeterminacies and before/through scalar normalization.

A faithful formulation should make the following data explicit:

- the input prime-strip and its distinguished pilot, with native right-column arithmetic realization;
- local Galois/unit/Kummer structures and their compatible localization into the global realified Frobenioid;
- the operation-induced poly-isomorphism composite;
- the correlated admissibility predicate for Ind1–Ind3;
- hull and positive-power, twisted determinant operations with their descent data;
- the formal quotient's objects and morphisms, rather than a guessed set quotient;
- the one-step vertical reconciliation and its normalization on volumes;
- the comparison between resulting output possibilities and the native input degree.

The needed conclusion about that data is an admissible degree coverage property sufficient for `P_approx`, or another property proved sufficient without strengthening the source. It is not yet legitimate to call this the exact absent IUT premise: its source-faithful type and its derivation from the cited categorical construction remain unresolved.

Two invalid shortcuts are excluded:

1. Turn the source's construction-level preservation assertion into an axiom `a ≤ b`, then claim success.
2. Delete that assertion, retain only bare isomorphism, produce a scalar counterexample, then claim failure of IUT.

## 6. Countermodel acceptance condition

An acceptable abstraction needs an interpretation of **each** premise and construction, including the asserted closure property, together with proofs of preservation. To transfer a particular abstract failure to the actual IUT claim, it also needs a realization or reflection argument. A forgetful passage from actual models to abstract models alone does not guarantee that the chosen counterexample is realizable.

No candidate reached this acceptance threshold. In particular, replacing the retained structured data by scalar-linear rescalings is not licensed by the inspected source definitions.

## 7. Lean and stopping decision

No Lean skeleton is supplied, because its essential source-faithfulness hypotheses would currently be names for the unresolved work. The proved elementary implication `UB ∧ P_approx ⇒ a ∈ OutVol` is recorded above without implying a formalization of IUT.

The recommended next action is a bounded specification/review of Remark 3.9.5(ix)'s formal quotient and native-pilot preservation, not a new abc proof attempt. It has not been started. There is no faithful countermodel, verified critical bridge, demonstrated essential omission, or prize-relevant flaw result in this audit.
