# Native Q is given; its formal-system representation is not yet typed

**Q_sys: unresolved because FormalSys_q is unresolved.** Section 5's stop precedes the choice of a constant diagram, a marked diagram, or a family over log-link iterates. This file preserves the native input fields; it does not relabel them as an object of an undefined category.

## Retained native input

Use precisely the [E3d definition](../06_e3d/E3D_TYPED_DIAGRAM.md):

`Q=(Hq,•,0,ι:P≅Ffull(Hq,0))`,

the native codomain vertical column of Θ±ell NF-Hodge theaters with coordinate (1,0) distinguished and the fixed full abstract strip P marked by ι. Isomorphisms must preserve this entire marked data. The relevant fields are:

| Field | Type and convention |
|---|---|
| Column and coordinate | The given native column with its vertical log-links; the coordinate is not moved freely to change the native endpoint. |
| Full strip P | Global realified Frobenioid C_P, its prime labels V, local full split-×μ-Kummer data, and local/global realification identifications. |
| Finite-place realization | Native local fields/rings and Π_v↠G_v rigidifications, including the Kummer unit realization. Splitting and units are in the same multiplicative structure. |
| Native bad-place splitting | `s_q,v:N→k_q,v^×/μ(k_q,v)`, `r↦[q̲_v^r]`. The root q̲_v is q_Tate,v^(1/(2ℓ)), with the source μ_(2ℓ) convention before the ×μ quotient. |
| Archimedean realization | The given compatible torsion-quotient systems, their surjections, and the stipulated order-two ambiguity; no chosen sign or inverse surjection. |
| Global pilot | `L_q∈Ob(C_q,g)` up to isomorphism, with the native global realified Frobenioid and its prime labels. C_q,g is not the category C_q of collections. |
| Localization | The native isomorphisms `ρ_q,v:r_v(L_q,v)≅loc_v(L_q)` and all given unit/prime-strip comparison data. |
| Power bookkeeping | `q_M=((q_M,v)_v,q_M,g,(ρ_qM,v)_v)∈C_q`, formed from the native pilot using the same positive degree-M naive Frobenius convention as the determinant presentation. M is not a free scalar rescaling. |

Source locators retained from E3d: [IUT I](../../sources/primary/IUT_I.pdf), Example 3.2(iv), p.71, Definition 5.2(iv), pp.134–135; [IUT II](../../sources/primary/IUT_II.pdf), Definition 4.9(i)–(viii), pp.153–158, Corollary 4.10(i), pp.158–159; [IUT III](../../sources/primary/IUT_III.pdf), Definition 3.8, pp.112–114, Remark 3.9.5 Ob7, pp.135–137. These are retained initial data, not newly reconstructed arithmetic geometry in E3d.1.

## Candidates tested, none selected as Q_sys

For every chosen J, `const_J(q_M)` is a perfectly well-defined ordinary C_q-diagram. Its constant transition maps do not encode the full Q-marking, nor establish that it is the target used by the source's formal quotient. An augmented marked diagram would need explicit attachment and preservation rules for the fields above. A family over vertical iterates must distinguish coric Galois/unit data from the different Frobenius-like realizations, and retain the directions of the finite inclusions and archimedean surjections in Theorem 3.11(ii), pp.155–156.

The source slices checked do not select one of these encodings in the required formal-system category. Thus the existence of q_M in the ordinary ambient category does not resolve the type of Q_sys. Native Q stays fixed; Ind1–3 do not authorize choosing a different native splitting to match a returned output.

Remark 3.12.2(ii), pp.187–189, describes simultaneous retention of q-intertwining as the target. Its conclusion is not used to choose a representation or to prove the missing preservation rule.
