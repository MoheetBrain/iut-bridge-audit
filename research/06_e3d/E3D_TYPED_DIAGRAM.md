# E3d: the marked comparison and its first unconstructed edge

**Verdict: FIRST_WITNESS_NOT_SUPPLIED.** The stopping point is the native-marking rule for the formal cQ3/cQ4 presentation. The exact, single-object substitute below is typed but is **not** imposed on the source. The weaker source-specific rule has not been reconstructed. This is a reconstruction limit, not an established defect of IUT.

All page numbers refer to the pinned PDFs, and agree with their printed pages. Abbreviations: [I](../../sources/primary/IUT_I.pdf), [II](../../sources/primary/IUT_II.pdf), [III](../../sources/primary/IUT_III.pdf), [FrI](../../sources/primary/Frobenioids_I.pdf), [FrII](../../sources/primary/Frobenioids_II.pdf). `Ffull` below denotes III's full, globally realified split-×μ-Kummer prime-strip; `Funit` denotes its unit prime-strip. This avoids confusing the several similar source superscripts.

## Q is a marked native realization

Fix the initial Θ-data and an LGP-Gaussian log-theta-lattice of III Theorem 3.11. Use columns 0 and 1, and native codomain coordinate (1,0). Let

`Q = (Hq,•, 0, ι : P ≅ Ffull(Hq,0))`.

Its mathematical type is a **marked vertical column of Θ±ell NF-Hodge theaters**, with a distinguished coordinate and an isomorphism from the fixed full strip P to the native constant strip there (II Corollary 4.10(i), Definition 4.9(viii); III Definition 3.8). Tuples are considered up to isomorphisms of this entire marked data. Q is given by the actual codomain column, not reconstructed from P by an assumed inverse functor. Only the following restrictions of the tuple are used:

| Level | Data and actual typing |
|---|---|
| 0: full abstract P | `(C_P, Prime(C_P)≅V, {F_P,v}, {ρ_P,v})`. C_P is global realified; F_P,v is split-×μ-Kummer at finite v and the specified torsion-quotient inductive system at archimedean v. The ρ identify the global prime divisor monoids with local realified divisor monoids. Conditions (a)–(f) of I Definition 5.2(iv), pp.134–135, are incorporated by II Definition 4.9(viii), p.158. P already has an abstract pilot object up to isomorphism. |
| 1: retained coric data | The D/Funit data, local Galois groups, Kummer unit structures and mono-analytic log-shells. At finite v, κ is an Ism-orbit `O×μ(G_v) ≅ O×μ(A_v)`, equivalently the collection of submodules `I_H^κ` for open H≤G_v (II Definition 4.9(i), p.154). At infinity use the compatible surjections with N-torsion kernels, modulo the stated order-two ambiguity (II p.157). Coricity does not identify all Frobenius-like realizations. |
| 2: native Q | The actual native holomorphic realizations in Hq,0 and their vertical log-links: local fields/rings, the rigidifications `Π_v ↠ G_v`, and the native multiplicative realization of the splitting and units, plus the native global realified Frobenioid and its localization data. In particular, at bad v the splitting generator is realized as `q̲_v = qTate,v^(1/(2ℓ))` modulo μ₂ℓ, not as qTate,v (I Example 3.2(iv), p.71). Units and splitting belong to the **same** multiplicative structure (III Ob7, pp.135–137). |

For example the bad-place marking contains the monoid map

`s_q,v : N → k_q,v^×/μ(k_q,v),   r ↦ [q̲_v^r]`,

with the native unit realization beside it. The global q-pilot `L_q ∈ Ob(C_q,g)` is determined up to isomorphism by these splitting generators and the native ρ (III Definition 3.8(i), p.112). Here C_q,g is the global realified Frobenioid; C_q below is the category of local-global collections. Write `q_M` for the collection of the degree-M naive-Frobenius image of L_q, the corresponding native local objects, and their localization isomorphisms. Roots, positive powers, signs, and normalization are recorded; they are not free rescalings of Q.

## One principal diagram

Here `b_i,u_i,k_i` have the types in the arrow key below. `θ` is a full poly-isomorphism; its inverse means the family of inverses. Unmarked arrows below the strip diagram are operations on presentations, not isomorphisms of strips.

```text
Q=(Hq,•,0,ι) ── native realization ──► (P_q, s_q, L_q, ρ_q)
                                           │ forget Level-2 marking only
                                           ▼
                                         P_q
                                           │ θ⁻¹ : full poly-isomorphism
                                           ▼
                  F_env^(0,0) ─b₁→ F_gau^(0,0) ─b₂→ F_LGP^(0,0) ─b₃→ F_lgp^(0,0)
                      │ k_env           │ k_gau          │ k_LGP          │ k_lgp
                      ▼                 ▼                ▼                ▼
                  F_env^(0,◦) ─u₁→ F_gau^(0,◦) ─u₂→ F_LGP^(0,◦) ─u₃→ F_lgp^(0,◦)
                      [IPL traverses b₂⁻¹,b₁⁻¹,k_env,u₁,u₂,u₃]
                                           │ Theorem 3.11(i)–(iii):
                                           │ multiradial representation in column 1
                                           ▼
                      bounded admissible family B of possible regions P_β
                                           │ φ, then corrected det^(⊗M)
                                           ▼
                                H_B ; D_B ; (C_B ─U_B→ C_q)
                                           │ log-Kummer correspondences, cQ4
                                           ▼
                      family of shifted/root presentations of this pair
                                           │
                                           ╳ W*: native-marked IPL descent rule
                                           │ NOT CONSTRUCTED; see below
                                           ▼
                      output presentation with its returned pilot marking
                      related to the ORIGINAL (s_q,L_q,ρ_q)

Constructed beside the last two rows: C_B ─U_B→ C_q ←q_M─ {*}
This span is not, by itself, the missing marked return relation.
```

The vertical Kummer arrows in the printed III p.152 diagram point **up** from the Frobenius-like lower row to the étale-like upper row. The diagram above places those rows in the opposite vertical order, so its `k` arrows point down with exactly the same domains and codomains.

| Arrow/operation | Exact kind, source and preservation |
|---|---|
| θ: F_LGP^(0,0) → P_q | Full poly-isomorphism of full strips, III Definition 3.8(ii), p.113. Preserves the complete abstract strip tuple, hence abstract pilot. Not a ring isomorphism between the two columns. |
| b₁: env → gau | Evaluation **isomorphism**, II Corollary 4.10(ii), p.159, passed through Definition 4.9. |
| b₂: gau → LGP; b₃: LGP → lgp | Tautological full-strip isomorphisms, III Proposition 3.7(iii),(iv), pp.110–111; III Remark 3.10.2, p.152. |
| k_env: F_env^(0,0) → F_env^(0,◦) | Induced Kummer isomorphism, III Proposition 2.1(ii), with its projective-system data as in (iii)–(v); identified explicitly in Remark 3.10.2. |
| k_gau,k_LGP,k_lgp | Induced Kummer isomorphisms, III Proposition 3.10(i), pp.147–148. |
| u₁: env → gau | Étale-like evaluation isomorphism from II Corollary 4.6(iv),(v), as specified by III Remark 3.10.2. |
| u₂,u₃ | Natural isomorphisms of III Proposition 3.10(i). For each square, `u_i k_i = k_(i+1) b_i` as full-strip maps. This is genuine commutativity, not commutativity of the whole log-theta-lattice. |
| Representation in column 1 | Theorem 3.11(i): functorial representation of (a) modules, (b) splitting-monoid actions, (c) global data, modulo Ind1/2; (ii) adds Ind3; (iii)(c),(d) gives the stipulated equivariance of Kummer/evaluation constructions. Not a set map carrying one actual region across θ. |
| φ and determinant | III Remark 3.9.5(i)–(vi), Ob3–5, pp.127–134. On a bounded admissible B, `H_B=φ(B)` and `D_B=det^(⊗M)(H_B)`. Component weights, inverse determinant of the structural lattice, and stack twists are essential. `det^(⊗M)(O⊗L)=L^M`. No inverse to φ is used. |
| U_B: C_B → C_q | The **forgetful functor** of the two cQ3 categories, III pp.141–142. Forgets structure polymorphisms, retaining local/global objects, pullback actions and localization. Its direction is from the upper category to the ambient category. |
| cQ4 | III Theorem 1.5(i),(iii), Proposition 3.5(ii), Theorem 3.11(ii); III cQ4 p.142. Isomorphisms on appropriate Galois/étale-unit data; Frobenius-like unit comparisons modulo log iteration. Finite-place inclusions and archimedean surjections remain relations on their stated domains. Ind3 is not made a group action. |

For cQ3 the definitions are explicit:

`C_B,v = { (X_v,[a_v:X_v→D_B,v]) : deg_Fr(a_v)=1 }`,

where `[a_v]=Aut(D_B,v)·a_v` by **postcomposition**, and a morphism `f:X→Y` satisfies `[a_Y f]=[a_X]`. Then

`C_B = { ((X_v,[a_v])_v, X_g, (ρ_v: rlf(X_v) ≅ loc_v(X_g))_v) }`.

The ambient category C_q has the same data without `[a_v]`. Its local categories include the archimedean systems, not just a finite-place algebraic model. The source calls this **pair** a formal quotient; no universal categorical quotient is required here.

## Exact boundary for W*

A fully typed *exact-representative test* would be an object of

`Fib_q(U_B) = { (X,η) : X∈Ob(C_B), η:U_B(X)≅q_M in C_q }`.

It consists of the actual linear-map orbits, η_v, η_g and the equations

`loc_v(η_g) ∘ ρ_X,v = ρ_qM,v ∘ rlf(η_v)`.

This is **not** asserted necessary or sufficient for E3d: it can demand an exact representative where a formal family suffices, and without tracking the IPL pilot marking it can merely give an unrelated ambient comparison. No failure to construct this test is counted as an IUT gap.

**W\*** is instead the source's **marked, diagrammatic version of the return relation**: apply its permitted hull-approximant/formal-intersection, tensor-root and log-Kummer operations to the actual IPL output, and specify how the returned splitting/pilot marking is related to `(s_q,L_q,ρ_q)`. In an exact representative its bad-place equation would be `s_return,v(r)=[q̲_v^(Mr)]`, with the displayed localization square; in a formal presentation these must be represented as source-allowed relations, not forced into equalities of regions.

**First unresolved type dependency:** cQ3 specifies C_B, C_q and hence U_B, but the audited argument does not provide a reconstructed rule for the *marked* image/restriction in this formal pair. Consequently the index/arrow data for that weaker W* have not been obtained. Writing `q_M in the formal image of the IPL output` does not fill this dependency. Neither choosing a universal quotient nor inventing a topology of approximation would repair it faithfully. [E3D_PROOF.md](E3D_PROOF.md) stops here.
