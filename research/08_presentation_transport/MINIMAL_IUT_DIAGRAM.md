# The recovered finite fragment

No complete J_IUT or Y_IUT is declared: the prerequisite of recovering all required orbit transports is not met. What follows is a finite fragment of the actual source route, with its available types distinguished. It is not a new universal FormalSys.

## 1. Dependency-ordered route

1. **IPL strip isomorphisms (S0).** Retain the actual full-strip path from native P_q through the inverse Θ-link representative, the inverse lower evaluation/tautological isomorphisms, and the Kummer/coric isomorphisms of III Remark 3.10.2, pp.151–152. These are the maps retained in [E3d](../06_e3d/E3D_TYPED_DIAGRAM.md).
2. **Common possibilities and hull (S1).** In the fixed codomain realization, retain the bounded admissible family P_B of possible output regions, including the stipulated Ind1/2 choices, and form H_B. III (vi), Ob5–6, pp.130,134–135, uses this common family to avoid choosing one possibility.
3. **Corrected determinant at a chosen M (S2).** Apply Ob3, pp.131–133, with its weights and structural-lattice correction. This introduces D_B and the cQ3 orbit presheaf; it is not a map from an already defined T on arbitrary regions.
4. **cQ3 category pair (S3).** Form `C_B≅∫T_B → C_q,B`, retaining local/global data, unit/Galois structures and localization. Formal collapse is represented here by the given pair and its forgetful operation, not by an inverse or essential-surjectivity assertion.
5. **cQ4 vertical adjustment (S4).** Compare the shifted output realization with the native column using the source log-Kummer correspondences. The unit/module/global fragment is recovered; the induced relation on T_B is the first required unsupplied transport.

Conditional branches, not additional mandatory steps: A1 changes M to dM by the forward power functor; A2 compares supplied rooted presentations over a common powered one; A3 treats an actual admissible hull/enclosing-region inclusion. Their formulas and limits are in ORBIT_TRANSPORT. Root extraction is avoidable by remaining at M as in Ob4. Enclosing systems are needed only when the more general domain of Remark 3.9.7 is used. There is no requirement to arrange all seven candidate classes into a chain of equivalences.

## 2. Exact strip fragment

Using E3d's b_i,k_i,u_i notation, each arrow below is a full-strip isomorphism and each square commutes. The arrows are drawn with the same upward Kummer direction as the pinned III p.152 diagram.

```text
env^(0,◦) --u1--> gau^(0,◦) --u2--> LGP^(0,◦) --u3--> lgp^(0,◦)
    ↑ k_env           ↑ k_gau          ↑ k_LGP          ↑ k_lgp
env^(0,0) --b1--> gau^(0,0) --b2--> LGP^(0,0) --b3--> lgp^(0,0)
                                      ↑ θ⁻¹
                                   native P_q
```

The IPL composite is `u3 u2 u1 k_env b1⁻¹ b2⁻¹ θ⁻¹`. This preserves the given abstract strip data; it does not identify its two arithmetic-holomorphic realizations. Native Q remains the marked endpoint, with the splitting s_q and localization tuple from E3d. No determinant is carried across θ by pretending it is a ring map.

## 3. Exact log fragment at its available level

III Proposition 1.2(x), p.34, supplies the log-linked graph with its coric vertex. One adjacent piece is

```text
F_(1,m)   --log correspondence-->   F_(1,m+1)
       \                              /
        \ Kummer identifications      /
         -------- coric data --------
```

The top edge concerns the specified monoid portions and domains. The sloping edges denote the corresponding Kummer maps on the labeled data. This is a graph of specified comparisons, **not a commuting triangle**: Proposition 1.2(iv), p.31, and Remark 1.2.2(iii), pp.36–37, state the relevant failure and the replacement by upper semi-compatibility. Proposition 3.5(ii), pp.104–106, gives the packet-level containment/surjection statements. Its global MOD companion is Proposition 3.10(iii), p.149.

This finite piece tests one adjacent change. It does not replace all permitted log iterates by finitely many indices or claim that coherence for one edge settles every iterate.

## 4. Orbit-level boundary

```text
T_B-(Y_-)     .... R_log not reconstructed ....     T_B+(Y_+)
    |                                                  |
 upper tuple                                       upper tuple
    | U_B-                                             | U_B+
    v                                                  v
    Y_-           source comparisons on data            Y_+
```

Both fibers are individually well-defined for specified endpoint tuples. The displayed dotted relation is an obligation, not an arrow or a declaration that every pair is related. Even the permitted comparison of the actual IPL endpoint tuples must be supplied by the source construction. The available lower-level comparisons cannot simply be relabeled as Y_IUT:J_IUT→C_q^loc-lin.

Consequently the recovered object is this **partial route with an explicitly missing orbit relation**, not a completed native-q diagram. No new transport work is launched after this stop.
