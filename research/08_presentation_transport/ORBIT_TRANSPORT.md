# E3d.2: transport of cQ3 structure-morphism orbits

This file freezes E3d.1 and proves the smaller transport statements that follow from actual functors or linear comparison morphisms. It does not construct a universal formal-system category. The first required transport not reconstructed is the cQ4 log adjustment; see [CQ4_TRANSPORT.md](CQ4_TRANSPORT.md).

References are to the pinned [III](../../sources/primary/IUT_III.pdf), [FrI](../../sources/primary/Frobenioids_I.pdf), and [FrII](../../sources/primary/Frobenioids_II.pdf). All page numbers are printed/PDF pages. The transition inventory, including optional changes, is [PRESENTATION_TRANSITIONS.csv](PRESENTATION_TRANSITIONS.csv).

## 1. Frozen fixed-presentation calculation

At each fixed admissible presentation B, retain exactly

`T_B(Y)=∏_v Aut(D_B,v)\Hom_lin,C_v(Y_v,D_B,v)`,

`T_B(f)(([a_v])_v)=([a_v f_v])_v`.

Here `D_B,v=det^(⊗M)(φ(P_B))_v` uses the corrected determinant; linear means Frobenius degree one. An upper arrow f:(Y,a)→(Z,b) satisfies

`[b_v f_v]=[a_v]`,

and its ambient localization equation is

`loc_v(f_g) ρ_Y,v = ρ_Z,v r_v(f_v)`.

Thus `C_B≅∫T_B` over C_q,B^loc-lin, as proved in [E3d.1](../07_formal_lift/CQ3_FUNCTOR_OR_PAIR.md). All claims below concern fixed Frobenioid presentations, with the given archimedean torsion-system comparisons retained; no interchange of orbits and limits is asserted.

## 2. A functional transport lemma, with its necessary input exposed

Suppose a presentation comparison supplies local functors F_v:C'_v→C_v preserving linear arrows, a global functor F_g:C'_g→C_g, local realification functors F_v^R:R'_v→R_v, and natural isomorphisms

`c_v:r_v F_v ≅ F_v^R r'_v`, `d_v:F_v^R loc'_v ≅ loc_v F_g`.

The prime labels are matched; a permutation can be incorporated by reindexing v. These data define F:C_q,B'→C_q,B by

`ρ_FY,v = d_v,Yg ∘ F_v^R(ρ_Y,v) ∘ c_v,Yv`.

Suppose also that the comparison supplies linear arrows

`h_v:F_v(D_B',v)→D_B,v`

such that, for each σ∈Aut(D_B',v), there exists t∈Aut(D_B,v) with

`h_v F_v(σ)=t h_v`.                                            (E)

This is a sufficient equivariance condition, not claimed necessary. Then

`τ_Y:T_B'(Y)→T_B(FY)`, `τ_Y([a_v])=([h_v F_v(a_v)])_v`.         (T)

The five checks are explicit:

1. Replacing a_v by σa_v changes the result by t using (E), hence leaves its target orbit unchanged.
2. F_v(a_v) and h_v have Frobenius degree one; their composite is linear.
3. For f:Y→Z and b∈T_B'(Z), associativity and functoriality give `T_B(Ff)(τ_Z(b))=τ_Y(T_B'(f)b)`.
4. Naturality of c_v,d_v transports the ambient localization square to the displayed square for FY. The new structure-map orbit is precisely a permitted local field in that same global tuple; it does not manufacture a global object from local data.
5. For a second comparison G from B'' to B' with comparison k, use F∘G and `h_v F_v(k_v)`. Condition (E) is closed under this composition, and its orbit transport is the composite of (T). If the source functors compose only up to natural isomorphism, the equation holds after that specified identification of the ambient objects, not as an equality of differently typed sets.

If h_v is an isomorphism, (E) follows with `t=h_v F_v(σ) h_v^−1`. Two isomorphism choices h_v differ by target postcomposition and give the same orbit map at fixed F. A natural isomorphism between choices of F also identifies the transports after reindexing Y by its component. For an arbitrary noninvertible h, (E) must not be assumed merely because h exists.

For a full prime-strip isomorphism in IPL, the ambient local/global functors and their unit/Galois/localization structure are available. The lemma applies to a **transported** determinant target. It does not show that a determinant independently computed from an additive region on the other side of a Θ-link equals that transported target. IPL precedes that determinant construction on the audited route.

## 3. A relation when an actual linear h is supplied

Without (E), the same F and linear h still give a well-defined relation with values

`R_h,Y([a])={([h_v F_v(σ_v a_v)])_v : σ_v∈Aut(D_B',v) for every v}`. (R)

This is a subset of T_B(FY). It retains all possible outputs of representatives; it is not asserted to be a function to T_B(FY). Replacing a_v by σ'_v a_v merely reindexes σ_v, proving independence from orbit representatives. Every output is linear. For f:Y→Z, taking direct images of these subsets gives the exact law

`T_B(Ff)[R_h,Z(b)] = R_h,Y(T_B'(f)b)`.

Localization is transported by F just as above. The relation uses the actual automorphisms allowed by cQ3, not a new action on native Q.

There is a precise weaker composition law. For consecutive (G,k),(F,h), the relation of the composite comparison hF(k) is contained in the composite relation:

`R_(hF(k)),Y(a) ⊆ ⋃_(b∈R_k,Y(a)) R_h,GY(b)`.                  (C)

Indeed the right-hand side allows an additional automorphism of the intermediate determinant; taking it to be the identity gives the left-hand side. Equality is not claimed without an absorption argument. If (E) holds for both comparisons, both relations are graphs of the functions in Section 2 and equality follows. For a genuinely relational path, keep the intermediate witness and use associative relational composition; do not identify that path with a shortcut by fiat.

This construction follows from the frozen orbit definition whenever F,h are actually supplied. It is not a claim that an arbitrary set correspondence supplies h or that every relational output is the returned IPL marking.

## 4. Positive powers: supplied forward transport

III Ob3–Ob4, pp.131–134, use the corrected determinant and the naive Frobenius functor. FrI Proposition 2.1(i),(ii), p.44, supplies Ψ_d on objects and arrows, up to natural isomorphism. With Frobenius-type arrows α_A:A→Ψ_d A of degree d, its equation is

`Ψ_d(a) α_Y = α_D a`.

For a linear a, multiplicativity of degree gives `deg_Fr(Ψ_d(a))d=d`, hence Ψ_d(a) is linear. Functors send automorphisms to automorphisms, so

`[a] ↦ [Ψ_d(a)] : T_B(Y)→T_Bd(Ψ_d Y)`                        (P)

is well-defined, where D_Bd is identified with Ψ_d(D_B). This is the **forward** direction; it has the request's convention after relabeling its domain B' and codomain B. The degree-d arrows α themselves are not asserted to be locally linear when d>1.

Local/global power constructions commute with localization as in III Ob4, p.133: in the arithmetic-line models, restriction of L^⊗d and of a^⊗d is the d-th power of the restriction. This supplies c_v,d_v for (P), including the realified global tuple. Galois equivariance and the unit action are transported through the functor. In Frobenius-normalized models the unit map is u↦u^d (FrI 2.1(ii)); it is not called an isomorphism of all original unit data. The ×μ/root bookkeeping is retained.

FrI 2.1(i) gives `Ψ_e Ψ_d≅Ψ_ed`. The comparison identifies the two orbit transports. Coherence of choices can be seen using the defining Frobenius arrows: the isomorphism intertwining the composite arrow and the chosen degree-ed arrow is unique by FrI Definition 1.3(ii). The two further-composition comparisons satisfy the same intertwining equation and hence agree. Thus no strict choice of roots or of a representative [a] is needed.

This also applies to replacing M by a divisible multiple dM when the corrected determinant weights are all multiplied by d. It does not mean that arbitrary normalizations may be changed without updating q_M to q_dM.

## 5. Roots and twists: a conditional cospan, not an inverse

Ob4-2/3, pp.133–134, describes copies over a powered Frobenioid with tensor-root twists. It does not license inversion of Ψ_M: FrI 2.1(iii) requires perfectness for that conclusion, and Ob4-2 explicitly notes the relevant finite-place nondivisibility.

When rooted **objects and markings** are supplied in two root presentations R_i (i=1,2), write

`δ_i:Ψ_M(D_i)≅D_p`, `η_i:Ψ_M(Y_i)≅Y_p`.

Require η_i to be isomorphisms of whole local/global collections. The forward maps are

`p_i:T_Ri(Y_i)→T_p(Y_p)`, `p_i([a_v])=[δ_i,v Ψ_M(a_v) η_i,v^−1]`.

The relation is the fiber product of sets `p_1(a_1)=p_2(a_2)`. Sections 2 and 4 prove representative independence, linearity and naturality for arrows compatible with η_i. Localization follows from the whole-tuple η_i. A root-presentation isomorphism over the powered data preserves these images. Chains retain the common powered image and intermediate root witnesses; equality of the endpoint images alone is not claimed to supply every intermediate witness.

This is a typed consequence **conditional on δ_i,η_i and rooted objects**; it does not establish an M-th root of every determinant or a canonical comparison of all roots. In the minimal route one may remain at the power M and compare with q_M, as Ob4 expressly permits. Extracting roots is therefore not an earlier mandatory obstruction.

## 6. Hulls, collapse, enclosures and Ind1/2

At fixed arithmetic realization and exponent M, actual inclusions of admissible hulls H⊆H' induce linear local determinant maps D_H→D_H'. If transport between the two target presentations is needed, Section 3 supplies the relation with F=identity and this h. Its localization tuple Y is unchanged. It does not assume that every automorphism of D_H extends across h. When actual maps all land in a common D_B, they are simply objects/arrows of the already fixed C_B; no change of presheaf is required.

III (vi), Ob5 and cQ3 allow using the common H_B and D_B for the whole bounded family of possibilities. Thus Ind1/2 choices need not be promoted to separate endofunctors of a holomorphic Frobenioid. The family, its admissibility and boundedness remain hypotheses; this audit does not establish a bound for an unrestricted union. Native Q is not moved. For a particular change induced by a full arithmetic isomorphism, Section 2 applies; a general mono-analytic Ism action is not assumed to be such an isomorphism.

The collapse in (v),(vi) has a genuine set-level rule; its cQ3 presentation has the genuine U_B. It supplies no inverse to forgetting or automatic transport between arbitrary fibers. Formal empty intersections remain unevaluated. We do not require every map of subsets to have a determinant or claim that their images form ordinary cQ3 arrows. The unresolved formal intersections arising in the log domain are included in the cQ4 test, rather than repaired by a universal formal-system construction.

Enclosing-region refinements from Remark 3.9.7(ii),(iii), pp.146–147, are conditional approximation data. On a chosen pair of admissible regions with inclusion and finite-volume hulls, monotonicity of φ yields the preceding determinant comparison relation. This does not establish cofilteredness, compatibility for all refinements, or the native-q section. No exact minimizer is demanded.
