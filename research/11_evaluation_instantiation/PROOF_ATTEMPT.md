# Evaluation compatibility on the fixed Theta/q pair

**2026-10-03. Verdict: PRECISE_APPLICATION_STILL_UNRESOLVED.**

This is one proof attempt from explicit accepted source results. It constructs a joint radial lift, instantiates evaluation and localization, and writes the abstract input-to-output prime-strip composite. It does not construct the required native-marked bounded hull comparison. Source IDs, hashes and access limits are in [LITERATURE_DELTA](LITERATURE_DELTA.md); map-level substitutions are in [INSTANTIATION.csv](INSTANTIATION.csv). `Y18` always denotes the inspected 2018-path PDF, not the newer revision.

## 1. Fixed data and types

Fix the initial Theta-data and the given LGP log-theta-lattice of Y18 Theorem 13.12, pp.345-351. Substitute **n=0, n+1=1, m=0**, exactly as in Corollary 13.13's proof, p.353. The LGP construction at `(i,0)` retains its preceding log-link `(i,-1)->(i,0)`; m=0 does not remove that link or the full log-Kummer family.

Write `H_i` for the vertically coric D-Hodge theater at `(i,circ)`. Keep all places v, packet indices j, cusp labels t, their symmetrizing maps, localizations, and the gluing of the Theta- and NF-bridges. A theater isomorphism transports its labels; it does not identify the two arithmetic-holomorphic realizations. Write `B_q` for the full receiving q-pilot prime-strip at `(1,0)` and

\[
\lambda:L_0^F\xrightarrow{\sim}B_q
\tag{1}
\]

for a representative of the given full Theta-link. Here `L_0^F` is the **full** LGP prime-strip, including the global realified portion, splitting and units. Such morphisms take its pilot to the receiving pilot by the pilot construction (IUT II Definition 4.9(viii), p.158; Y18 Definition 13.9, pp.338-340). This is a structured isomorphism, not an identification of numerical volumes across two rings.

For `i=0,1`, let `U_i = (i,0)F_Delta^(ell x mu)` and `C_i=(D_i^ell,F_Delta^(ell x mu)(D_i^ell))`. Denote the Kummer map of Theorem 12.5(3) by `k_i:U_i -> C_i.unit`. The induced unit portion of (1), with the source's natural identifications, is `lambda_Delta:U_0 -> U_1`. Thus the prescribed coric arrow has unit component

\[
\bar\alpha_{\rm unit}=k_1\lambda_\Delta k_0^{-1}.
\tag{2}
\]

Its D-prime-strip component is the induced base map. It remembers the local Galois/unit quotient data and its auxiliary Kummer structures; it does **not** contain the radial theater, the evaluated Gaussian splitting, the NF localization family, a native pilot degree, or a bounded hull.

## 2. A joint radial lift really exists

Y18 Corollary 12.8, pp.317-320, defines

\[
R_i=(H_i,E_i,R_i^{\rm bad},C_i.{\rm unit},A_i),
\qquad A_i=\operatorname{Isom}(E_i^{\rm unit},C_i.{\rm unit}).
\]

`E_i` is the env F-prime-strip; `A_i` is the **full poly-isomorphism**, not a chosen rigid map. The bad data includes the splitting monoid, torsion, cyclotome, mono-theta projective system and zero-label splitting. The functor `Phi` remembers `C_i`. These are groupoids; the fixed initial data and Corollary 12.8(1)-(2) give the connected setting and fullness. IUT III Corollary 2.3, pp.72-75, has the same construction.

**Elementary derivation.** Choose one theater isomorphism `h:H_0 -> H_1` supplied by the etale permutation picture. It induces `h_E` and `h_bad`. The tuple

\[
u=(h,h_E,h_{\rm bad},\bar\alpha_{\rm unit})
\tag{3}
\]

is a radial morphism: the only remaining gluing condition is compatibility with the full `A_i`. Explicitly,

\[
\bar\alpha_{\rm unit}A_0=A_1h_E^{\rm unit}
\tag{4}
\]

as sets of arrows. Given `a_0 in A_0`, choose `a_1=bar(alpha)_unit a_0 (h_E^unit)^(-1) in A_1`; then `bar(alpha)_unit a_0=a_1 h_E^unit`. This checks the condition, not just the theorem title, and `Phi(u)=bar(alpha)`.

For any two lifts u,v, `k=u^(-1)v` lies in `ker[Aut(R_0)->Aut(C_0)]`, and `v=uk`. Conversely every such uk is a lift. This proves the torsor assertion without uniqueness. It does not identify this kernel with Ind1, Ind2 or Ind3.

**Important limit of (4):** it is not the equality `bar(alpha)_unit eta_0=eta_1 h_E^unit` for the particular native Kummer identifications `eta_i`. The discrepancy is the concrete unit automorphism

\[
\delta_1=\eta_1^{-1}\bar\alpha_{\rm unit}\eta_0(h_E^{\rm unit})^{-1}
\in\operatorname{Aut}(E_1^{\rm unit}).
\tag{5}
\]

Here `eta_i` is obtained by inverting the Delta-to-env identification of Proposition 12.6(3). Fullness absorbs (5) in the abstract gluing, without proving a strict lift to every arithmetic realization. Theorem 12.7(1), p.316, explicitly asserts surjectivity for the **second** of its two automorphism homomorphisms; it must not be cited as surjectivity of the first. No strict extension of every delta_1 to an env Frobenioid is required here.

## 3. Actual evaluation and NF equations

Write superscripts F and e for Frobenius-like and etale-like realizations. For each bad place and permitted value profile xi, Corollary 11.17(2)-(3), pp.278-279, and Corollary 11.21(4)-(5), pp.292-293, give evaluation from theta monoids to their **Gaussian value monoids**, not directly to `B_q`:

\[
K_{i,G}e_i^F=e_i^eK_{i,E},\qquad
e_i^F:\Psi_{Fenv}(i,0)_v\longrightarrow\Psi_{Fgau}(i,0)_v.
\tag{6}
\]

The infinity/rational versions are retained where the source uses them. These are equations of the compatible systems, with their specified conjugacy and torsion ambiguities. The source chooses synchronized conjugacy across t, not independently for every packet factor. The same `h` transports xi, t and v and induces the evaluation square

\[
h_G e_0^e\simeq e_1^e h_E.
\tag{7}
\]

The symbol `simeq` means the source's natural, possibly 1-compatible collection with those ambiguities, not equality after independently choosing representatives. Proposition 12.6(2) gives Kummer isomorphisms including the global realified structures and their localizations; (3) checks their unit restriction against k_i. Thus (6)-(7) are jointly typed with (2), not a second unrelated existential choice.

For the NF part put

\[
N_{i,j}=\{\pi_1^{rat}(D_i^{\circledast})\curvearrowright
\mathbb M_{\infty\kappa}^{\circledast}(D_i^{\circledcirc})\}_j,
\quad \ell_{i,j,v}:N_{i,j}\longrightarrow M_{\infty\kappa v}(D_{i,vj})
\subseteq M_{\infty\kappa\times v}(D_{i,vj}).
\]

These spell out the decorated objects in Y18 13.12(3)(d); they are pseudo-monoids with actions/localization poly-morphisms, not simply unstructured real numbers. Corollary 11.22(3), p.295, applied to `H_0,H_1`, yields, for the **same** h,

\[
h_{j,v}\ell_{0,j,v}\simeq\ell_{1,hj,hv}h_{N,j}.
\tag{8}
\]

Corollary 11.23(1)-(3), pp.296-298, supplies its Frobenius-like Kummer version. The source carries localization and prime-index bijections globally; (8) does not arise by freely assembling local isomorphisms. Its NF diagonal is a formal family of symmetrizing maps (Remark 11.22.1), not a newly synchronized product of all local representatives.

**What 13.12(3)(c)-(d) adds.** At n=0,m=0 these evaluation/localization constructions, with (2), are compatible with the horizontal full poly-isomorphism `U_0 -> U_1` after Ind1/2/3 (Y18's turn/right/up indeterminacies). The more explicit IUT III 3.11(iii)(c)-(d), pp.157-159, quantifies over any etale permutation and arbitrary endpoint automorphisms: the **constructions** are equivariant after those indeterminacies. In notation for that assertion,

\[
\mathcal A(g_1\lambda_\Delta g_0^{-1};g_0,g_1\text{-transported data})
\simeq g_*\mathcal A(\lambda_\Delta;\text{data}).
\tag{9}
\]

Here `A` denotes the source's whole compatible construction, including both (7) and (8). Equation (9) records its algorithmic equivariance; it is not a newly proved equality of sets of measurable output regions. It is stronger than three separate existence statements, but does not say every arbitrarily chosen representative commutes strictly. IUT III Remark 3.11.4, pp.171-172, explains why torsion orbits and entire NF sets are used. We accept this source result at its stated scope, rather than demanding exact representatives.

The final sentence of Y18 (d) prints `(2b)` although its NF comparison belongs to `(2c)`; IUT III (iii)(d) explicitly points to (ii)(c). This is a located reference discrepancy, not an alleged mathematical obstruction.

## 4. One typed diagram and the constructed composite

For full prime-strips set `E=env`, `G=gau`, `L=LGP`, `T=lgp`; let `e:E->G`, `t:G->L`, `d:L->T` be the source evaluation and natural maps. Their local/global structures are supplied by Y18 11.21, 13.8, 13.11 and IUT II 4.10(ii). IUT III Remark 3.10.2, p.152, gives the following diagram (displayed for i=0; the i=1 row has the same form):

```text
 E_0^e --e_0^e--> G_0^e --t_0^e--> L_0^e --d_0^e--> T_0^e
   ^ K_0,E         ^ K_0,G         ^ K_0,L           ^ K_0,T
   |               |               |                 |
 E_0^F --e_0^F--> G_0^F --t_0^F--> L_0^F --d_0^F--> T_0^F
                                    |
                                    | lambda: given Theta-link
                                    v
                                   B_q   [native pilot Q fixed]

 E_0^e --h_E--> E_1^e --e_1^e--> G_1^e --t_1^e--> L_1^e --d_1^e--> T_1^e
                                                                   |
                   P_Theta --union/hull--> H_Theta                  : unresolved
                                            |                      : native marked
                                            v                      : realization
                         D_H = corrected det^M(H_Theta) <...........+
```

Every solid horizontal/vertical arrow is between full prime-strips except the explicitly separate hull/determinant line. The dotted connection is not a constructed arrow. In particular this is not a set map carrying a region across a non-ring-theoretic Theta-link.

Put `A_i^F=t_i^F e_i^F` and `A_i^e=t_i^e e_i^e`. Commutativity within each theater gives

\[
K_{i,L}A_i^F=A_i^e K_{i,E}.
\tag{10}
\]

Choose the Kummer and localization representatives as a single compatible record chi. Using inverses of actual isomorphisms, define

\[
\Gamma_\chi=
d_1^e A_1^e h_E K_{0,E}(A_0^F)^{-1}\lambda^{-1}:
B_q\longrightarrow T_1^e.
\tag{11}
\]

This is the linking path described in IUT III Remark 3.11.1(iii), pp.160-161, with the etale permutation inserted explicitly. Each adjacent endpoint matches. By (10), with `T_L=A_1^e h_E(A_0^e)^(-1)`,

\[
\Gamma_\chi\lambda=d_1^e T_L K_{0,L}.
\tag{12}
\]

Consequently (11) transports the native pilot to the abstract pilot image described by the evaluated source side. It preserves the local-global isomorphism-class data by construction. It does **not** yet identify its receiving holomorphic realization, or its normalized degree, with a datum controlled by `D_H`. An abstract full prime-strip isomorphism must not be silently identified with a normalized-volume-preserving map of its realized regions.

There is an additional qualification at precisely this passage: IUT III 3.11.1(iii), p.161, interprets the final evaluation as a global realified Frobenioid with pilot rigidifications **subject to** the sign conditions of 2.4.2(iv),(vi), the product-formula considerations of 3.9.6, and the inverse systems of direct-product regions of 3.9.7. Formula (11) constructs the prime-strip composite; it does not discharge these conditions for the particular bounded native specialization. They remain part of that application's obligations.

The joint record is `(lambda,k_0,k_1,h,u,a_0,a_1, Kummers, evaluations, NF localizations, permitted log-domain histories)`. Equations (4), (6), (8), (10) couple it. Equivariance (9) is accepted for the associated formal family. There is no claimed joint record for the dotted arrow.

## 5. Uniform enlargement: the attempted last step

Define `P_Theta` to be precisely the raw possibilities stipulated in 13.12(1)-(2), and `H_Theta=Hull(union P_Theta)` in the receiving arithmetic structure. They are not all abstract radial isomorphisms and not all Rss representatives. The source explicitly includes procession automorphisms (Ind1), the indicated Ism/archimedean actions (Ind2), and domain-restricted log-Kummer histories (Ind3). Proposition 13.7(2), pp.334-336, supplies the unit inclusions/surjections and the splitting action, with only torsion overlapping log domains. These are genuine inclusion statements. Theorem 13.12(1) supplies the induced procession transport. Neither statement permits arbitrary tensor powers of the theta function or independent local/global histories.

**Elementary enlargement test.** If a jointly admissible realized comparison is already one of the stipulated possibilities, its region is contained in the union and hence in H_Theta. If it is obtained by a transformation T, sufficient facts would be `T(P_Theta) subseteq P_Theta` and compatibility of T with the relevant hull operation. For a semilinear isomorphism carrying the coefficient ring and integral structure to the target ones, hull compatibility follows by carrying each finite linear combination to the corresponding combination; the reverse inclusion uses T inverse. At archimedean places the prescribed norm/ball structure must also be retained. No such semilinear identification across the Theta-link is asserted. Algorithmic equivariance (9) instead permits a formal construction, which is why the region-level argument cannot simply replace it.

**Exact application still open.** Apply the permitted formal family (11), with its prescribed coric arrow (2) and compensation (5), to the particular **bounded corrected determinant**

\[
D_H=\det^{\otimes M}_{\rm corrected}(H_\Theta)
\]

and the receiving native pilot `Q_M`. IUT III Remark 3.9.5(ix), cQ3/cQ4, pp.141-144, proposes the local-global formal category pair at D_H and the log adjustment. We have not constructed the specialization of (11) in that pair which still carries the original native marking. At the exact-object level, this would require the appropriate local structure poly-morphisms into D_H and their common global localization record after cQ4. That is a **sufficient representative implementation**, not a demand that the source use one strict object; its formal/approximate implementation is also allowed.

The definition of cQ3 produces the ambient categories and unit/Galois actions from a given D_H. It does not, by that definition alone, select the native object in them. Composing (11) gives an abstract linked pilot, but does not give those structure poly-morphisms or a compatible approximation. Conversely, the source explicitly asserts a closed loop in (ix) and IPL/SHE in 3.11.1; failure of this reconstruction does not negate those assertions. We have checked their content, not used their endpoint coverage as a premise.

**Attempt to obtain the missing datum by transport.** Grant provisionally a source-compatible realization `F_v` of the evaluated composite in the local Frobenioid containing `D_H,v`, coupled to a global realization `F_gl`. At the exact-object level, transporting cQ3's category back along an equivalence gives objects mapping to `F_v^(-1)(D_H,v)`. In particular its identity gives a bounded object with compatible automorphism orbits. For the fixed native object, however, full faithfulness only gives

\[
\operatorname{Hom}_{\rm lin}(F_v(Q_{M,v}),D_{H,v})
\cong
\operatorname{Hom}_{\rm lin}(Q_{M,v},F_v^{-1}(D_{H,v})).
\tag{13}
\]

An equivalence preserving the indicated linear morphisms transports this Hom-set and its structure-poly-morphism orbits; it does not prove that the Hom-set is nonempty. The identity above has a different domain unless the needed comparison has already been supplied. Independent local choices would also leave cQ3's `(lc-gl_3)` localization isomorphisms and their common global object to be checked. Thus this direct transport proof stops at an explicit local morphism datum and its global assembly, even after granting the realization. cQ4 supplies compatibility of vertical adjustment with unit/Galois data and permitted log iterates; its wording does not independently construct that datum. This tests an exact-object implementation only. The source's pair of categories `(fQ_1,fQ_2)` and its formal/approximate alternative are not replaced by a nonemptiness requirement for one strict representative.

This locates the remaining application more narrowly than an unspecified missing lift: **restriction of the concrete evaluated composite (11) to the D_H-bounded local-global formal comparison while fixing the given native realization**, including the effect of (5). No equality between the fullness kernel and the permitted enlargement, and no extra convenient realization in P_Theta, has been assumed. V has not been postulated.

## 6. Degree bookkeeping and circularity control

Theorem 13.12(2) and Proposition 13.10, pp.340-342, supply packet/procession normalized log-volume and its local-global sum. The corresponding IUT III inputs are 3.9 and 3.11(ii). MOD has precise multiplicative log-Kummer comparison; mod retains upper semi-compatibility. NF localization in (8) and all finite and archimedean terms must remain in a single record. IUT III Corollary 3.12(xii), pp.185-186, explains why local object isomorphisms alone do not fix this calculation.

Use the source root `underline(q)_v=q_Tate,v^(1/(2 ell))` modulo the prescribed torsion. The already reconstructed local Rss value is `-M r ord_v(underline(q)_v) log(p_v)`; no repeated proof or experiment is performed. The positive M is the common permitted determinant exponent, with packet weights and the inverse structural determinant in Ob3, pp.131-133. It is not a new M-th-power theta-function construction. Normalize the corrected global degree by the same M and the source weights. This makes its log-volume comparable **once the missing marked formal application has been supplied**.

In particular no inequality `a_q=-|log q| <= b=-|log Theta|` follows here. Conditional on an independently constructed source comparison, either `a_q<=LV(V)<=b` or admissible approximants `a_q-epsilon<=LV(V_epsilon)<=b` would suffice. Neither is a definition of admissibility, and b is not asserted to be the supremum of raw-output volumes.

For the requested circularity control, in a common measured realization with `0<mu(H)<infinity` and finite `mu(Q_M)`, the existence of measurable `0<=g<=1_H` with integral `mu(Q_M)` implies `mu(Q_M)<=mu(H)` by integration. Conversely that inequality gives `g=[mu(Q_M)/mu(H)]1_H`. Thus inventing g in this way assumes exactly the needed inequality. The Rss representative only fixes the integral, not domination or arithmetic provenance. This control is not a countermodel to IUT.

## 7. Boundary of the result

Derived from the accepted constructions: the prescribed coric lift and its ambiguity, the jointly chosen evaluation/localization diagrams, and the explicit abstract prime-strip composite (11)-(12). Accepted rather than independently re-proved: the anabelian/Kummer algorithms, their family equivariance and the source degree normalizations. Unresolved: their native specialization in the particular bounded formal hull/determinant comparison. No fatal flaw, nonexistence theorem, global inequality or source equivalence beyond the cross-check in [VERDICT](VERDICT.md) is established.
