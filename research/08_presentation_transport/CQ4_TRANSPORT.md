# cQ4: a log-Kummer correspondence is not yet an orbit transport

**First required transport not reconstructed: γ_log^det**, the passage from the source's log-Kummer comparison of output realizations to a comparison of the cQ3 structure-morphism orbits in those realizations. This is a bounded reconstruction result. No nonexistence theorem or IUT flaw follows.

The source does provide relations and some genuine isomorphisms. The missing item is their induced action or relation on T_B, even allowing a relation instead of a function. The existence of lower-level relations alone therefore does not resolve this task as SOURCE_TRANSITION_IS_RELATIONAL_NOT_FUNCTORIAL.

## 1. Exact source data for one vertical change

Fix the native column n=1 of the given LGP-Gaussian lattice. Consider an adjacent log-link from the theater at m to the theater at m+1. Keep Q at its original distinguished coordinate; do not change Q to absorb the output indeterminacies. Let B_- and B_+ denote admissible hull/determinant presentations at the two realizations, with a common permitted exponent M. No equality of their hulls is presumed.

At the unit/module level, [III](../../sources/primary/IUT_III.pdf) Proposition 3.5(i),(ii), pp.103–106, supplies the following precise data. For each allowed packet index j and each v|v_Q, use the labeled monoids Ψ_cns(n,m F)_|t|, |t|∈{0,…,j}, their unit portions, and the corresponding coric packet `I(S_(j+1)^± F(n,◦D)_vQ)`. Kummer maps are the monoid isomorphisms of 3.5(i), not maps chosen solely from equality of log-volumes.

| Component | What the source actually supplies | Limit of the asserted type |
|---|---|---|
| Local Galois/Π rigidification | Vertical full poly-isomorphisms of D-Hodge theaters, Theorem 1.5(i), pp.48–49; the quotient rigidifications retained in Remark 3.9.5(ix), p.143. | They identify these group-theoretic structures; a rule on every linear Y_v→D_B,v is not part of that record. |
| Étale/Frobenius-like units | Kummer comparisons and the bi-coric unit strip, Theorem 1.5(iii), pp.49–50; cQ4, p.142. Auxiliary Kummer structures remain attached. | Frobenius-like unit comparisons must retain the allowed log iterates. |
| Finite places | 3.5(ii)(a), pp.104–105: both the tensor Kummer images of Galois-invariant unit data and the images after permitted log iterates lie in the coric packet. | Common containment, not equality of the two images or an inverse to a logarithm. |
| Archimedean places | 3.5(ii)(b), p.105: the specified closed balls contain subsets surjecting, by the relevant iterate, onto the unit subset on which that iterate is defined. | Retain the covering subset and surjection; there is no chosen inverse. |
| Splitting monoids at bad places | 3.5(ii)(c), pp.105–106, and Theorem 3.11(ii)(b), pp.155–156: the stated actions are compatible modulo roots of unity. | A compatibility of these splitting actions, not a computed returned native splitting through the determinant-orbit comparison. |
| Global data | Proposition 3.10(iii), p.149, gives mutually log-compatible MOD Frobenioid isomorphisms and the associated LGP split portion; Theorem 3.11(ii)(c), pp.155–156, records the global realified versions. | Do not omit this positive result. It does not by itself supply the local structure-map orbits with which to assemble a cQ3 upper tuple. |
| mod versus MOD | Remark 3.10.1(i), pp.149–150, explains why the corresponding log-compatible mod isomorphisms cannot be obtained in the same manner; Theorem 3.11(ii) explicitly distinguishes them. | One cannot use the MOD isomorphism to assert unrestricted precise transport of the additive local-ideal presentations. |

Remark 1.1.1, pp.28–29, fixes the domain conventions: log iterates concern local units, with the stated archimedean semi-germ interpretation. Proposition 1.2(iv),(x), pp.31,34, and Remark 1.2.2(iii), pp.36–37, distinguish the log-linked graph with a coric vertex from a commuting triangle of Kummer identifications. These are exact dependencies cited by Proposition 3.5. They explain why replacing the log edge by a composite of Kummer isomorphisms changes the edge under audit.

## 2. The orbit-level datum sought

For already specified local/global collections Y_-∈C_q,B_- and Y_+∈C_q,B_+, put

`S_-=∏_v Aut(D_-,v)\Hom_lin(Y_-,v,D_-,v)`,

`S_+=∏_v Aut(D_+,v)\Hom_lin(Y_+,v,D_+,v)`.

The weakest form admitted by this test is a source-derived relation

`R_log,Y-,Y+ ⊆ S_- × S_+`,                                   (L)

with representative independence, the relevant local/global compatibility, and a specified law for consecutive log comparisons. Its orientation follows the actual source correspondence. Taking the opposite of a relation when expressing a return condition does not invert a map. The relation must concern the actual IPL/pilot-associated collections; a nonempty relation between unrelated objects is insufficient. Selecting their permitted comparison is itself part of the required construction, not assumed from their having the same abstract strip.

One **sufficient**, stronger realization of (L) would be a compatible ambient functor F:C_q,B_-→C_q,B_+ and linear arrows `h_v:F_v(D_-,v)→D_+,v`. Section 3 of [ORBIT_TRANSPORT.md](ORBIT_TRANSPORT.md) would then give an orbit relation without requiring equivariance (E); with (E), it would give a function. Neither this sufficient form nor a function on all ambient objects is imposed on the source. A directly defined relation at the actual IPL collections would suffice.

## 3. Attempt and first unsupplied component

Start with a local linear morphism `a_v:Y_-,v→D_-,v`. The source unit correspondence relates portions of multiplicative monoids, their log images, and packet actions. Applying a logarithm to a_v is not a typed operation on these Frobenioid Hom sets. Nor does taking the determinant apply to an arbitrary partial set map. The corrected determinant acts on the specified arithmetic hull/vector-bundle data. A rule connecting those two operations on the actual orbit representatives is the missing component.

Granting the available Galois/unit comparisons and global MOD isomorphism does not fill that component. Even if an ambient reindexing functor is separately chosen from appropriate arithmetic realizations, one must still compare the **actual output determinant objects** and the images of the actual linear maps, or construct (L) directly. An isomorphism of transported targets supplied by the abstract functor is not automatically the determinant comparison supplied by the log-Kummer algorithm.

The first unresolved question can thus be written concretely: what subset of pairs of classes in (L) is assigned by the given adjacent log-Kummer comparison, and why is that assignment unchanged when a_v is replaced by σ_v a_v? The checked source gives no completed answer in this reconstruction. We consequently cannot claim local linearity, naturality, localization compatibility and iterated composition for (L). The generic orbit-saturation lemma cannot help until an actual Hom-level comparison is supplied; saturating arbitrary pairs would erase the marking constraint rather than prove it.

Formal intersections at empty log domains are part of this same issue. Remark 3.9.5(v) preserves their unevaluated set expressions after collapse. It does not in this reconstruction assign them maps of determinant lines. We do not evaluate an empty expression and force it into the finite-volume hull domain.

## 4. Requiredness, weaker relations, and limits of the verdict

This transition is genuinely present in the route: Ob8, pp.137–138, identifies the output's vertical shift; sQ4, pp.139–141, performs its adjustment; cQ4, p.142, states the retained unit/Galois compatibility; (ix), pp.143–144, explicitly includes sQ4 before taking coarse log-volume invariants. Ob9-1, pp.138–139, says the formal indeterminacies retain comparability. These clauses are respected as the construction to reconstruct, not used as a substitute for (L).

The strongest obtained transport is the exact unit/module correspondence and the separately specified splitting/global MOD comparisons above. A weaker-than-functional **orbit relation** could suffice, but it has not been constructed here. No conclusion is drawn from failing to find a function, an exact region, or a universal limit.

Decision: **RETRY this dependency**, not an arithmetic-geometry escalation yet. The relation's endpoint sets and its necessary role are explicit, but the minimal source-derived relation at the actual IPL marking is not fully specified. There is no fully formulated source-minimal theorem whose failure has been proved. Remark 3.12.2(ii) and xi-f have not been used as premises.
