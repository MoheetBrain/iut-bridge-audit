# Categorical cross-check

Standard names below are applied only after the source records are written down. The comparisons do not endow IUT's formal quotient with extra universal properties. Primary category-theory references were checked on 2026-10-03.

## Definitions used to check the names

An inverse system over a preorder specifies objects and transition maps with identity/composition laws; directedness is an additional condition. See [Stacks, Definition 4.21.2](https://stacks.math.columbia.edu/tag/0030). Cofilteredness requires a nonempty category, cones under pairs of objects, and equalizers of parallel arrows in the indexing sense. See [Stacks, Definition 4.20.1](https://stacks.math.columbia.edu/tag/04AY).

A pro-object uses a cofiltered diagram, and its morphisms use a limit/colimit construction, not just arbitrary maps of underlying sets. See [Stacks, Remark 4.22.5](https://stacks.math.columbia.edu/tag/05PT). These requirements must be checked before using that name.

For a presheaf T:C^op→Sets, the category with objects (Y,a∈T(Y)) and arrows f satisfying T(f)b=a is fibred in sets over C. See [Stacks, Example 4.38.5 and Lemma 4.38.6](https://stacks.math.columbia.edu/tag/0042). The cQ3 instance is proved directly in [CQ3_FUNCTOR_OR_PAIR.md](CQ3_FUNCTOR_OR_PAIR.md).

Technical descent data require a fibred category, a family of arrows to one base object, suitable fiber products and cocycle isomorphisms. Effectivity means that this datum is isomorphic to the pullbacks of an object over that base. A topology is not required merely to define one descent datum; calling something a stack requires further structure and conditions. See [Stacks, Definitions 8.3.1 and 8.3.5](https://stacks.math.columbia.edu/tag/02ZC).

## Source-to-analogue comparison

| SOURCE STRUCTURE | STANDARD CATEGORICAL ANALOGUE | MATCH STATUS | Exact scope or missing hypothesis |
|---|---|---|---|
| cQ3's fixed-presentation C_B, C_q and deletion of structure-map orbits (III pp.141–142) | Forgetful functor | EXACT | Identity/composition and localization equations are verified. The source calls the pair a formal quotient; that phrase supplies no universal quotient property. |
| Same unrestricted C_B over C_q^loc-lin | Category of elements; discrete Grothendieck fibration | EXACT | C_B≅∫T_B and the unique lift is precomposition of linear-map orbits. This is a consequence of the records, not an assertion that the printed text uses this terminology. |
| Same U_B over all C_q arrows | Grothendieck fibration inferred by the preceding argument | NOT_APPLICABLE | A higher-degree local arrow cannot satisfy the orbit compatibility equation. The proved fibration has the locally linear base. |
| Given Y∈C_q and orbits T_B(Y) | Strict fiber; ordinary essential-image criterion | EXACT | Y has a lift precisely when T_B(Y) is nonempty; isomorphic images transfer along the isomorphism. No claim of nonemptiness for every Y. |
| E3d's optional test `(X,η:U_B(X)≅q_M)` | Iso-comma / 2-fiber product with the category selecting q_M | EXACT | Exact as an auxiliary test; not established as the necessary source W*. Morphisms satisfy η' U_B(h)=η. For the standard construction see [Stacks, Example 4.31.3](https://stacks.math.columbia.edu/tag/003O). |
| An already specified J-diagram of cQ3 tuples | Diagram category and postcomposition Fun(J,U_B) | EXACT | Explicitly conditional on J and the actual arrows being supplied. No cofilteredness or effective realization of a limit is needed. |
| Remark 3.9.5(v)'s specified family of nonempty subsets over E | Unevaluated star/cospan diagram recording a formal intersection | EXACT | Exact encoding of that raw expression, including an empty evaluated intersection; not a definition of all source-permitted morphisms between formal expressions. |
| The same formal-empty expression encoded by nonempty subobjects of E with inclusion refinements | A cofiltered pro-presentation containing all original leaves | NOT_APPLICABLE | The disjoint-singletons example in FORMAL_SYSTEM_TYPE proves this particular encoding fails. Other formal completions are not excluded. |
| Remark 3.9.7's enclosing regions with their actual inclusions | Inverse diagram over the reverse-inclusion preorder | EXACT | Minimal inclusion encoding of the given indices; no assertion that the source specifies a full category of comparisons between different such systems. |
| The unrestricted enclosing-region indices of Remark 3.9.7(ii) | Pro-object using all those indices and inclusions | NOT_APPLICABLE | The tangent-disks example shows the general index category need not be cofiltered. No claim against the restricted direct-product version or a separately proved equivalent presentation. |
| cQ3 localization tuples plus cQ4 Galois/unit comparisons | Descent datum with effective global marked descent | HEURISTIC_ONLY | No source-derived base family, overlap cocycle and descent functor for this native-marked problem have been identified. Having a global object as a tuple field is different from constructing it by effective descent. |
| FrI Definition 1.3(i)(c)'s base pullbacks used by cQ3 | Cartesian lifting over the Frobenioid base | EXACT | The given pullback universal property and slice equivalence supply this operation. They do not identify that base with a site of native-q formal output presentations. |
| cQ3's word “stack-theoretic” for its formal category pair | A stack on a Grothendieck site | HEURISTIC_ONLY | The checked record supplies neither a chosen topology nor a stack/descent verification for the present system. |

All IUT matches refer to the pinned [III](../../sources/primary/IUT_III.pdf), Remark 3.9.5(v),(vi),(ix), pp.129–130, 141–144, and Remark 3.9.7, pp.145–147. The Frobenioid pullback record is in [FrI](../../sources/primary/Frobenioids_I.pdf), Definitions 1.2(ii), 1.3(i)(c), pp.21,24.

No row is marked EQUIVALENT_AFTER_PROOF on the basis of an unperformed proof. In particular, the equality of an infimum with a value obtained from a different cofiltered approximation would need a comparison proof before being used. These checks distinguish unavailable analogies from failures of IUT itself.
