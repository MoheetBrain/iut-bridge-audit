# E3d.3: the downstream contract

## Result and correction to E3d.2

A one-step **marked numerical comparison on realified semi-simplifications** is available in Remark 3.9.4(iii)-(iv). It preserves the degree of the specified native q-power without applying a logarithm to that nonunit. It does not construct an admissible IPL output or prove native-q coverage by the output family.

E3d.2 went too far in calling a relation on the determinant-morphism orbit fibers the minimum required transport. Its evidence established that sQ4 is required, not that this particular categorical encoding must be transported. Preserve that report historically, but withdraw the necessity claim in its `VERDICT.md` ("Transport needed"/"Requiredness") and `CQ4_TRANSPORT.md` ("weakest form admitted"). The fixed-presentation calculation and the conditional transport lemmas are unaffected.

The source does not authorize discarding the unit/Galois data before the marked comparison is justified: Ob7 and (ix) explicitly exclude that shortcut. The numerical result below is a necessary consistency component and a sufficient implementation of the **local degree-preservation part**; it is not a replacement for the complete closed-loop argument.

## Source lock and use of theorems

Pinned [IUT III](../../sources/primary/IUT_III.pdf): author PDF May 2020, subsequently published PRIMS 2021; SHA-256 `9a7ee3c77b1c7717210c0613eb39b6844649d0040dc3d9e1be7d544f8f91a0b9`. Printed and one-based PDF page numbers agree. This identifies the repository copy, not a claim about the current online version.

| Passage | Input or role in this derivation |
|---|---|
| Remark 1.1.1, pp.28-29; Remark 1.2.2(i),(iii), pp.36-37 | Unit-only domains; coric containment, not a commuting Kummer triangle. |
| Proposition 3.5(i),(ii), pp.103-106 | Labeled Kummer maps; finite-place inclusions for units and log pre-composites; separate splitting actions up to torsion. |
| Proposition 3.9(i)-(iv), pp.115-117 | Packet/procession normalization, global degree interpretation, and vertical compatibility. |
| Remark 3.9.4(i),(iii)-(vi), pp.120-126 | Actual quotient by integration; injective unit charts; q-power marking; finite-extension/tensor and archimedean scope. |
| Remark 3.9.5 Ob3-7, pp.131-137 | Corrected determinant, same permitted M, bounded common output hull, and retained arithmetic data. |
| Ob8, Ob9, Ob9-1, pp.137-139; cQ3/cQ4/(ix), pp.141-144 | Vertical adjustment; comparable objects; numerical quotient compatibility; asserted marked closed loop. |
| Proposition 3.10(iii), Remark 3.10.1(i), pp.149-150 | Genuine MOD comparisons; no replacement of mod by MOD. |
| Theorem 3.11(ii), pp.155-156 | Unit packets, splitting and global comparisons; final exact log-volume compatibility statement. |
| Corollary 3.12, xi-d through xi-f, pp.183-184 | Conclusion consumed, not premises for coverage. |

We accept the stated local measure identity of Remark 3.9.4(iii), its existence of an injective compact ample unit chart, and the stated Kummer/splitting and packet compatibility results as explicit source inputs. Their deeper proofs, including AbsTopIII Proposition 5.7 and the construction of all Hodge theaters, are not independently verified here. The elementary quotient calculation is proved in [LOCAL_CALCULATION.md](LOCAL_CALCULATION.md). Mathematical displays on pp.123,124,155,156,183,184 were visually checked. The retained native root convention was checked against IUT I, Example 3.2(iv), p.71.

## What the next stage consumes

Write `a=-|log(q)|`, `b=-|log(Theta)|`, with the source's normalizations. In xi-d the two objects to be compared are the downset `(-infinity,b]` and the **fixed native** value a. Comparability alone is not membership. Xi-e retains the native input constraint during the construction; xi-f consumes coverage, possibly by approximation, to obtain `a<=b`. None of those latter assertions is assumed in this derivation.

For the selected vertical step there are two distinct obligations:

1. **Numerical stability:** after the specified passage to realified semi-simplifications, the normalized degree is unchanged, and the input native q-power still has its prescribed degree. This is supplied locally below.
2. **Admissible marked attachment:** the object/value being compared must arise from the actual IPL construction with its correlated choices and native marking. The operation must not substitute an arbitrary equal-volume representative for an admissible algorithmic output. The inspected clauses assert such compatibility; its precise application to the output hull/formal family remains the semantic question.

| Strength | Type | Downstream use | Classification |
|---|---|---|---|
| A: transport all relevant determinant orbits | A family of maps/relations between `T_B(Y)` fibers, with native provenance as additional data | Could implement a structured presentation comparison | **SUFFICIENT_ONLY** when marked attachment and numerical compatibility are also proved. Necessity is **UNESTABLISHED**. An unmarked orbit relation alone does not suffice. |
| B: compare the actual marked IPL output | A witnessed comparison between the actual source output record and a target record, retaining Q, localization, choices and normalization | Supplies the required attachment without transporting every fiber | **SUFFICIENT_ONLY** as an exact representative solution; a formal/approximate version may suffice instead. Not constructed here. |
| C0: one-step degree preservation | `Phi_gamma:Rss(E_-)->Rss(E_+)`, `nu_+ Phi_gamma=nu_-`, evaluated on the given q-power marking | Implements the numerical part of Ob9 and Theorem 3.11(ii)'s last sentence | **REQUIRED** numerical consistency on the objects used; the particular Rss implementation is source-supplied and sufficient for this part. Derived below. |
| C: native-marked bound comparison | A source-witnessed relation of admissible output bounds/degrees attached to the original Q, strong enough to compare a with b | The effective numerical information consumed in xi-d/e/f | **REQUIRED** at the level of consequence; its precise source-specific witness predicate is **UNESTABLISHED** in this audit. C0 alone is insufficient. |
| D: admissible one-sided approximation | For an independently defined correlated output type A and map L, `forall epsilon>0, exists O:A, a-epsilon<=L(O)` | Together with `forall O:A, L(O)<=b`, yields a<=b | **SUFFICIENT_ONLY**, by the existing Stage 1 lemma. That exact quantifier encoding is not proved to be the source's intended formal quotient. Its hypothesis is not supplied here. |

There is thus a proved smaller route for **degree preservation**, but not a proved bypass of all marked source data. The assertion that all T_B data must be transported is corrected; the assertion that the global bridge is closed is not made.

## Signs, powers, weights, and approximation

At the selected bad nonarchimedean place set `q=underline(q)_v`, the root `q_Tate,v^(1/(2 ell))` modulo its prescribed torsion, not q_Tate itself. Set `c_v=ord_v(q) log(p_v)>0` with the source normalization. For the same permitted positive integer M used in corrected determinants, the local native ideal `q^(Mr) O_k` has normalized log-volume `-Mr c_v`. Dividing by M recovers `-r c_v`; neither M nor the sign is adjustable.

Packet weights are the positive normalized weights of Proposition 3.9(i) and Remark 3.1.1; procession normalization is the stated average, not a freely chosen weighting. Ob3 subtracts the structural-lattice determinant and uses the prescribed positive tensor powers. The source's global map is a sum with all but finitely many contributions zero (Proposition 3.9(iii)). Preserving one contribution does not establish a simultaneous global output or its upper bound.

The Stage 1 approximation lemma is only an endpoint test. We do not define A as every region or as every simple function in Rss. Nor do we define its image to be `(-infinity,b]` and then infer that the native input is in it. Attainment, a one-sided witness, and approximation remain different assertions. No inequality relating a to b follows from C0 alone.
