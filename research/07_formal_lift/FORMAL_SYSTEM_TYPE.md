# Formal region systems: recovered records and the first unresolved type

**FORMAL_SYSTEM_TYPE_UNRESOLVED.** Two precise set-level records and the fixed cQ3 functor can be recovered. Their assembly into the actual IPL output system, with its permitted changes of presentation, has not been reconstructed. This is an audit boundary, not a claim that IUT admits no such assembly.

All III references are to the pinned [IUT III PDF](../../sources/primary/IUT_III.pdf); printed and PDF page numbers agree. The symbol `FormalSys_B` is reserved for a source-justified formal output category. It is **not defined** by simply declaring it to be Pro(C_B), a stack, or the category of all diagrams.

## A. Formal intersections in Remark 3.9.5(v), pp.129–130

The given data are a set E, a proper subset S⊂E with |S|≥2, and the collapse map

`π:E→(E\S) ⊔ {S}`.

For nonempty A,B⊆S, any set map A→B induces the identity between their singleton images. Such a map need not commute with the original embeddings into E. Therefore the arbitrary maps in the first assertion are not automatically morphisms in Set/E. They commute with the maps to E/S after collapse.

A precise raw record for a displayed formal intersection is

`FI(E,S;I,A) = (I, (∅≠A_i⊆S)_i, (A_i↪E)_i)`.

Here I is the chosen nonempty indexing set. Its star-shaped diagram has objects i∈I and an ambient object *, arrows i→*, and values A_i and E. This records the fiber-product expression **without evaluating it**. An additional given inverse diagram can similarly be retained with its actual indexing category and arrows; no universal choice of such a category is stipulated in (v).

The evaluated intersection may be empty. After replacing each nonempty leaf by its image {S}, the formal intersection over E/S has value {S}. This is a rule for the formal expression, not the assertion π(∅)={S}. Nor is the ambient object E/S itself replaced by {S}.

For example E={a,b,c}, S={a,b}, A={a}, B={b} gives an empty ordinary fiber product A×_E B and a singleton fiber product of their collapsed images. A cofiltered diagram of nonempty subobjects of E with inclusion transitions cannot contain both A and B: a common refining index would be a nonempty subset of A∩B. Thus a pro-system of **nonempty subobjects over E** is not automatically an exact encoding of this particular formal-intersection expression. This is a typing check on a candidate encoding, not an arithmetic countermodel.

What (v) does not reconstruct for us is the class of all formal presentations, morphisms between them, and permitted identifications of different presentations. The raw star record suffices to retain the expression; it does not by itself specify those comparisons.

## B. Hull-approximants in (vi), p.130

For a direct-product region P, put S=φ(P) in its ambient packet. The source identifies P and its hull-approximants through this collapse. Its explicit sets, from (iii), p.128, are

`Φ(P)={H∈Hulls : H⊆φ(P), μlog(H)≥μlog(P)}`,

`Ξ(P)={H∈Hulls : H⊆φ(P), μlog(H)=μlog(P)}`.

For a bounded admissible family P_B, replace S by `H_B=φ(P_B)`, the intersection of hulls containing every member. Keep the upper bound H⊆H_B. In the local setting Ξ(P) is not asserted always nonempty; the source supplies particular sufficient cases and a global analogue in (iv), pp.128–129.

The sets Φ(P) and Ξ(P) are indices for **choices of hull-approximants**, not the over-region indices in C below. Their lower volume bound does not establish closure under common refinements. Exact attainment by an element of Ξ(P) is not imposed in this audit.

At a fixed presentation, a hull gives D_H=det^(⊗M)(H); actual module inclusions of hulls into H_B give the corresponding local linear determinant maps to D_B. Their postcomposition orbits are cQ3 data. This supplies an object-level connection and an inclusion-based local subcase. It does not turn an arbitrary set map A→B from (v) into a module map or determinant morphism. Evaluating a formal empty intersection first would also leave the finite-volume domain of the hull construction in (i), p.127.

## C. Enclosing-region systems in Remark 3.9.7(ii),(iii), pp.146–147

For a relatively compact E⊆K=I^Q((−)), the source gives the index set

`A_E={U∈M(K) : E⊆U}`.

At finite places M(K) consists of nonempty compact open subsets; at infinity it consists of compact closures of nonempty open subsets (Proposition 3.9(i), pp.115–116). A minimal precise inclusion encoding has one arrow U'→U when U'⊆U, and sends it to the actual inclusion of subsets of K. Equivalently order indices by reverse inclusion and use inverse-system transition maps. Identities and composition are forced by inclusion. Its scalar prescription is exactly

`μlog(E)=inf_(U∈A_E) μlog(U)`.

Every term has finite log-volume; the infimum may be −∞. The source also allows the subclass of direct-product regions when E is a direct-product pre-region. This records an approximation and requires neither an attained minimum nor an object realizing a categorical limit.

For a collection (E_vQ), indices are collections (U_vQ) of the kind in Remark 3.9.7(i), pp.145–146: they contain E_vQ componentwise and have only finitely many nonzero local log-volumes. Transitions in the minimal encoding are componentwise inclusions. The global value is the infimum of the already defined global log-volumes of those indices. Existence of at least one such enclosing collection is an explicit hypothesis in (iii). Do not exchange this infimum with an unrestricted infinite sum.

**Cofilteredness is not automatic.** For the unrestricted archimedean M(C), let E={0}, U={z:|z−1|≤1}, V={z:|z+1|≤1}. These are compact closures of nonempty open sets, contain E, and satisfy U∩V={0}. No member of M(C) is contained in their intersection. Thus the full inclusion category A_E in this example is not cofiltered. This does not address the more restricted direct-product-region version or the actual IPL family. It prevents an unjustified general replacement by Pro(C_B). Restricting to compact neighborhoods would change the indices and needs a separate comparison argument; none is silently supplied here.

## D. What survives cQ3, and where Section 5 stops

The records above retain regions, inclusions or other specified set maps, and formal expressions. cQ3 retains local Frobenioid objects, orbits of linear maps into fixed determinant objects, a global realified object, and localization isomorphisms. Its genuine functor and exact composition equations are proved in [CQ3_FUNCTOR_OR_PAIR.md](CQ3_FUNCTOR_OR_PAIR.md).

For any already specified J-diagram in C_B, its image under U_B is a J-diagram in C_q. There is **no obstruction to this generic pointwise extension**. The unresolved issue is identifying the actual source class and its arrows so that this lemma applies. Neither arbitrary set maps in A nor arbitrary over-regions in C already have the type of cQ3 morphisms.

The first missing datum is an **arrow-level presentation rule for the actual output**: for the formal presentations actually used by IPL/Theorem 3.11 and Ob4–9, specify their index objects and transition arrows, assign to each term a cQ3 tuple, and assign to each permitted transition a tuple satisfying equations (1),(2) in the companion file. The rule must say which comparisons of different root/log/formal-intersection presentations are retained, and how forgetting acts on them. At a fixed presentation its ordinary-diagram part would have type `D_B:J→C_B`, with image `U_B∘D_B:J→C_q`; across presentations it must state the source-permitted comparison type rather than assume isomorphisms or a group action.

This requires neither a unique universal category nor a topology nor effective descent. Even one adequate source-derived diagram presentation with its allowed comparisons would suffice for the next typing step. The point of failure is that such a presentation has not been extracted, not that no canonical completion was named.

Candidate clauses checked: (v),(vi); Ob4–9, especially Ob9-1, pp.133–139; cQ3/cQ4 and the rest of (ix), pp.141–144; Remark 3.9.7, pp.145–147; IPL, pp.151–152; Theorem 3.11(i),(ii), pp.153–156. Ob9-1 asserts that the formal indeterminacies preserve comparability and impose compatibility conditions on coarse invariants; it does not give us the above index/arrow rule. Theorem 3.11's functoriality for isomorphisms of processions is not, without another construction, functoriality for arbitrary region refinements. cQ4 retains the stated Galois/unit comparisons under log iteration; it does not in this reconstruction specify a functor on every upper-category object.

Consequently `FormalSys_B`, `FormalSys_q`, and `U_B^sys` remain **source-type unresolved**. The subsequent deliverables record this stop; they do not choose a constant q-system, a pro-category, or a substitute W* to bypass it.
