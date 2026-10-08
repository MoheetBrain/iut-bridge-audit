# Bounded proof attempt and explicit translation obstruction

The original bridge is **neither derived nor refuted**. This attempt gives a restricted labelled-norm calculation, a counterexample to a universal hull identification in Joshi's translation, and exact printed index/sign inconsistencies. It does not give a faithful countermodel to original IUT.

## Work backwards from Theorem 9.11.1

The theorem's proof (Construction III v4 p.127) invokes 9.10.8.1 to work interchangeably with Banach convex closures and holomorphic hulls, 9.8.1 to obtain a standard tuple, 9.10.7.1 to bound a contained tensor region, and 9.9.1 for its numerical template.

Tracing that tuple gives the following actual chain:

1. Initial global data and the standard Ansatz tuple provide labelled Tate parameters in untilt structures (III §§3–4,6.4).
2. The class used in §9 is the crystalline **unit** Kummer class of `1+p* q^(1/(2 ell))` (§9.6), followed by a normalized logarithm (§9.7).
3. Proposition 9.7.5.1 collates images under the cited topological cohomology isomorphisms; 9.8.1 takes convex closures and tensor images.
4. Clause 9.8.1(7) identifies the result with IUT's multiradial representation; the proof provides no separately instantiated map from this family into the original permitted output, with matched weights and cQ3/cQ4 data.

The **first unestablished original-IUT inference** is step 4, including calibration after step 3. Before collation the Tate marking and its labelled norm are specified. After collation, being an image in a standard cohomology group does not establish that it is the same native-marked term in the independently bounded original output. No universal category or canonical representative is required for this observation: a verified one-sided numerical transfer would suffice. That was attempted explicitly in [NUMERICAL_COMPARISON](NUMERICAL_COMPARISON.md), N12.

## A counterexample to Proposition 9.10.8.1(1)

**Exact proposition challenged:** in the finite-dimensional Banach decomposition `f:E_1 tensor_Qp E_2 -> direct_sum F_alpha`, the source asserts that the holomorphic hull of a relatively compact U is the minimal **convex** subset containing f(U). Its assertion (3) identifies hulls of tensor regions with images of convex closures.

The original definition in IUT III Remark 3.9.5(i)–(ii), p.127 instead minimizes among **componentwise fractional-ideal regions**, with P1/P2/P3 characterizing that closure into the specified class H. It does not minimize among all Z_p convex subsets. [Schneider's author-hosted text](https://www.uni-muenster.de/IVV5WS/WebHop/user/pschnei/lectnotes/nfa.pdf), Chapter I §2, printed/PDF p.10, defines convexity using translates of modules over the base field's ring of integers. For the specified Q_p Banach space this is Z_p, not the product of the extension-field integer rings.

Take **p=3**, `E_1=E_2=E=Q_3(pi)`, `pi^2=3`. The Eisenstein polynomial gives `O_E=Z_3[pi]`. Let

\[
U=O_E\otimes_{\mathbf Z_3}O_E\subset E\otimes_{\mathbf Q_3}E.
\]

This is a full-rank compact open lattice: in particular it is relatively compact and has finite nonzero volume, as the original hull definition requires. With sigma(pi)=-pi, the field decomposition is

\[
f(x\otimes y)=(xy,x\sigma(y))\in E\oplus E.
\tag{O1}
\]

It is a Q_3-linear isomorphism of finite-dimensional Banach spaces. The images of the integral tensor basis are

\[
(1,1),\quad (\pi,\pi),\quad(\pi,-\pi),\quad(3,-3).
\tag{O2}
\]

They generate exactly

\[
A=f(U)=\{(x,y)\in O_E^2:x-y\in\pi O_E\}.
\tag{O3}
\]

Indeed, writing `x=a+b pi`, `y=c+d pi`, membership means `a-c in 3 Z_3`. Because 2 is a 3-adic unit, the coefficients of O2 recover every such pair. Both coordinate projections of A are all of O_E, but `(1,0)` is not in A. The quotient `O_E^2/A` is the residue field `O_E/pi O_E=F_3`, so its index is **3**. Equivalently the integral basis matrix in the two copies of `(1,pi)` has determinant -12, of 3-adic valuation 1.

The set A is already a **closed Z_3 module**, hence a closed nonarchimedean convex set. Its convex closure is A itself. However the smallest componentwise fractional-ideal region containing it is

\[
H(U)=O_E\oplus O_E\supsetneq A.
\tag{O4}
\]

Each projection contains 1, so neither component ideal can be smaller than O_E. This proves the strict inclusion directly, without a norm convention or a numerical approximation. With additive Haar measure normalized to give `O_E^2` measure 1, the convex closure has measure 1/3 and the holomorphic hull has measure 1. The discrepancy is not removed by making f continuous or by using equivalent Banach norms.

All hypotheses of the challenged **universal local proposition** are verified: finite p-adic fields, tensor decomposition, relatively compact full-dimensional region, and the actual split-field hull definition. Its part (2), preservation of convexity under a linear map, is not challenged. If “with this property” in part (1) was intended to restrict minimization to componentwise ideal regions, that restricted statement is true; it does not establish the ordinary Banach convex-closure equality used in part (3). The counterexample does not instantiate the global initial-theta datum, IUT's algorithm, or every IUT indeterminacy. None of those is a hypothesis of 9.10.8.1; accordingly this is **not** a faithful IUT countermodel or a claim against original Corollary 3.12.

### What can repair this particular step

Let `B=direct_sum F_alpha`, `O_B=direct_sum O_{F_alpha}`. For a bounded U with nonzero coordinate projections the holomorphic hull is the O_B saturation: each component is the fractional ideal generated by its projection. In particular

\[
\overline{\operatorname{conv}_{\mathbf Z_p}(f(U))}
\subseteq H(U).
\tag{O5}
\]

To prove this inclusion, H(U) is closed and Z_p convex and contains f(U). For the saturation description, choose in each nonzero projection an element of minimal discrete valuation, and use the component idempotents of O_B to generate its principal ideal separately. This is a standard closure argument, not a new IUT transfer theorem.

O5 permits a lower estimate for the **larger** hull from a lower estimate for its convex subset, provided the measure and normalization have been supplied. Thus the false equality is not demonstrated necessary for every repair of Joshi's own lower-bound argument. More importantly, enlarging H_J this way gives **no** comparison with H_IUT. The missing original bound cannot be supplied by declaring an enlarged family admissible.

## Forward numerical attempt

With the canonical mth-coordinate reference, the standard tuple has product norm `Q_w^S_m`, where `S_m<m`. This follows from the accepted Ansatz scaling, the p-adic logarithm estimate and elementary sums, as proved in N1–N5. A labelled norm supremum containing that tuple therefore exceeds `Q_w^m`. This is a substantive calculation beyond Stage 14; it concerns Joshi's own family.

To complete a volume derivation one must attach these norms to the collated receiving classes, specify the tensor-region or O_B saturation, and match the measure's extension, packet, procession and determinant factors. The author states the resulting volume lower bound in 9.11.1. Its proof is **not independently completed here**: the hull equality is false, full-region containment is stronger than point containment, and the source-norm/receiving-volume translation requires the conversions recorded in N6–N9.

Even granting 9.11.1 as an explicit input **about A_J**, its correct log consequence is `a_J<=b_J`. The necessary next comparison is `b_J<=b_IUT`, along with the native identification `a_J=a_IUT`. Neither follows from the presence of the same words “theta,” “log-shell” or “hull.” No source-justified inclusion or weaker numerical replacement was obtained. Therefore original `a_IUT<=b_IUT` does not follow from this attempt.

Two further literal defects can be proved without assuming the hull equality: III (9.9.4), at j=1 under its printed first-coordinate reference, contradicts `0<|q^(1/(2 ell))|<1`; and Corollary 9.11.1.1 has a nonpositive LHS and positive RHS in the nonempty bad-place case. Correcting these index/sign statements recovers a possible internal lower estimate; it does not recover the original transfer. These are local findings about the printed Joshi translation, not a certification that its whole programme is irreparable.

## Ambiguity test, necessity and final scope

The old `Q_5, ell=3`, multiplication-by-2 control is not rerun. III 3.3 requires **ell>=5**, so that auxiliary example is not a verified instance of these initial data. Period-ring lifts here retain a common lambda, selected Tate parameters and a root modulo torsion; they are not arbitrary independent scalars. The cohomological locus, however, uses unions of the cited topological isomorphisms. No calculation in the inspected source identifies their complete permissible subgroup with the original IUT mono-theta, global, unit/Galois and integral constraints at the receiving bounded record.

Cyclotomic equivariance alone remains insufficient, while full global integral conditions can exclude the old control. Neither statement proves that an unwanted ambiguity survives the actual IUT restrictions. No native-marking invariance theorem for that exact subgroup, and no faithful obstruction to all permitted weaker comparisons, is established.

**Why the final verdict is not B:** the universal hull assertion and literal printed formulas are refuted at their stated local/sign scopes. It has not been proved that any of them is an unavoidable inference in original IUT or that one-sided repairs cannot work. **Why it is not C:** the saturation fact and norm sum are standard restricted deductions; they do not supply the missing source-instantiated original comparison. The strongest result is **D, at restricted scope**: a lower estimate in the alternative labelled construction, with its required transfer to original IUT unestablished. This is not endorsement of a complete alternative proof of Corollary 3.12 or abc. Stop this route and preserve the archive.
