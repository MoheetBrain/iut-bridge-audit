# Localization reconstructed from the action on volume

2026-10-04. This expands III Remark 3.9.2, p.119, and Remark 3.11.2(iv), p.169, in their stated MOD setting. Source versions, hypotheses and limits are recorded in [SOURCE_INSTANTIATION.csv](SOURCE_INSTANTIATION.csv). The mathematical application to the fixed comparison is in [PILOT_SPECIALIZATION](PILOT_SPECIALIZATION.md).

## 1. Objects and the action that is actually available

Fix a capsule A, a distinguished label alpha, and a place v in the source's selected set V; let w be its image in V_mod and u its rational place. Put F=F_mod, d=[F:Q], F_w its completion, K_v the selected extension, d_w=[F_w:Q_u], and n_v=[K_v:F_w]. All these belong to a *single* holomorphic presentation. The source supplies their mono-analytic counterparts, with their compatible volume functions, by III Proposition 3.9(ii). No identification of fields across the Theta-link is being added.

The acting group is

`G_alpha = ((M_mod)_alpha)^× = ((M_MOD)_alpha)^×`,

the nonzero elements of the non-realified number-field copy of III 3.3 and 3.7(i). The source's decorated M notation already denotes these multiplicative elements where it calls them monoids. Zero is excluded. It is neither the realified Picard group nor an arbitrary independent product of local coefficients.

Use the injection of III 3.3(ii), p.100: insert m in the alpha factor and 1 in every other tensor factor, then use the *given* NF localization. On the direct summand with alpha-place v this is multiplication by m_v. On other summands it is the corresponding localization of the **same** m. To read one place, restrict this action to the v-summand. This restriction of an observable does not invent a globally supported coefficient at v.

For a finite tensor-algebra level containing these data, write

\[
B_\tau=\bigotimes_{\beta\in A,\,\mathbf Q_u}K_{v^\beta}
       =\prod_s E_{\tau s},\quad
N_\tau=\prod_\beta n_{v^\beta},\quad
D_A=\sum_{(w_\beta)}\prod_\beta d_{w_\beta}=d^{|A|}.
\tag{R1}
\]

Here tau runs through the selected v's over u, independently in each factor. The weights in III Remark 3.1.1(ii), p.94, are `1/(N_tau D_A)`. Tensor products and field degrees are over Q_p at finite u and over R at infinity. The K_v at infinity are complex in this presentation; d_w still distinguishes real and complex places of F.

For the calculation choose direct product regions E with nonempty compact open components at finite places, and products of positive-radius closed radial balls at infinity. Both E and mE are in the permitted volume domain. Finite scalar multiplication preserves compact openness. An archimedean component is interpreted radially; this is not a claim that the source assigns ordinary Haar measure to arbitrary subsets of a complex packet. Fixed offsets between holomorphic and mono-analytic integral structures cancel in the difference. III 3.9.1 explains those offsets; its tensor-metric factor is not a new multiplier in the action increment.

## 2. Weighted calculation, including the restricted packet

Let `|p|_w=p^(-1)` for finite w, extended to F_w, and use the usual absolute value at infinity. Put k_v=n_v d_w. At a finite place the change on a component is

`log |Norm_(E_tau,s/Q_p)(m_tau,s)|_p`.

Summing over s is the logarithm of the determinant of multiplication by m on B_tau. Since only one tensor factor is acted on, it is

\[
\left(\prod_{\beta\ne\alpha}k_{v^\beta}\right)
\log|\operatorname{Norm}_{K_v/\mathbf Q_p}(m_v)|_p
=\left(\prod_\beta k_{v^\beta}\right)\log|m|_w.
\tag{R2}
\]

At infinity use `2 log |m_tau,s|` per complex component, or equivalently radial log-volume with twice the component weight. The same real-dimension identity proves (R2). This convention gives +1 for simultaneous multiplication by e on a packet; the finite convention gives -log(p) for multiplication by p. It agrees with III 3.9(i), pp.115-116.

Restrict the *full-packet* weighted sum to tau with v^alpha=v. Its increment is

\[
\begin{split}
\ell^{\rm contribution}_{A,\alpha,v}(m)
&=\sum_{\tau:v^\alpha=v}\frac{\prod_\beta k_{v^\beta}}
 {N_\tau d^{|A|}}\log|m|_w\\
&=\frac{d_w d^{|A|-1}}{d^{|A|}}\log|m|_w
=\kappa_w\log|m|_w,\qquad \kappa_w=\frac{d_w}{d}.
\end{split}\tag{R3}
\]

The **packet-normalized restricted volume** of III 3.9(i) is normalized again so that its p-increment is -log(p), rather than -kappa_w log(p). Thus

\[
\ell^{\rm local}_{A,\alpha,v}(m)
=\mu^{\log}_{A,\alpha,v}(mE)-\mu^{\log}_{A,\alpha,v}(E)
=\log|m|_w;
\quad \ell^{\rm contribution}=\kappa_w\ell^{\rm local}.
\tag{R4}
\]

Equivalently its component weights are those in (R3) divided by kappa_w. Distinguishing these two normalizations is necessary: treating the restricted summand's contribution as a separately normalized packet would lose a field-degree factor.

For the actual procession let J be its set of capsules, A_j its capsule and alpha_j=j its distinguished factor. The contribution of the corresponding global elements m_j is

\[
\ell_{\rm procession}((m_j))
=\frac1{|J|}\sum_{j\in J}\sum_w\kappa_w\log|m_j|_w.
\tag{R5}
\]

For one acted-on capsule retain the factor 1/|J|. For a synchronized action on all capsules sum first and then average. There is no extra factor |A_j|: it is only the distinguished factor that is acted on. The other factors have already canceled in (R3).

**Independence of E.** Haar change of variables proves (R2) for every finite component of a direct product region; a radius r is replaced by |m|r at infinity, so `2 log(|m|r)-2 log r=2 log|m|`. Add the fixed weights. Therefore (R3)-(R5) are independent of the chosen E in this class. Composition gives ell(mn)=ell(m)+ell(n). The argument needs no arbitrary-set measure or hull approximation. III Remark 3.1.1(iii)-(iv), pp.95-97, distinguishes the broader weighted construction from an ordinary measure; nothing here replaces it.

## 3. The actual quotient and cone

Set `lambda_w(m)=-ell_local(m)=-log|m|_w`. Then lambda_w is nonnegative on local integers: at finite w it is `ord_p(m) log(p)` with ord_p(p)=1, and at infinity it is nonnegative when |m|<=1. Its kernel is exactly the globally defined elements that are local units at w. This recovers the unit kernel by an action measurement, rather than assuming that taking the ordinary local-unit quotient commutes with log.

Extend to the perfection G_alpha^pf by

`lambda_w^pf(m^(1/N))=lambda_w(m)/N`.

This is an abstract rationalization, not a choice of new roots acting on E. Torsion has zero increment, and equality after a common power proves that this formula is well-defined. The reconstructed ordered quotient and its cone are

\[
V_w^{\rm act}=G_\alpha^{\rm pf}/\ker\lambda_w^{\rm pf},\qquad
(V_w^{\rm act})_{\ge0}=\{[g]:\lambda_w^{\rm pf}(g)\ge0\},
\quad [g]\longmapsto\lambda_w^{\rm pf}(g).
\tag{R6}
\]

This displays the subquotient of Remark 3.9.2. At finite w the image before perfection is a nonzero discrete subgroup of R; its positive generator can be recovered from that image. Perfection gives its rational span, and realification gives the oriented real ray. At infinity the image of global elements need not equal R. Its perfection contains rational multiples of log(2), hence is dense; its ordered completion supplies the real ray. One must not replace that ordered completion by an unrestricted algebraic tensor product with R. The realified local cone itself is already a source input in I 5.2(iv).

Thus this calculation recovers the valuation quotient, its positive cone, and its scale **relative to the given packet volume**. It does not reconstruct the local field multiplication, Galois action or unit structure from the scalar quotient. Those structures remain in the accepted source record.

## 4. Divisor localization, with the source's degree factor

The rho_v in I Definition 5.2(iv), pp.134-135, has type

`rho_v: Phi_(C_global),w -> Phi_(C_local,v)^rlf`,

an isomorphism of topological monoids isomorphic to R_{≥0}. It is a divisor-monoid map, not a map from global Picard classes to local Picard classes. Its associated localization functor is determined up to isomorphism by this map (I Example 3.5(i), p.84).

Let b_w(p) be the global prime-ray element called log_mod(p) in I 3.5, and b_v(p) its local counterpart log_Phi(p). The source's map is **not** the unweighted identity:

\[
\rho_v(b_w(p))=\frac1{n_v}b_v(p),\qquad
\rho_v(t b_w(p))=\frac{t}{n_v}b_v(p)\quad(t\ge0).
\tag{R7}
\]

The numerical volume coordinates verify the factor. The global prime component has size d_w log(p); the raw K_v component has size n_v d_w log(p). Weighting the latter by 1/n_v gives the former; division by d gives the contribution in (R3). The p used here is a test scalar and a generator of a real ray; it need not be a primitive integral uniformizer. At infinity choose the positive ray generator e of I's convention. Its divisor orientation corresponds to contraction by e^(-1); expansion by e has volume increment +1. The same factor 1/n_v applies. Alternatively use the global scalar 2 to recover the ray and then extend continuously to the e-normalization.

For a reconstructed global prime element z, (R7) can be written without an unspecified map:

`rho_v(z) = [c_w(z)/c_w(b_w(p))] b_v(p)/n_v`,

where c_w is the prime coordinate recovered from (R6), rescaled by the fixed d_w contribution. Any nonzero positive element can replace b_w(p), with the same result. For env/theta coordinates, use the actual evaluation image of b_v(p); I 3.5(ii), p.85, and II 4.6(v), p.139, supply that change of coordinate. Identifying a formal theta generator with the field scalar p would discard this requirement.

## 5. Extension to line objects, and its limit

The calculation is **not confined to principal Picard classes**. III Example 3.6(i), p.107, specifies a global G_alpha-torsor T with local trivializations t_v of its pushouts by beta_v. Given that record, use (R6) for beta_v and (R7) for the divisor normalization; push out T along the reconstructed quotient map, carrying t_v with it. This is the reconstructed localization of this line object. Integral morphisms are reconstructed by the same nonnegative cones. Perfection and realification extend this construction; III 3.6(iii), p.108, supplies the independence at those levels of a choice of the same-field MOD/mod identification.

In a fractional-ideal presentation, choose a common generic basis t. If its local integral generator is m_v t, then the line is represented locally by m_v O_v and its normalized degree is

`sum_w kappa_w log|m_v|_w`,

with the procession average when applicable. Changing the common basis replaces the local m_v by m_v/f for a *single* f in G_alpha. The change in the sum is zero by the product formula. This proves basis independence; it does not say that every line has degree zero. The finite-support condition is the one in III 3.6 and 3.9(iii). For realified objects use the associated additive divisor coordinates rather than require scalar representatives of all real exponents.

There is a useful nonzero calibrator here. The positive arithmetic divisor supported **only at w** with coefficient b_w(p) has normalized degree `kappa_w log(p)>0` at a finite place. Its negative is the class of the line with local ideal pO at that place and O elsewhere. The entire principal divisor of the global scalar p includes all finite and infinite contributions and has degree zero. It cannot calibrate a nonzero Picard class. Localizing its divisor and retaining a *single prime component* is a different, legitimate operation; transporting that marked component across a comparison is an additional assertion to check.

This reconstructs the localization functor on the source MOD torsor model, up to the source's isomorphisms. It does not select a torsor/trivialization tuple for a bounded algorithm output from a Picard class alone, nor identify such a tuple with the fixed native-q marking across the horizontal link. The latter application is the next file's explicit test.
