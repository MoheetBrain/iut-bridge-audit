# One adjacent local comparison and its quotient

## 1. Actual data and the limit of its reconstruction

Fix the given native column n=1, its distinguished coordinate (1,0), and the adjacent link `(1,0) --log--> (1,1)`. This choice does not move native Q. Fix one allowed bad nonarchimedean place `v_* in Vbad` above `v_Q`, the first nonzero packet index `j=1`, and its factor with label `|t|=1` in `S_2^±`. This is a symbolic specialization of the given initial data, not a numerical example or a replacement number field. The other packet factors, places, global object and localization maps are fixed parameters. If no bad place is present, this marked bad-place calculation is inapplicable; the unmarked good-place version omits q.

Take the native local field `k=K_v*`, its ring O, and its native splitting `s_q(r)=[q^r]`, with q the root specified in IUT I Example 3.2(iv), p.71. That passage places the root in K_v and specifies its torsion ambiguity. The q-pilot local component, its global pilot and localization marking are the retained data of [Q_SYSTEM](../07_formal_lift/Q_SYSTEM.md). The fixed allowed exponent M is the same on the pilot and corrected-determinant sides.

| Object | Actual source and status |
|---|---|
| Unit-domain pieces | Galois-invariant portions of `(Psi_cns(1,m F)_{|t|})_v*^times` for m=0,1; log only on its unit domain, as in Remark 1.1.1 and Proposition 3.5(ii)(a). |
| Kummer maps | The labeled isomorphisms `kappa_m: Psi_cns(1,m F)_t -> Psi_cns(1,circ D)_t` of Proposition 3.5(i). Choices belong to the given common theater/prime-strip data; they are not independent arbitrary automorphisms. |
| Common packet | `I(S_2^± F(1,circ D)_{v_Q})`, with its Q-span and label-1 action portion. Proposition 3.5(ii)(a) contains both direct Kummer unit images and the permitted one-log pre-composites. Containment is not equality of those images. |
| Local analytic chart | The chosen factor's unit-to-additive-log chart `O^times --log_k--> log_k(O^times)` inside the coric holomorphic model of Remark 3.9.4(iii)-(iv). Using this source chart does not identify two independent arithmetic-holomorphic realizations, nor make the Kummer triangle commute. |
| Splitting | The separate monoid action of Proposition 3.5(ii)(c), with overlap with log domains only through roots of unity. It does not send q through log. |
| Hull and determinant | For the actual bounded admissible output family P_B, `H_B=phi(P_B)` and `D_B=det^(tensor M)(H_B)`, with Ob3's weights and structural correction. This retains the source-defined family, not a constructed list of its members. |
| Native tuple | `q_M,v*` is the local q-power component; `q_M,g` and `rho_qM,v` remain fixed. Locally its marked ideal is `q^M O`. No claim about arbitrary Hom_lin or base arrows is used. |
| Shifted determinant tuple | No particular target hull H_+, target determinant D_+, or IPL-marked morphism into it has been reconstructed. This is not concealed by introducing arbitrary Y_- and Y_+. The relation below has explicitly smaller, numerical representative types. |

The first packet only selects a place to test the mechanism. It does not identify the entire native q-pilot with the LGP splitting monoid, or infer the global answer from its j=1 component.

## 2. Representative-level unit data

For a permitted joint choice c of the labeled source maps, let `D_c` be the actual unit-domain portion on which the one-log pre-composite in Proposition 3.5(ii)(a)(2) is defined. Denote the two source maps on this portion by `K_c^0` (direct Kummer) and `K_c^1` (one-log pre-composite). Their codomain is the same coric packet. On pure tensors this means taking the tensor products over |t|=0,1 prescribed by that proposition, with the other factors and their domains retained.

The witnessed unit relation is

`L_unit,c = { (K_c^0(u), K_c^1(u); u,c) : u in D_c }`.

Membership requires the same u, the actual domain restriction and the same joint choice c. Both images lie in the common packet by Proposition 3.5(ii)(a). This is a typed rewriting of an actual source correspondence; it does not assert that the two images coincide, or that their hulls have equal volume. The source also supplies injective charts on the single local analytic factor. We have not identified such a chart with a restriction of this particular labeled D_c: that would require the actual domain/chart comparison, including any S subset D_c condition in the chosen realization. Existence of a suitable joint witness for an IPL output is not inferred.

For a root of unity zeta and a unit u for which both inputs are allowed, `log_k(zeta u)=log_k(u)`. Proposition 3.5(ii)(c) supplies the separate splitting-action compatibility; its restriction of the overlap to torsion is essential. We do not replace it by `log(q u)=log(q)+log(u)` on nonunits.

## 3. An explicit Rss representative construction

Let E_- and E_+ denote the two endpoint **measure-space copies of k in the displayed coric-model chain** in Remark 3.9.4(iv), which the source uses to express one-log-step numerical compatibility. They are not asserted to be objects of the cQ3 upper category. Give them the source additive Haar normalization `mu(O)=1`. A final passage back to a differently labeled actual realization uses the source Kummer/Rss comparisons, not a ring identification invented here.

For a measure space E let Fn(E) be the finite-valued nonnegative Borel functions of relatively compact support used in Remark 3.9.4(i). Write

`I_E(f)=integral_E f`, `pi_E:Fn(E)->Rss(E)`,

where `pi_E(f)=pi_E(g)` exactly when `I_E(f)=I_E(g)`. The induced map `Ibar_E:Rss(E)->R_{>=0}` is a bijection.

By Remark 3.9.4(iii), choose a compact ample `S subset O^times` on which log_k is injective. This is a permitted auxiliary analytic chart, not an output of the multiradial algorithm. Put `S'=log_k(S)` and `s=mu(S)=mu(S')>0`. For an actual f in Fn(E_-), set

`t=I_E-(f)/s`, `h=t chi_S`, `g=t chi_S'`.

The complete representative witness is

`f --same-integral quotient--> h --push along log|S--> g`,

including S and the unchanged contextual labels Q,c. The tag c records the given link/Kummer choice; it does not prove that S is a chart for its exact domain D_c. The first step is precisely the source's quotient Fn->Rss, not a set map f->log(f). The second uses an actual injective unit-domain logarithm. For a fixed analytic chart S, with Q,c retained as contextual tags, this defines a relation on

`X_-= {Q,c} x Fn(E_-)`, `X_+= {Q,c} x Fn(E_+)`:

`L_Rss^S = { ((Q,c,f),(Q,c,g)) : g=(I_E-(f)/s) chi_S' }`.

The construction includes its quotient and chart witnesses; it is not defined by the desired inequality or by native-output membership. This is the representative relation for the source Rss construction, not yet an identified restriction or lift of L_unit,c. Varying S retains the chart witness. Any extension to the actual labeled unit correspondence must separately check jointly permitted choices; contextual tags are not a proof of that compatibility.

**Existence:** each f has the displayed witness because s>0 and Fn allows nonnegative real coefficients. For the native input use the actual function `f_r=chi_(q^(Mr) O)`, r in N. It has positive finite measure, so no zero-volume logarithm occurs. This supplies witnesses for the native **numerical representative**, not for an admissible IPL output.

**Consequence:** `I_E+(g)=t s=I_E-(f)`. Projecting the actual relation gives

`(pi_- x pi_+)[L_Rss^S] = graph(Phi_gamma)`,

`Phi_gamma = Ibar_+^(-1) Ibar_-`.

This is the isomorphism of Remark 3.9.4(iii)-(iv). Its independence of S follows from injectivity of Ibar_+, not from equivariance of arbitrary determinant automorphisms. For the source normalization factor d>0, define `nu=d log Ibar` on positive classes. Then `nu_+ Phi_gamma=nu_-`. Zero maps to zero and has value -infinity; it is excluded from the real-valued native-pilot calculation.

**This construction does not manufacture admissible outputs.** The weighted characteristic function g is only an Rss representative. It may be neither a characteristic function nor an arithmetic hull, let alone a member of P_B. No such assertion is made. The source expressly permits non-hulls at intermediate Rss steps (Ob9), but that permission alone does not put their endpoint classes into the IPL output family.

## 4. The native marking and its precise scope

In the fixed native/coric presentation put `e_q,M(r)=pi_-(chi_(q^(Mr) O))`. By the source normalized valuation formula (Remark 3.9.4(iv), p.124),

`nu_-(e_q,M(r)) = -Mr ord_v(q) log(p_v)`.

Applying the constructed comparison proves

`nu_+(Phi_gamma(e_q,M(r))) = -Mr ord_v(q) log(p_v)`.

Thus it preserves the **given** local native value, not just an unspecified real number. Replacing the allowed generator by zeta q leaves the ideal and its class unchanged. Q, its coordinate, the permitted Kummer path, and its localization tags remain attached to the witness. No equality with an independently chosen q at coordinate (1,1) is asserted.

This calculation proves existence of the native numerical image in the Rss codomain: the class Phi_gamma(e_q,M(r)) has an explicit witness. It does **not** prove coverage by the restricted algorithmic output family, or that its representative descends from the actual IPL marking through the formal quotient. That distinction is the remaining issue.

Finite-extension and tensor compatibility are the stated constructions in Remark 3.9.4(iii),(v), pp.123-125; positive fixed packet weights and the procession average preserve the resulting equalities. The Galois/unit identifications are retained from Proposition 3.5 and Theorem 3.11(ii), but Fn->Rss itself forgets them (iQ5). Attaching their provenance as tags records what was used; it does not reconstruct their action from a volume class. No new global localization square is proved by this local computation. Global MOD isomorphisms remain the source's positive result; they are not substituted for mod comparisons.

For actual admissible hulls H, Ob3 identifies their correctly normalized determinant degree with the corresponding volume. Conditional on the relevant marked admissible hull comparison having been supplied, the Rss equality can therefore be used at that numerical stage without recovering every element of T_B. It gives no inclusion H_- subset H_+, no native-output witness, and no bound by b on its own.

## 5. Quotient soundness and composition

For an arbitrary constructed representative relation L, its quotient image always exists. This fact does not require function-level equivariance. It also does not imply preservation of witness compatibility.

At the **Rss-only** level, the graphs just proved compose correctly: `Phi_12 Phi_01=Ibar_2^(-1) Ibar_0`. The quotient projections have equality-of-integrals fibers. More concretely, the second chart relation is defined on every Fn(E_1): feed it the actual first output g_1, with the same middle measure space and compatible unchanged tags. Thus `(pi_0 x pi_2)[L_12 composed L_01]=graph(Ibar_2^(-1) Ibar_0)` already follows from a matched representative chain. No re-representation of the middle record is needed. This is a statement about the entire source Rss quotient, not about a subset of admissible marked IPL histories.

For marked admissibility retain a chain `(c,f_0,S_01,g_1,f_1,S_12,g_2)` together with the actual permitted identification of the middle records. Equality of their volumes or determinant orbits alone is not that identification. If no matching rule is proved, form the representative fiber product first and only then quotient. The weaker inclusion law from E3d.2 remains an inclusion.

For identity comparisons use the diagonal representative relation `L_id={(x,x)}` and the identity on all native tags. Its quotient is the diagonal on the marked quotient. The log-chart construction also induces the identity between identical normalized Rss copies, but its weighted representatives need not be identical; confusing these two levels would fail Control A.

The counterexample in Control B demonstrates why Rss coherence cannot itself supply the missing correlated IPL witnesses. Our local Rss calculation is sound at its declared quotient; the extension to the marked output family is not claimed.
