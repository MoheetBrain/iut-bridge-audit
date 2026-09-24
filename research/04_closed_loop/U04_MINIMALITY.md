# U04 minimality audit

**Verdict: GLOBAL LIFT NOT REQUIRED by the printed route examined here.** The earlier audit's demand for a globally selected structured map `f` was over-strong. This corrects the audit, not the source. It does not establish that no such map exists, or certify every underlying reconstruction theorem.

The controlling text is the pinned **LANA_TEX**, lines 1966–2017. The pinned PDF **LANA** is a separately versioned artifact: its §6.2(g)–(h), pp.35–36 and schematic §9.1(f)–(g), p.45 must not be silently assigned the TeX's numbering. In particular, the English word “factors” and a schematic dashed arrow do not, on their own, specify a canonical or homomorphic section.

## Relation first

Write `C_v=(ell Delta_Theta)(Pi_v)` and `H_v=product_t infty H1(D_t,C_v)`. The detailed text obtains synchronized D_t-module isomorphisms `iota_t:C_v -> Lambda(Kbar_v,t)` from the mono-theta environments omitted in the exposition. It defines

`phi_v,t=(iota_t^-1)_* kappa_t`, and `phi_v=product_t phi_v,t`.

Here the domain of `phi_v` is the product of actual local monoids belonging to `Psi_cns(F_succ)_t`, not an unconstrained product of abstract copies. The theta evaluation map `psi_v` has codomain `H_v`. The explicitly displayed realization assertion is

`im(psi_v) subseteq im(phi_v)`.

The least existence content of this assertion is the totality of the relation

`R_v={(m,x): psi_v(m)=phi_v(x)}`

over its first coordinate. Surjectivity of this projection requires no section. An arbitrary choice function, even if available set-theoretically, would add nothing to the recorded image assertion and would not automatically be compatible with monoid operations, Galois actions or the prime-strip data.

The subsequent text strengthens the relevant realization statement to

`im(psi_v^Frob)=phi_v(G_v)`

for the **specified Gaussian monoid** `G_v` in that container [LANA_TEX lines 1996, 2009–2017]. The source describes its splitting only roughly as `((q_v^(t^2))_t)^N` times diagonally embedded units. That shorthand is not a complete definition of saturation, torsion quotients or splitting choices. We therefore use the source object, rather than promote the rough formula to an exact definition. Its relation `R_v^G` projects onto the Frobenioid theta monoid conditional on this asserted image equality.

## Answers to the six checks

1. **Function f asserted?** The detailed Step 6 gives maps into a common cohomology object and an image containment. The schematic η discussion suggests realization/factorization but does not specify a selected global `f` with a stated structure class. No such selection is used by the detailed Step 7 route.
2. **Monoid homomorphism f asserted?** No homomorphic section or lifting theorem of that form is stated in the inspected passages.
3. **Only image containment?** This is the explicit Step 6 assertion, but not the whole Step 6–7 account.
4. **Equality of specified images?** Yes: the Frobenioid theta image and the Gaussian-monoid image under `phi_v` are asserted equal.
5. **Discrete action without individual preimages?** Yes, as a source reconstruction: the specified Gaussian splitting supplies a discrete N-part embedded in the realization monoids, and the text reconstructs its natural action on the MF log-shells. Bare equality of images of arbitrary maps would not suffice to prove this; the actual Gaussian splitting and realization are essential.
6. **Later dependence on coherent selection?** None found in the inspected Steps 7–9. They use the realized actor, field/log-shell embedding, container and suitable region. No later formula evaluates a chosen `f(m)` for every theta-monoid element.

Thus **Step 7 requires the source-compatible Gaussian actor and its shell action**, with the synchronized image comparison identifying it as the relevant theta realization. It does not require the audit's independently postulated global lift. The separate discrepancy between ordinary H1/inductive-limit H1 and between barred/unbarred realizations remains a domain-reconciliation issue; the correction does not erase it.

## Replacement U04

Replace “construct a coherent section/factorization” with:

> Reconstruct the specified synchronized Gaussian realization and discrete splitting action, checking the source's image equality and the passage from that actual splitting monoid to the labeled MF-shell action, including torsion and prime-strip compatibility.

The weakest **explicit Step 6 proposition** is image containment. The weakest package **actually used by the printed Step 7** also includes the specified Gaussian image equality and its source-structured action. This audit does not claim a logically weakest axiom for all of IUT.

The active M09, CH07 and U04 records are corrected; C024 retains the old sentence with an explicit supersession notice. See [STEP6_RELATIONS.csv](STEP6_RELATIONS.csv). No replacement Lean bridge axiom has been introduced.
