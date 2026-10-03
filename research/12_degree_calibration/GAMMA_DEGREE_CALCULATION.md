# Calibration and effectivity of Gamma_chi

**2026-10-03.** The new local-fiber result is proved in [LOCAL_EXISTENCE_TEST](LOCAL_EXISTENCE_TEST.md). This file separates the degree calibration of the particular stage 11 composite from the effectivity/boundedness of its output. No coefficient realization of Gamma_chi is invented. The final bounded native specialization remains at the earlier realization boundary.

## 1. Retained comparison and intrinsic degree data

Keep the fixed `(0,0)->(1,0)` link and the coupled record chi from [stage 11](../11_evaluation_instantiation/PROOF_ATTEMPT.md), including all Kummer, evaluation, NF-localization and log-domain choices. In that notation,

\[
\Gamma_\chi=d_1^e A_1^e h_E K_{0,E}(A_0^F)^{-1}\lambda^{-1}:B_q\longrightarrow T_1^e.
\tag{G1}
\]

Its global realified Frobenioid component induces an ordered Picard-group isomorphism

`gamma_chi: P_q=Pic(C_q) -> P_T=Pic(C_T)`.

This is a consequence of the accepted full-prime-strip constructions and the Picard reconstruction (FrI Theorem 5.1, pp.96-97; III Remark 2.4.2(v), p.90). Write eta_q for the nonzero negative native pilot class. The full prime-strip morphism takes it to its associated abstract target pilot class; this follows from II Definition 4.9(viii), p.158. The class is not thereby identified with a bounded arithmetic region.

Here is the one source-typed diagram for this calculation. Solid arrows are available abstract data; dotted arrows denote the particular realization/application still to be instantiated.

```text
   B_q ---------------- Gamma_chi ----------------> T_1^e
    | global realified portion                       | global realified portion
    v                                                v
   C_q -------------- Gamma_chi,g -----------------> C_T
    | Pic                                            | Pic
    v                                                v
   P_q ---------------- gamma_chi -----------------> P_T
    | nu_q / M                                       : rho_chi,*  (uninstantiated)
    v                                                v
    R                     Pic(C_rec) <...............+
                              | nu_rec / M
                              v
                              R

  In the receiving arithmetic presentation, separately:
  Q_M ; D_H = corrected det^(tensor M)(H_Theta).
  An effective comparison of the realized Gamma image with D_H is not drawn
  as an existing arrow. The local maps of LOCAL_EXISTENCE_TEST are not rho_chi.
```

The nu maps are the specified normalized arithmetic degree evaluations, with the log-volume sign convention of III Proposition 3.9(iii); they are not bare identifications of unmarked copies of R. C_rec denotes the receiving arithmetic Frobenioid in which the hull determinant is computed. The missing datum is a source-supported realization/comparison rho_chi, or its weaker formal replacement, identifying the evaluated Picard datum with that receiving calculation **with its marking and bounded-output provenance**. This is the same realization boundary as stage 11, now tested against calibration separately.

## 2. What can be calculated intrinsically

Between chosen ordered real-line degree coordinates any ordered additive isomorphism is multiplication by one c>0. Proof: it sends positive elements to positive elements; additivity fixes its values on rational multiples of one positive element; bounding a real number between rational multiples determines its value. This does not require an extra continuity axiom. FrI Theorem 6.4(ii), pp.114-116, is the corresponding source statement for equivalences of realified arithmetic Frobenioids.

Thus, once the target's *independently specified arithmetic degree chart* is supplied, the abstract global map has

\[
\nu_T\gamma_\chi=c_\chi\nu_q,\qquad c_\chi>0.           \tag{G2}
\]

Scales multiply under composition and invert under inverse maps. Applied to (G1), in compatible fixed endpoint charts,

`c_Gamma=c_d1 c_A1 c_h c_K0 / (c_A0 c_lambda)`.

This is a typed accounting identity, not a computation that any of these factors equals one. In particular one must include the horizontal Theta-link and the eventual receiving realization; a result about vertical log-links alone cannot assign the composite's scale.

For a source-specified realization rho_chi, put F_chi=rho_chi,* gamma_chi and define the calibration functional **before reference to H** by

\[
\mathcal E_\chi=\nu_{\rm rec}F_\chi-\nu_q,\qquad
\Delta_\chi^{\rm Pic}=M^{-1}\mathcal E_\chi([Q_M]).        \tag{G3}
\]

If F_chi has scale c in these charts, then Delta_chi^Pic=(c-1)a, where a=nu_q([Q_M])/M<0. Hence c=1 gives zero defect; c<=1 gives a nonnegative defect; c>1 gives a negative defect that would need compensation by sufficient slack. This Delta is independent of b and is **not** defined as b-a. No numerical c or Delta for the bounded Gamma realization was recovered in this run.

There are real calibration mechanisms in the sources. A compatible global model coefficient has divisor of degree zero (FrI Example 6.3). FrI 6.4(iv) forces degree one for an equivalence of the specified *unrealified arithmetic Frobenioids*. FrII Remark 5.6.3, p.65, gives a related criterion for its arithmetic poly-Frobenioids. Those stronger hypotheses have not been identified for the composite (G1) with its split/x-mu, pilot-dependent local structures and realified global component. In particular the bad-place divisor monoid is generated by the prescribed q (I 3.2(iv)), not an unmarked assertion that every local value-group generator equals the ambient field's primitive valuation generator. We therefore do not apply these stronger degree-one conclusions solely because a prime-strip isomorphism exists.

For an ordered Picard-line isomorphism, one independently calibrated nonzero class suffices to prove c=1. The native eta_q is such a potential calibrator. Defining the target chart by transport so that its image has the desired value would prove only a tautology; it would not identify that chart with the receiving packet/determinant normalization. Conversely, a source theorem doing that identification would suffice without principality or a canonical representative.

## 3. Ordinary accounting identity and its sign

Suppose an actual rank-one measured comparison supplies V_v=t_v Q_v subseteq H_v, with positive finite measures and finitely supported contributions (or convergent sums). Multiplicative scaling gives

`log mu_v(V_v)=log mu_v(Q_v)+log |t_v|_v`.

Sum this equality and subtract it from the definition of b. With

\[
a=\sum_v\log\mu_v(Q_v),\quad b=\sum_v\log\mu_v(H_v),\quad
\Delta=\sum_v\log|t_v|_v,\quad
S=\sum_v\log\frac{\mu_v(H_v)}{\mu_v(V_v)},
\]

one obtains

\[
b-a=\Delta+S,\qquad S\ge0.                              \tag{G4}
\]

S>=0 uses the *specified* containments. Delta=0 requires another fact, such as one global coefficient and the product formula. Neither local isomorphism nor arbitrary local membership implies that fact. The exact Q-control gives Delta=-log(p), S=0, b-a=-log(p); the single global p has zero defect but fails the real containment. Thus calibration and effectivity cannot be exchanged.

## 4. Packet, procession and determinant accounting

The IUT analogue uses its own weights. Let J=F_ell^star be the procession index set used in III 3.12, with averaging factor 1/|J|, and A_j the corresponding capsule. For a rational place v_Q, write tau=(v^alpha)_(alpha in A_j), and set

\[
N_\tau=\prod_{\alpha\in A_j}[K_{v^\alpha}:(F_{\rm mod})_{v_\alpha}],\quad
D_{j,v_Q}=\sum_{(w_\alpha)}\prod_{\alpha\in A_j}
 [(F_{\rm mod})_{w_\alpha}:\mathbf Q_{v_Q}],\quad
\omega_{j,\tau,v_Q}=\frac1{|J|N_\tau D_{j,v_Q}}.           \tag{G5}
\]

These are the normalized weights of III Remark 3.1.1(ii), p.94, followed by the procession average of Proposition 3.9(i), pp.115-116. The w_alpha range over all choices above v_Q, as printed. In particular D_(j,v_Q)=[F_mod:Q]^(|A_j|). They are not the unweighted sum over places of K.

For direct products in the finite tensor-algebra presentation, decompose the tau summand into local fields E_(tau,s). Write ell_(tau,s)(R) for the component's unnormalized additive log-volume, relative to the same structural reference. At finite places use log Haar volume; for an isotropic complex ball of radius r use the real-degree convention 2 log(r). Equivalently one can use plain radial log(r) and double its component weight. This retains the packet normalization of III 3.9(i): simultaneous multiplication by p at a finite rational place changes the packet log-volume by -log(p), and multiplication by e at infinity changes it by +1.

To check the factor, the sum of the component field degrees in a tensor summand is the product of the input field degrees. Consequently the weighted sum of those degrees is D_(j,v_Q); division by D_(j,v_Q) gives one. At infinity the real degree of each complex component is two, so omitting that factor while retaining (G5) would fail the e-normalization. These are numerical determinant/log-volume coordinates in one holomorphic presentation, not a norm functor on the Galois/unit data of the Theta-link (III 3.9.5(x), pp.144-145).

For this product-region calculation the normalized functional is

\[
L(R)=\sum_{v_Q,j,\tau,s}\omega_{j,\tau,v_Q}
       \ell_{\tau,s}(R_{j,\tau,s}).                      \tag{G6}
\]

All but finitely many local contributions vanish in Proposition 3.9(iii)'s domain. For a supplied coefficient action in this *same* presentation, define J_(tau,s)(t) from that action's volume multiplier: at a finite component it is log|Norm_(E/Q_p)(t)|_p; at a complex component it is 2 log|t|. Summing the component equalities yields

\[
L(H)-L(Q)=\Delta_w+S_w,\quad
\Delta_w=\sum\omega J(t),\quad
S_w=\sum\omega\,[\ell(H)-\ell(tQ)]\ge0.                  \tag{G7}
\]

This derives the correct weighted identity whenever the actual coefficient/determinant comparison exists. It does not assign these coefficients to Gamma_chi. III Remark 3.1.1(iii)-(iv), pp.95-97, expressly distinguishes weighted log-volume from an ordinary measure on general regions; (G6)-(G7) are restricted to the direct-product arithmetic setting just specified.

Ob3, III pp.131-133, requires weighted positive tensor powers of determinants **and the inverse weighted determinant of O_(minus)**. It characterizes the resulting common positive integer M by

`D^M(O tensor L)=L^(tensor M)`.

Use that same M on the native pilot: Q_M=Q^(tensor M). With the source's matching degree normalization, for an admissible arithmetic region R one has

`L(R)=nu_rec(D^M(R))/M`.

Thus in powered determinant coordinates, Delta_w and S_w are respectively the corrected determinant degree change and the effective residual degree divided by M. The structural reference cancels between the two corrected objects **in this common presentation**. Across presentations one must transport that reference as well; no cancellation is assumed in advance. Replacing M by dM multiplies every powered degree, defect and slack by d and leaves the normalized identity unchanged. It does not authorize an M-th power of the theta-function construction.

The root is still q_v=q_Tate,v^(1/(2 ell)), with its prescribed torsion ambiguity. The already verified local native contribution is -r ord_v(q_v)log(p_v) after division by the common M. Torsion does not alter it. Every finite and archimedean contribution and the procession average is retained. MOD's global rational-function/torsor comparison and mod's local-fractional-ideal comparison remain distinct (III 3.6, 3.7, 3.9; stage 9); their vertical compatibility does not supply arbitrary equality of realized regions.

## 5. Application of the undischarged source conditions

**Sign.** III 3.12, p.174, has a=-|log q|<0. If finite b>=0, the desired inequality is immediate; the nontrivial finite case has b<0. III 2.4.2(iii)-(vi), pp.89-91, then places negative pilot elements in a common ordered Picard/Frobenioid setting with consistently directed pre-steps. It rules out reversing the order while pretending to keep arithmetic degrees. It fixes orientation, not scale, and does not compare the magnitudes of two negative elements. Neither finiteness of b nor the existence of the bounded native specialization is proved by this reduction. If b=+infinity the comparison inequality alone is trivial, but the corollary's finiteness assertion remains separate.

**Product formula and vertical calibration.** III Remark 3.9.6, p.145, explicitly deduces compatibility of global arithmetic degrees from the log-link compatibility on sufficiently small regions and their inter-place conversion ratios. This is a positive source input, not merely a theorem title. In the domain of III 3.9(iii)-(iv), transporting the conversion ratios keeps the normalized global functional fixed on the compared classes. The previously constructed Rss native value is consistent with that assertion. It does not apply the product formula to arbitrary independently selected coefficients, nor does it identify (G1)'s bounded receiving realization. It therefore discharges a vertical normalization issue in its stated domain, not the entire joint application.

**Objects versus comparison morphisms.** A globally compatible coefficient in the model makes the coefficient divisor's degree zero. The local/global *object* record in cQ3 does not assert that its local a_v are localizations of that coefficient or of a global comparison arrow. LOCAL_EXISTENCE_TEST proves this distinction from the actual record. III 3.12(xii) expressly explains why local isomorphism classes cannot replace the global Frobenioid in a precise log-volume computation.

**The compensating unit automorphism.** Retain

`delta_1=eta_1^(-1) bar(alpha) eta_0 (h_E^unit)^(-1)`.

At stage 11's declared type this is an automorphism of abstract unit prime-strip data. It has no computed determinant on a receiving arithmetic module. Multiplication by a concrete valuation-zero unit would preserve a finite-place lattice volume, but delta_1 is not identified with such multiplication; even the word “unit” in its name does not provide that identification. No extension to every arithmetic realization is assumed. Its effect on the particular marked determinant remains part of rho_chi's construction.

**Permitted enlargement and effectivity.** A realized output known to lie in the stipulated family is bounded by its hull. The free local maps of the preceding file do not prove that membership, do not preserve its native degree by themselves, and need not be induced by the accepted formal family of 13.12(3)(c)-(d). No new S_chi>=0, effective global residual class, or weaker marked bound is derived for Gamma_chi here. IPL/SHE in III 3.11.1(iii), pp.160-161, asserts the relevant source relationship; this run does not use its endpoint coverage or xi-f as a premise.

## 6. Formal approximation, with calibration first

If a source comparison uses III 3.9.7, pp.146-147, keep its inverse system of enclosing direct-product regions and its shared local/global witnesses. Do not replace it by arbitrary equal-volume representatives. For an actual indexed comparison c with powered Picard image x_c and effective residual z_c relative to an enclosing determinant D_c, the intrinsic identity is

`nu_rec(D_c)/M - a = Delta_c + nu_rec(z_c)/M`,

where Delta_c is computed from the specified map on the native class as in (G3). For example, calibrated defects Delta_c>=-epsilon_c and residual degrees >=0, together with epsilon_c->0 and enclosing degrees tending to b from above, imply b>=a. Calibration must hold along that same indexed family before taking the limit. No such family is constructed in this run. Exact attainment or pointwise containment is not required for this sufficient formal alternative.

## 7. Acceptance boundary

New: source-model constructions show why the free local existence target is too weak, and the cQ3 record does not itself globalize the structure maps. The exact Q diagnostic and the weighted/intrinsic accounting separate calibration from effectivity.

Retained, not independently re-proved: the source's categorical/Kummer reconstruction, evaluation equivariance, Picard reconstruction and vertical degree-compatibility results. Still unresolved: the particular source-permitted receiving realization of Gamma_chi whose image is both calibrated at the native marked class and controlled by the stipulated hull/formal bound. No numerical Gamma defect, new global inequality, essential flaw or source-faithful countermodel has been established.
