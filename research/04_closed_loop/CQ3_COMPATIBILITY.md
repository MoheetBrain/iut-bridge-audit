# sQ3/cQ3: typed reconstruction

**Result: substantial paragraph-level typing; full recursive reconstruction remains PARTIAL.** Remark 3.9.5 was read in full, (i)–(x), PDF pp.126–145. The obstruction is no longer an unspecified “quotient of regions”: the source supplies concrete local and global categories and compatibility data.

Start in the codomain column of the Θ-link with the labeled tensor packets `I_Q`. Region class `P` and hull class `H` are those of Remark 3.9.5(i)–(ii), pp.127–128. A relatively compact admissible region has its smallest holomorphic hull `phi(P)`; hulls are products of modules of the form `lambda O`, with the stipulated nonzero components. Non-relatively-compact cases may give the whole ambient space. The upper-category discussion must be restricted to the proper/bounded hull situation actually used. Archimedean analogues cannot all be replaced by nonarchimedean modules.

`P -> phi(P) -> weighted determinant line -> det^(tensor M)(phi(P))`

is shorthand for the source construction, not an assertion that taking a tensor power of a rank-r vector bundle and then taking its determinant has exactly the displayed exponent. **Ob3**, pp.131–133, requires component determinants, suitable positive powers encoding the rational weights, and tensoring with the inverse determinant of the structural sheaf. The source calls their combination `det^(tensor M)(-)`: on the structural module tensored with a line L it produces `L^M`. M must also accommodate the local stack twists. These distinctions matter for rank, ramification and normalization.

The result lies in the local/global Frobenioids attached to the codomain full prime-strip. It is comparable with the **M-th power of the native q-pilot**. The power is tracked through degree-M naive Frobenius and tensor-root presentations; the internal categories and their localization functors remain present [Ob4, pp.133–134]. This is no license to confuse q with an arbitrarily rescaled pilot. Normalized degree recovers the intended original log-volume [Ob3-3].

## cQ3's actual category

For a bounded family of outputs, let `H_B=phi(P_B)` and `D_B=det^(tensor M)(H_B)`. The local upper category at v has:

- Objects `(X,[a])`, with X in the local Frobenioid and `[a]` the `Aut(D_B)`-orbit of a **linear morphism** `a:X -> D_B`.
- Morphisms of X compatible with the structure polymorphisms. One may restrict the objects to the specified hull approximants; the source presents this as an alternative.
- Suitable pullbacks carrying mutually compatible faithful actions of `G_v` and the Frobenius-like unit data.

These are the source's cQ3 clauses, pp.141–142, referring to FR1 Definitions 1.2(i), 1.3(i). The automorphism orbit is on structure morphisms; it does not identify all objects or declare their volumes equal.

A local-global upper object is a tuple

`((X_v,[a_v])_v, X_global, (rho_v)_v)`

where `X_global` belongs to the global realified Frobenioid and each `rho_v` is an isomorphism from the local realification to the localization of `X_global` at the corresponding prime. Morphisms are compatible local/global collections. The source refers to FR2 Example 5.6(iii)–(iv), rather than discarding the global object after specifying local fields.

The **formal quotient** is described by the pair of this category and the analogous category using the original local Frobenioids, interpreted as the second modulo the first. This paragraph is more informative than a scalar quotient, but it does not supply here a universal categorical quotient, a specified stack construction, or a complete descent theorem in independently checked form. These are limits of the extracted description, not a demand for a stronger universal quotient than the proof uses. A category-pair presentation may suffice; the necessary check is the claimed q-preserving comparison and its scalar interpretation within that presentation. We have not substituted an arbitrary equivalence relation on measurable sets.

## Information carried forward

Retained through cQ3 are the codomain arithmetic holomorphic setting, multiplicative line objects, local Galois and unit actions, the global realified Frobenioid, localization isomorphisms, power bookkeeping and the structure polymorphisms. The region's fine additive shape is replaced by the hull and determinant data. The q-intertwining is still represented by the connection of all this data to the **native codomain full prime-strip**, not by naming a new scalar q.

Remark 3.9.5(v) really does define a set quotient collapsing a subset. Its later category presentation is additional structure. Moreover, hulls collapsed by that formalism can have different volumes [iii–vi, Ob6]; passage to an upper bound is not evaluation of a constant scalar on each collapsed hull class. This must be addressed at sQ5.

The source explicitly rules out bypassing hulls by replacing the Frobenioids with a general category of regions [x, pp.144–145]: higher-rank additive geometry is not compatible with the multiplicative Θ-link. A determinant/norm to Q also cannot simply replace the Galois-compatible local construction. See [SQ3_TYPES.csv](SQ3_TYPES.csv) and [FORMAL_QUOTIENT_LEDGER.csv](FORMAL_QUOTIENT_LEDGER.csv).
