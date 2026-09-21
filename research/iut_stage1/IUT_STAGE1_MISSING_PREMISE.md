# Missing-premise gate: no exact IUT P* established

Prepared by **Astra (Codex)**, 2026-09-21.

**P_STAR: NOT_IDENTIFIED_AS_A_SOURCE_FAITHFUL_PROPOSITION**
**P_STAR_SOURCE_STATUS: UNABLE_TO_DETERMINE**

The bounded audit does not establish `H_pre ⊬ C_xif`. Its full structured antecedent is not reconstructed. Consequently it cannot claim that a single precise extra premise is necessary, missing from IUT, or the weakest useful addition.

## 1. Exact conclusion versus an incomplete interface

In the finite case of III Corollary 3.12, let `a = −|log(q)|`, `b = −|log(Θ)|`, and `OutVol = {t : ℝ | t ≤ b}`. Then `C_xif := a ∈ OutVol` unfolds to `a ≤ b` (**DEFINITIONAL_EQUALITY**).

To state a nontrivial coverage lemma one would first need a source-faithful type `A` of allowable structured outputs and a normalized log-volume map `L : A → ℝ` (**MAP**). In particular `A` must retain the local/global quotient construction, Galois/unit actions, allowed correlated indeterminacies, and prescribed q realization. These are not optional metadata.

The registry deliberately marks this `A` and `L` as unresolved interfaces. Neither is defined by simply declaring `IMAGE(L,A) = OutVol`.

## 2. Three scalar candidates in a specified abstract interface

Suppose independently that `A`, `L`, `a`, `b` are specified, with

```text
UB := ∀ x : A, L(x) ≤ b.
EQ := ∃ x : A, L(x) = a.
GE := ∃ x : A, a ≤ L(x).
APX := ∀ ε : ℝ, ε > 0 → ∃ x : A, a − ε ≤ L(x).
```

Relation types: EQ uses **PROPOSITIONAL_EQUALITY**; GE and UB use **INEQUALITY**; APX uses **APPROXIMATION**, here defined exactly by the displayed quantified inequality.

`EQ ⇒ GE`: equality implies the weak inequality.
`GE ⇒ APX`: use the GE witness for each positive ε and `a−ε ≤ a`.
`UB ∧ APX ⇒ a ≤ b`: if `a>b`, take ε=(a−b)/2 and contradict UB with the APX witness.

These implications have elementary proofs. They do not establish any of EQ, GE, APX for the IUT construction. Under UB, EQ and GE need not be necessary for `a≤b`: when `A=ℕ≥1`, `L(n)=−1/n`, and `a=b=0`, APX holds while EQ and GE fail. This example distinguishes scalar predicates; it is **not** an IUT countermodel and does not remove arithmetic structure from `H_pre`.

APX is a weaker sufficient member of this small candidate list, not a globally weakest additional proposition. No exhaustive minimization over a source-faithful predicate language has been completed. An unrestricted “weakest sufficient hypothesis” such as `H_pre → C_xif` is an unhelpful repackaging of the target.

## 3. Why the down-set shortcut is circular

If `A` is defined to be the subtype `{t : ℝ | t ≤ b}` and `L` its inclusion into ℝ, then UB is automatic and

```text
APX ↔ a ≤ b.
```

The forward implication is the proved conditional lemma. For the reverse implication, if `a≤b`, choose the subtype element `a` for every ε. Thus postulating APX in this interface merely postulates the numerical conclusion in another form (**EQUIVALENCE**). It is not evidence for an exact missing structural premise.

Similarly, replacing the output bound by a stipulated finite supremum does not solve the task. For a nonempty bounded-above image, the least-upper-bound property gives `APX ↔ a ≤ sup IMAGE(L,A)`. Such a formulation is useful only if the source-faithful family and its compatibility were already constructed independently.

## 4. What the inspected source actually supplies

| Source | Relevant content | Audit consequence |
|---|---|---|
| III Remark 3.9.5(v)–(ix), pp. 128–144 | Quotient formalism, hull approximants, normalized determinants, local/global categories, cQ3/cQ4, then closed joint q/Θ structure | There is an explicit claimed route. It is inaccurate to say that the text never addresses the issue. Its precise formal quotient interface remains unexpanded here. |
| III Remark 3.11.1(iii)–(v), pp. 160–164 | Operation-induced IPL, SHE, APT; actual prime-strip input and structured outputs | Mere isomorphism or executability is an insufficient replacement for these assertions. |
| III Corollary 3.12 xi-b–g, pp. 181–185 | Fixed q input, hull/determinant/log-volume comparison, then membership | Xi-f and xi-g cannot be recycled as independent pre-xi-f premises. |
| Comments C12–C14/C17, pp. 5–6 | Distinction between abstract pilot normalization and arithmetic scale; rejection of the scalar identification | A normalization choice requires an explicit relation, not a silent equality. |
| Essential Logical Structure §3.10, pp. 144–156 | Fixed gluing, enlargement, log-shift symmetrization, joint structure in a numerical container | A stronger structured explanation exists; translating it into APX requires work not completed here. |
| Alien Copies §3.11(v), pp. 143–146 | Joint q/Θ structure and the necessity of retaining unit and value data | An abstraction discarding those data does not qualify as faithful. |
| April 2026 Formalization, pp. 10–11 | HDD=(hull+det)∘descent and final SHE+IPL comparison | Moving the construction into “3.11.5” is not an independent proof of its complete interface. |
| Scholze–Stix §2.2; LANA §§9–10 | Different formulations of the disputed numerical step | Their equivalence is not proved in this audit. LANA's report says its own comparison (9-1) is unproved at that time. |

The [source map](IUT_STAGE1_SOURCE_MAP.md) distinguishes directly re-read passages from recovered dependency pointers. The recursive chain through Frobenioid and log-Kummer constructions was not exhaustively checked. Therefore the correct source status is **UNABLE_TO_DETERMINE**, not NOT_FOUND, CIRCULAR, or ONLY_EXPLANATORY_PROSE for a purported exact P*.

## 5. Decision

No exact source-faithful P* has been isolated. Necessity, source absence, and formalization readiness have not been established. A proposed Lean structure with an APX field would certify only the elementary conditional statement above; it would not settle IUT. No such file was created.

The missing interface triggers outcome D and the requested stop rule. This file is a record of the boundary, **not a new lemma programme or an invitation to expand the task**.
