# Dependency check: the formal-system typing boundary

**Result: FORMAL_SYSTEM_TYPE_UNRESOLVED.** The attempt stops at row 7 below. Later native transport and scalar steps were not attempted. “Unresolved” means not reconstructed from the checked slice, not disproved.

Use the pinned [III](../../sources/primary/IUT_III.pdf), [FrI](../../sources/primary/Frobenioids_I.pdf), and [FrII](../../sources/primary/Frobenioids_II.pdf). The detailed E3d initial input and strip path are preserved in [E3D_PROOF.md](../06_e3d/E3D_PROOF.md).

| Step / required component | Construction and exact hypothesis matching | Resulting component | Status |
|---|---|---|---|
| 1. Native input Q | E3d's actual codomain column of the fixed initial Θ-data and LGP-Gaussian lattice; no inverse reconstruction from abstract P. | Native splitting, units, pilot, realification and localization, recorded in Q_SYSTEM. | RETAINED INPUT |
| 2. IPL on full strips | III Remark 3.10.2, pp.151–152, uses the env/gau/LGP/lgp strips of that same theater and its coric column. The displayed horizontal and vertical arrows are the cited strip isomorphisms. | The commutative strip diagram; the IPL path uses inverses of genuine strip isomorphisms. | CONSTRUCTED IN E3d; DIAGRAM RECHECKED |
| 3. Stated multiradial output | III Theorem 3.11(i),(ii), pp.153–156, applies to the given lattice/procession. Part (i) supplies modules, splitting-monoid actions and global field/Frobenioid data modulo Ind1/2; its functoriality is with respect to procession isomorphisms. Part (ii) gives the specified log-Kummer comparisons and Ind3. | The stated collection of output data and comparison families. This is not yet a functor from a category of formal region presentations. | RETAINED AT ITS STATED TYPE |
| 4. Hull/determinant and cQ3 | III Remark 3.9.5(i)–(vi), Ob4–7, cQ3. Require admissible bounded regions, the corrected positive tensor power, and the given local/global Frobenioids and localization. The formal global envelope version retains the hypothesis of Remark 3.9.7(iii). | D_B; C_B,C_q with explicit objects/arrows; genuine U_B. No unconditional boundedness of all outputs is inferred. | FIXED-PRESENTATION CONSTRUCTION |
| 5. Local pullback and localization | FrI Definition 1.3(i)(c), p.24, gives pullbacks over the Frobenioid's base for an already given object. Pullbacks are linear by 1.3(iv)(b), p.25. FrII Example 5.6(iii),(iv), pp.63–65, uses the specified tempered-group diagram, divisor support/saturation and coefficient choices to construct localization functors. | The cQ3 actions and localization framework. For the abstract tuple category, the category-of-elements proof explicitly constructs lifts over locally linear arrows. | CONSTRUCTED; NO NEW GLOBAL GLUING CLAIM |
| 6. Formal region records | III Remark 3.9.5(v),(vi), pp.129–130, supplies formal intersection/collapse and hull-approximant data. Remark 3.9.7(ii),(iii), pp.146–147, supplies finite-volume enclosing-region indices. | Unevaluated intersection records and inclusion diagrams; no universal cofilteredness or exact attainment. | RECONSTRUCTED AT SET/REGION LEVEL |
| 7. Assignment of actual formal output arrows to cQ3 arrows, with allowed presentation comparisons | Must connect the preceding records to the actual IPL output. Need its index/transition data and the structure-orbit/localization equations; varying root/log presentations need their source-permitted comparison rules. cQ3 gives the fixed categories; cQ4 and Ob9-1 state compatibility but have not supplied this whole rule in the reconstruction. | FormalSys_B, FormalSys_q and their source-specific forgetful operation cannot yet be instantiated. | FIRST UNRESOLVED TYPE |

## What the source compatibility statements contribute

cQ4, III p.142, compares local Galois and étale-like unit data through the log-Kummer correspondence; the Frobenius-like unit version retains indeterminacy under arbitrary log iterates. Theorem 3.11(ii), pp.155–156, carefully distinguishes its compatible splitting/global data from the module comparisons subject to Ind3, and distinguishes MOD from mod compatibility. These are substantial specified comparisons. They are not recast here as an equivalence on all of C_B.

Ob9-1, pp.138–139, explicitly says the three formal indeterminacies do not change comparability and function as compatibility conditions for passage to coarse invariants. This rules out treating comparability as destroyed merely by keeping formal systems. It does not, in this attempt, provide the transition assignments needed at row 7. The later discussion of (ix), pp.142–144, is checked as the claimed simultaneous compatibility to reconstruct, not substituted for that assignment.

Remark 3.12.2(ii), pp.187–189, was read only as the target description: fix native q-intertwining and retain it simultaneously with the represented Θ data. The stated logical conjunction and specialization are not proof inputs. Equal underlying strips alone do not establish equal marked intertwining.

## Does this require an effectivity theorem?

For **(a), built into the object definition**, a cQ3 local/global object already includes a global object and localization isomorphisms. Once such a tuple is supplied its compatibility is data, not a separate existence theorem. This definition does not assert that every family of local objects extends to a global one.

For **(b), cited Frobenioid results**, FrI supplies base pullbacks, and FrII supplies localization-by-restriction functors under its hypotheses. Neither statement, as used here, constructs a native-marked IPL formal system. The explicit discrete-fibration proof supplies a fixed-category lifting operation over locally linear arrows; it presupposes the target upper object and is not essential surjectivity.

For **(c), an additional proof**, it is premature to demand a general descent-effectivity theorem. At the present stop no source-native descent datum, comparison category or W* has been fully specified. A raw diagram needs no effective realization as a single object. If a specified diagram Y were recovered, its ordinary strict-lift problem would be exactly the compatible orbit-family criterion already proved in CQ3_FUNCTOR_OR_PAIR.

For **(d), an over-strong formulation**, replacing formal approximation by an exact representative or demanding a technical stack would add requirements. Neither is imposed. No finding that a weaker source-native W* actually suffices and is constructed has been obtained either.

## Exact stopping record

Last constructed data: fixed-presentation `C_B≅∫T_B→C_q^loc-lin↪C_q`, the native q_M beside it, the given cQ4 comparison family, and separate raw formal-region records. The generic diagram extension is proved.

Next datum: the source-derived assignment of actual formal output terms **and arrows** to these tuple categories, together with the allowed root/log/refinement comparisons. Its fixed-presentation part would be an explicitly specified diagram `D_B:J→C_B`, with the two displayed compatibility equations holding on every arrow. This is needed before selecting a Q_sys or a relation to it. A smaller sufficient presentation is allowed; no universal completion is demanded.

No generator was transported, no scalar applicability claim was made, and no countermodel was launched. The first obstruction is to the audit's typing, not an established obstruction to an IUT construction.
