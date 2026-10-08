# Numerical comparison and normalization test

Sources and byte/version pins: [SOURCE_CROSSWALK](SOURCE_CROSSWALK.md). All inequalities below distinguish labelled source norms, receiving volumes and the original IUT degree.

## Recovering the j-squared calculation

Write m=(ell-1)/2. At a selected split multiplicative place w, let q_w be the Tate parameter at the standard coordinate **j=m** and write

\[
Q_w=|q_w^{1/(2\ell)}|_{\rm can},\qquad 0<Q_w<1.
\]

Construction III 4.2.2.1 and II 6.9.1 give relative scaling `v_j=j^2 v_1`. II 9.2.1, pp.27–28 explicitly constructs a tuple with standard coordinate m and hence

\[
v_1=v_{\rm can}/m^2,\qquad
v_j=(j^2/m^2)v_{\rm can}.
\tag{N1}
\]

This does not identify different untilt fields by a field map. For the fixed embedded Tate data it compares their valuations in the specified tilt value group. The normalized 1-unit logarithm of III 9.7.2,9.8.2.7 has norm

\[
\left|\frac{\log_p(1+p^*q_{w,j}^{1/(2\ell)})}{p^*}\right|_j
=|q_{w,j}^{1/(2\ell)}|_j=Q_w^{j^2/m^2}.
\tag{N2}
\]

Here the hypothesis `p* q^(1/(2 ell)) in p* O_E` places the logarithm inside its strict norm-preservation radius. This proves a norm identity for the constructed **unit class**, not equality with the nonunit native q-class.

Consequently the labelled tuple product is

\[
\prod_{j=1}^m Q_w^{j^2/m^2}
=Q_w^{S_m},\quad
S_m=\frac{(m+1)(2m+1)}{6m},\quad
\alpha_m=\frac{S_m}{m}=\frac{(m+1)(2m+1)}{6m^2}.
\tag{N3}
\]

For m>=2, `0<alpha_m<1` and `S_m<m`. Since `log Q_w<0`,

\[
S_m\log Q_w>m\log Q_w,\qquad Q_w^{S_m}>Q_w^m.
\tag{N4}
\]

Thus a supremum of the **labelled pre-collation norms** including this tuple has the claimed lower estimate. It does not automatically follow that its image under an arbitrary allowed topological cohomology isomorphism has that same norm in the independently measured receiving realization.

In terms of the unrooted parameter, the coefficient in the product log is exactly

\[
\frac1{2\ell}\sum_{j=1}^m\frac{j^2}{m^2}
=\frac{m+1}{12m}<\frac{m}{2\ell}.
\tag{N5}
\]

The unnormalized average discussed by Scholze–Stix/LANA is `(m+1)(2m+1)/6`, of order m^2. Joshi's standard-point convention **divides it by m^2**, yielding alpha_m, approaching 1/3. The factors have been retained and re-referenced, not proved irrelevant to the original receiving degree.

### Literal index inconsistency in III equation (9.9.4)

The displayed equation on III v4 p.121 writes the right-hand reference as `|q_{w;1}^{1/(2 ell)}|_{L'_w,1}^{j^2/m^2}`. But Theorem 4.2.2.1's relative-to-first-coordinate exponent is **j^2**, while the exponent **j^2/m^2** is relative to the canonical **mth** coordinate. Under the literal indices, j=1 gives `r=r^(1/m^2)` for `0<r<1` and m>=2, which is false. Equations N1–N5 use the reference explicitly constructed in **II 9.2.1**. This repairs the local calculation; it is not an IUT refutation.

## From local norms to volume: the factors that must be supplied

III 9.10.2 normalizes Haar measure by `mu_E(O_E)=1`. For E/Q_p of degree d_E, residue degree f_E and uniformizer pi,

\[
\mu_E(xO_E)=|N_{E/\mathbf Q_p}(x)|_p
=p^{-f_E\operatorname{ord}_E(x)}
=|x|_{p,\rm root}^{d_E}.
\tag{N6}
\]

Here the root-normalized absolute value has `|p|=p^(-1)`. A tilted absolute value may be a positive power of it. Equality of the Haar scaling factor with `|x|_E` therefore requires the **modulus normalization**, or an explicit power conversion. III 7.3.1 instead chooses `|pi_w|_{C_p}=p^(-1)`; this equals the Haar value of pi only if f_E=1. It cannot silently be used for every volume normalization in 9.10.

The local weight printed in 9.10.5 is `gamma_w=1/n_w`, `n_w=[L'_w:Lmod,v]`. Applying it to N6 gives

\[
\gamma_w\log\mu_{L'_w}(xO_{L'_w})
=[Lmod_v:\mathbf Q_p]\log|x|_{p,\rm root}.
\tag{N7}
\]

This is a legitimate **restricted local conversion**. It does not by itself prove that all tensor summands in 9.4.6, the procession's auxiliary entries, the global factor `[Lmod:Q]^(-1)`, and the split-field structure-sheaf correction agree with original III Proposition 3.9 and Remark 3.9.5(Ob3). The tensor product of rings of integers can have nontrivial index in the product of split-field integer rings; [PROOF_OR_OBSTRUCTION](PROOF_OR_OBSTRUCTION.md) exhibits index 3 explicitly.

Even granting the author's tensor-region volume formula 9.10.3.1 and assuming the N2 absolute values have been converted to that normalization, weights `0<gamma_j<=1` make negative logs less negative:

\[
\sum_j\gamma_j\log|\tau_j|\ge\sum_j\log|\tau_j|.
\tag{N8}
\]

That proves the last elementary inequality in 9.10.7.1 at its stated scope. Two additional assertions used by 9.11.1 remain distinct: **(i)** the measured set contains the full tensor lattice `tensor_j(tau_j O_{E_j})`, not just a tuple of points or their Z_p span; **(ii)** the relevant receiving normalization is the one used in N2–N8. An O_E saturation can enlarge the set and repair (i) for a newly defined hull, but does not place that enlarged set inside H_IUT.

### Product formula compensation

III 4.2.2.4 and 4.6.1 refer to normalization at other places. The immediate dependency II½ 5.3, p.32 is explicit: `|x|_v=|x|_{K_{y,v}}^{alpha_{y,v}}` on L_v, and these normalized restrictions recover the standard product formula. If the raw scaling at a bad place is `s_j=j^2/m^2` relative to the standard coordinate, then the normalization coordinate there changes by `alpha_j=alpha_can/s_j`. On the fixed embedded local element,

\[
\alpha_j\log|x|_j=\alpha_{\rm can}\log|x|_{\rm can}.
\tag{N9}
\]

The raw tilt comparison and the normalized arithmetic-degree comparison are therefore different operations. A principal x has total degree zero after normalization; that is not a volume calculation for the nonprincipal Tate-parameter tuple supported at bad places. Nor does it prove invariance of the collated theta hull. IV 6.10.1's simultaneous normalization of y_0 and phi(y_0) needs a comparison of the actual measured loci to yield its middle volume equality. This audit does not derive that comparison from the normalization identity alone.

## Sign check and the attempted sandwich

Suppose, as an **explicit source input at Joshi's own scope**, Theorem 9.11.1 gives `V_J>=Q^m`, where `Q=product_w Q_w` and `0<Q<1`. For finite positive V_J the valid consequence is

\[
a_J:=\log Q\ \le\ b_J:=\frac1m\log V_J.
\tag{N10}
\]

If also `V_J<=1`, this b_J is negative and equals `-|log V_J|/m`. For arbitrary positive V_J that replacement by a negative absolute value is not valid. The original frozen target has `a_IUT=-|log q|` and `b_IUT=-|log Theta|`; equations identifying these with N10 are additional translation assertions.

**III v4 Corollary 9.11.1.1, p.128 literally prints**

\[
-\frac1m|\operatorname{LogVol}(\widetilde\Theta^I_{Mochizuki})|
\ \ge\ -\sum_w\log |q_w^{1/(2\ell)}|_{L'_w}.
\tag{N11}
\]

The left side is nonpositive; in the nonempty split-multiplicative case the right side is **strictly positive**. This is inconsistent as written. If an absolute value around the negative sum was intended, replacing the right side by `sum log Q_w` and reading the left side as `log V_J/m` when V_J<=1 gives N10. Multiplying an ordinary log inequality by `-1/m` instead reverses its order. No sign convention stated on p.128 makes N11 a consequence of Theorem 9.11.1. The absolute-value bars and RHS sign were checked visually, not inferred from OCR.

The strongest candidate for the requested original sandwich is thus

\[
a_{IUT}\ \overset{?}{=}\ a_J\ \le\ b_J
\ \overset{?}{\le}\ b_{IUT}.
\tag{N12}
\]

Both question-mark steps are **unverified** at the complete source interface. A lower bound on a larger hull provides no upper comparison `b_J<=b_IUT`. For a common positively normalized measure, inclusion `H_J subset H_IUT` would suffice for that direction; the reverse inclusion would not. No such inclusion, or adequate weaker numerical substitute, was derived from the Rosetta statements or 9.10.8.1. The bounded numerical attempt stops here.

## Exact arithmetic controls

A temporary Python calculation checked N3/N5 for all **44 primes from 5 through 199**, the tensor matrix determinant -12 and its image modulo 3 (27 of 81 elements), exclusion of the idempotent (1,0), and surjectivity of both coordinate projections. A rational domain control used Q=1/16, V=1/8, m=2 to satisfy `V>=Q^m` while preserving the sign contradiction in N11. No floating-point p-adic approximation was used. These checks accompany the written proofs; they are not certification of IUT or Joshi's full proof.
