# Applying the reconstruction to the fixed pilot comparison

2026-10-04. Verdict: **SAME_REALIZATION_BOUNDARY_STILL_OPEN**. The reconstruction in [LOCALIZATION_RECONSTRUCTION](LOCALIZATION_RECONSTRUCTION.md) supplies actual quotient, cone, divisor and torsor-localization operations. This file records their application, and where that application stops. It does not use Corollary 3.12 or xi-f as a premise.

## 1. Fixed input and one typed diagram

Retain the actual pair `(0,0)->(1,0)`, its preceding log-links `(i,-1)->(i,0)`, and the coupled chi of [stage 11](../11_evaluation_instantiation/PROOF_ATTEMPT.md). Keep

\[
\Gamma_\chi=d_1^e A_1^e h_E K_{0,E}(A_0^F)^{-1}\lambda^{-1},
\quad T_L=A_1^e h_E(A_0^e)^{-1},
\quad\Gamma_\chi=d_1^eT_LK_{0,L}\lambda^{-1}.
\tag{P1}
\]

Let `x_q=[Q_M]`, `a=nu_q(x_q)/M`, `D_H=corrected det^M(H_Theta)`, and `b=nu_rec(D_H)/M`. M is the common allowed positive determinant exponent, including the inverse structural determinant. The native q-root and its torsion convention are unchanged.

There is one diagram below. Solid arrows are constructed abstract comparisons or reconstructed divisor maps; the last line is a requested application, not an existing arrow.

```text
 B_q --lambda^-1--> L_0^F --K_0,L--> L_0^e --T_L--> L_1^e --d_1^e--> T_1^e
                      | MOD global     | MOD global   | MOD global    | mod global
                      v                v              v               v
                    C_0^F ----------> C_0^e --------> C_1^e --------> C_T
                      | Phi_w          | Phi_w        | Phi_h(w)      | Phi_h(w)
                      v                v              v               v
                    Phi_0,w --------> Phi_0e,w -----> Phi_1e,h(w) --> Phi_T,h(w)
                      | R_0,w          | R_0e,w       | R_1e,h(w)     | R_T,h(w)
                      v                v              v               v
                    local realified divisor cones, with the matched local maps

 Pic(B_q) --gamma_chi--> Pic(C_T),   x_q |--> z_chi  (constructed abstractly)
                                    z_chi ...> y_chi in the D_H receiving record
                                              (marked bounded application open)
```

Here R denotes (R6)-(R7), including the torsor extension; h(w) retains the prime-index transport. No local Picard map is implicit in the vertical divisor rows. The global Picard map is taken only after assembling the full global object.

For the stipulated initial Theta-data, V_bad is finite and nonempty and ord_p(q_v)>0 there. Its native line therefore has finite negative degree: schematically `a=-sum_(bad w) kappa_w ord_p(q_v) log(p)<0` in the native one-line normalization. This checks nonzero and sign independently of the disputed output. The common M cancels on division. For the hull, finiteness of b is not proved by this reconstruction. The meaningful unresolved case is finite b<0; finite b>=0 gives b>=a directly, and b=+infinity gives only the extended-real inequality, not a finiteness theorem.

## 2. Instantiate the source recipe before extending its scope

For each actual `(i,m,j)`, set

`G_(i,m,j)=((i,m)M_MOD)_j`,

with its source action on `I^Q(S_(j+1),j;(i,circ)D_v)` and all its places. Apply (R4)-(R6) to that action, retain its torsor/trivialization data, and then (R7) to obtain R_(i,m,j,v). The number-field/localization constructions needed for this are exactly III 3.3, 3.7(i), 3.10(i)-(iii), and 3.11(ii)(c). Remark 3.11.2(iv) refers to these MOD-derived LGP global portions. These hypotheses are present in the fixed record; an arbitrary group acting on an arbitrary real line would not meet them.

For a matched source action and packet transport S with global monoid map k, the reconstruction is natural by the explicit calculation

\[
S(mE)=k(m)S(E),\quad L'(S(E))=L(E)+c_S
\ \Longrightarrow\ \ell'(k(m))=\ell(m).
\tag{P2}
\]

The fixed offset c_S cancels. Consequently the unit kernels, the cones, their real-ray maps and the pushed-out torsor localizations correspond. This is the specific reason the localization squares commute; merely knowing that two ordered Picard groups are isomorphic would not prove (P2).

At `K_0,L`, use the number-field Kummer maps of III 3.11(ii)(c), the packet-volume compatibility of (ii)(a), and the action compatibility of 3.10(ii)-(iii). For the full log-Kummer family, this uses its *matched admissible histories*, not an assertion that log is a scalar-linear map on arbitrary regions. Proposition 3.9(iv) and Remark 3.9.6 supply the small-region comparison and the inter-place conversion ratios. Thus the recovered divisor localizations and the global torsor degree comparison are compatible vertically in their stated domain.

For `T_L`, use the *same* theater permutation h and NF maps as stage 11:

`h_(j,v) ell_(0,j,v) ~ ell_(1,hj,hv) h_(N,j)`.

III 3.3.1 and 3.11(i)-(ii) give the associated number-field/action record and the packet transports. Apply (P2) to that jointly transported record, with the Ind1/Ind2 ambiguities retained. This recovers the corresponding localization maps; it does not synchronize independently chosen conjugacies or make every representative a strict square. Ind3 is still governed by the stipulated unit-domain histories. Nothing here applies a p-adic logarithm to a nonunit pilot.

Finally, `d_1^e` is the **same-presentation** MOD-to-mod map of III 3.7(ii)-(v). It transports the reconstructed localizations through the torsor/fractional-ideal identification; the local monoids are the same, and the map is the identity on the global rational-function group. This is a genuine last component of (P1). It is not a log-link-compatible identification of mod objects at all heights. III 3.10.1, pp.149-150, and 3.11.2(iii), pp.168-169, expressly distinguish those assertions.

II 4.6(v), p.139, supplies the compatible env/gau evaluation divisor maps used in A_i. Its ordinary Kummer comparison is useful in that square. Taking local multiplicative groups modulo local units there, then declaring the quotient unchanged by log, would bypass rather than prove the MOD construction. The reconstructed operations above avoid that step.

## 3. The native pilot: what can and cannot be substituted

Apply the abstract composite to the **given** class, not to a newly chosen principal class:

\[
z_0=\lambda_*^{-1}x_q,\qquad
z_\chi=(d_1^e)_*(T_L)_*(K_{0,L})_*z_0=\gamma_\chi(x_q).
\tag{P3}
\]

The pilot-preserving full-prime-strip maps and III 3.7(v), 3.8(i), pp.111-112, supply its abstract local divisor/pilot record. R now gives its source-model localizations. In particular the recipe is not stuck at the zero principal class: it operates on the *whole supplied torsor object*, with its local trivializations. At a fixed holomorphic presentation, a nonprincipal pilot can also be calculated directly from its splitting-generated fractional ideals. The degree of an ordinary unperturbed Theta-pilot in that presentation is therefore a meaningful calculation.

The attempted next substitution was to regard the reconstructed localizations of (P3) as the particular native-marked arithmetic object in the receiving determinant calculation. For this, the input marking must follow the **prescribed** coric arrow

`bar(alpha)=k_1 lambda_Delta k_0^(-1)`.

The chosen h has unit discrepancy

\[
\delta_1=\eta_1^{-1}\bar\alpha\eta_0(h_E^{\rm unit})^{-1}.
\tag{P4}
\]

Keep it; do not replace h by a second conveniently chosen endpoint identification. The full radial gluing absorbs delta_1 abstractly. The reconstruction computes kernels and valuations for the actions it is given; it does not turn an arbitrary unit-prime-strip automorphism into a specified action on the local modules defining D_H. In particular, calling delta_1 a unit automorphism does not identify it with multiplication by a valuation-zero field element.

The action intertwining in (P2) has been instantiated on the MOD components and on their jointly transported record. Across `lambda^-1`, the accepted map has type **full prime-strip isomorphism**. It has not been supplied as a map of the non-realified global fields with their receiving packet actions and marked arithmetic realizations. No such field map is demanded by the source's formal alternative. Its absence from this type nevertheless prevents applying (P2) to that arrow by substitution alone. The NF maps induced by h are not a new field map induced by lambda.

One can take an unperturbed receiving-theater Theta-pilot, or return from T_1^e using a fixed receiving Kummer presentation, and compute its ordinary arithmetic degree. This does not by itself verify that the resulting native-q comparison, including (P4), is the same permitted bounded/formal record. We therefore do not name that substitute `y_chi`, assert that all such substitutions fail, or report its ordinary Theta degree as the requested Gamma defect. This is a limitation of the completed instantiation, not a nonexistence assertion about marked specializations.

## 4. A concrete calibration test, rather than a renamed realization map

Here is a specific way to test the attempted substitution. Choose one bad finite place w. The native arithmetic divisor supported at w with scalar p determines a positive class c_(q,w); in the fixed native chart

`nu_q(c_(q,w))=kappa_w log(p)>0`.

Its relation to the native q-generator in the realified local ray is obtained using ord_p(q_v), with the field-degree factor in (R7). In the constructed MOD components, the analogous **prime component** of the divisor of p is recovered by (R6)-(R7), and its transport follows (P2). This supplies an independent nonzero reference inside those components. It corrects any suggestion that action reconstruction can never yield a nonzero calibrator.

More explicitly, at the native arithmetic input the signed line-class convention gives

\[
x_q=-M\sum_{w\in V_{\rm bad}}\operatorname{ord}_p(q_v)c_{(q,w)},
\qquad
z_\chi=-M\sum_{w\in V_{\rm bad}}\operatorname{ord}_p(q_v)
                 \gamma_\chi(c_{(q,w)}).
\tag{P4a}
\]

This is an equality in the realified global Picard groups, using the native local divisor presentation, not a claim that the q_v arise from one global field element. The rational coefficients are taken in the realified groups; no new roots or nonunit logarithms are taken. Applying R computes the corresponding *abstract divisor transport*. To turn (P4a) into a receiving degree calculation one must evaluate those transported classes in the independently marked receiving record. Since the global Picard line is ordered and one-dimensional, one correctly transported nonzero reference would suffice; all terms need not be separately realized. This is the concrete attempted computation of the native class and the point where its numerical evaluation stops.

For the entire comparison, the unverified step is to identify the image of this *native marked component*, or equivalently a calibrated nonzero multiple of x_q, in the **same receiving arithmetic/formal record as D_H**, with the action-calibrated component. A localizing map that commutes abstractly with lambda's divisor maps is not yet an equality between these two fixed numerical markings. In particular a theorem about the MOD part cannot be used to assert that lambda transports the native scalar p as the scalar p acting in the receiving packet.

This is a sufficient calibration test, not a requirement that the source transport every principal divisor or every object. The still weaker test on x_q alone is allowed: construct a permitted receiving datum y_chi and calculate or bound

\[
\Delta_\chi=\frac{\nu_{\rm rec}(y_\chi)-\nu_q(x_q)}M.
\tag{P5}
\]

The receiving chart in (P5) must be the independent corrected-determinant normalization, with all packet weights and inverse structural terms. It has not been defined by pulling back nu_q. No such jointly marked y_chi was constructed in this run, so **there is no numerical Gamma defect to report**. Positivity, preservation of integer multiples and the degree-zero product formula do not remove the issue. FrI 6.4(ii) permits a positive scalar on realified Picard lines; its stronger degree-one arithmetic-category hypothesis is not established for the mixed split/realified horizontal arrow.

## 5. Bound in the same record

The reconstruction has produced no selected local region, effective residual class, or indexed enclosing family connecting (P3) to D_H while preserving the required native marking. Its test regions E were probes of coefficient actions; they are **not** newly certified algorithm outputs. Choosing one with a desired volume would add no bounded-output provenance.

If the marked comparison supplied an effective residual Z_chi, then with `S_chi=nu_rec(Z_chi)/M>=0` the actual degree accounting would give `b-a=Delta_chi+S_chi`. No value or sign for an actual S_chi follows from this run's reconstruction. Likewise III 3.9.7 allows a formal inverse-system implementation, but no actual indices, compatible marked terms and error bounds were obtained here. Exact attainment, uniqueness, raw-output membership and transport of every orbit have not been imposed as necessary conditions.

Thus neither a calibrated effective comparison nor a calibrated bounded approximation has been derived. The original nontrivial inequality does not follow from the results obtained here.

## 6. Exact boundary after this attempt

* **Last constructed datum:** the explicit action-valued quotient and cone, the maps R_(i,m,j,v), their torsor-localization functors and their compatible MOD transport, together with the abstract pilot z_chi in (P3).
* **Operation attempted:** specialize that localized pilot, with the native coric marking (P4), in the receiving arithmetic/formal record used to form D_H, and evaluate it in that record's independently normalized degree.
* **Instantiated source clause:** III 3.11.2(iv), using 3.9.2, applies to the non-realified global group actions and MOD-derived LGP global portions already present at the actual endpoints. The calculation (R1)-(R7) supplies its localization conclusion. I 5.2(iv) identifies the exact divisor-map type; II 4.6(v) supplies the coupled evaluation maps.
* **Precise difference:** that conclusion reconstructs localization from an existing global/action record. It does not, through this derivation, select or verify the native-marked receiving torsor/formal term controlled by D_H after the horizontal/coric application. IPL/SHE asserts the broader relationship; its marked bounded application is not used here as its own proof.
* **Weaker possibility retained:** a source-selected marked term, or a compatible approximation with a sufficient lower bound on Delta, could close the comparison without a realization functor on all objects or a field map across the Theta-link. This run has neither constructed nor excluded it.

The adversarial checks therefore reject four shortcuts: promoting a principal class to a calibration unit; transporting the degree chart by definition; extending vertical MOD compatibility to mod across log; and assigning the boundedness of one choice to the calibration of another. cQ3 object localization is not changed into localization of a comparison morphism. The positive reconstruction is substantial but does not move the final realization boundary beyond stage 12. No faithful countermodel or fatal flaw is established.
