# E3d.1 verdict

**FORMAL_SYSTEM_TYPE_UNRESOLVED**

**Attack status: UNDECIDED.** No source-faithful obstruction, countermodel, proof of failure, or closure of the attack has been established.

The task advanced from the E3d span to an explicit categorical construction: cQ3's object/morphism records give a genuine faithful U_B. At a fixed presentation its unrestricted upper category is exactly the category of elements of a presheaf T_B over the locally linear ambient arrows. Thus its fibers and the compatible-orbit criterion for lifting any specified diagram are known. Formal intersections and finite-volume enclosure systems have also been separated and typed as raw records. They cannot in general be declared cofiltered systems without a further argument.

## First unresolved datum

**Last constructed datum:** `C_B≅∫T_B→C_q^loc-lin↪C_q`, native q_M∈C_q, the stated cQ4 Galois/unit comparison family, and the separate formal region records. For every specified J the ordinary functor Fun(J,U_B) exists.

**Next exact datum:** the assignment of terms and transition arrows in the actual IPL formal output to cQ3 local/global tuples, including the source-permitted comparisons between root/log/formal-intersection presentations. Its fixed-presentation diagram part has type `D_B:J→C_B`; every transition must preserve the structure-map orbit and the localization square. The rule must also specify how forgetting acts on its allowed comparisons. This is the missing source-native presentation, not a demand for a universal pro-category or a single effective object.

**Why necessary:** region/set maps, determinant Frobenioid morphisms and cQ4 comparisons have different domains and preservation conditions. Knowing the constituent categories and object-level operations does not yet identify the actual output diagram or its native target. The generic extension theorem cannot determine its own source-specific input.

**Candidate clauses checked:** III Remark 3.9.5(v),(vi), Ob4–9, Ob9-1 and (ix), pp.129–144; Remark 3.9.7, pp.145–147; IPL in Remark 3.10.2, pp.151–152; the stated outputs of Theorem 3.11(i),(ii), pp.153–156; FrI Definitions 1.2 and 1.3, pp.21–25; FrII Example 5.6(iii),(iv), pp.63–65. Remark 3.12.2(ii), pp.187–189, was used only to identify the target conclusion.

**Strongest statement obtained:** explicit ordinary tuple categories, the faithful forgetful functor, the exact discrete-fibration description on its correct restricted base, and a necessary-and-sufficient compatible orbit-family criterion for a specified ordinary diagram lift. This is more than a category pair named as a quotient, but less than a typed source-native W*.

**Weaker source requirement:** formal expressions and enclosure approximations do allow weaker representations than an attained exact object. This audit permits them. Their actual marked comparison type has not been recovered, so removing the exact-object requirement does not finish the task or justify a different top-level verdict.

## Requested outputs at the stop

| Item | Result |
|---|---|
| FormalSys_B / FormalSys_q | Source-native category unresolved; raw records and the exact boundary are in [FORMAL_SYSTEM_TYPE.md](FORMAL_SYSTEM_TYPE.md). |
| U_B | Genuine functor, derived from cQ3's explicit pair. Proof and equations in [CQ3_FUNCTOR_OR_PAIR.md](CQ3_FUNCTOR_OR_PAIR.md). |
| Q_sys | Not yet typed. Native Q, its splitting, units, global pilot, root/torsion and localization data remain explicitly recorded in [Q_SYSTEM.md](Q_SYSTEM.md). |
| W* | Not yet typed or constructed; the two auxiliary tests in [WSTAR_TYPE.md](WSTAR_TYPE.md) are not substituted for it. |
| Effectivity test | Stops before a source-native effectivity statement; dependency and hypothesis check in [WSTAR_PROOF_ATTEMPT.md](WSTAR_PROOF_ATTEMPT.md). |
| Categorical analogue | Exact at the fixed cQ3/category-of-elements level; pro/stack/descent identifications are not imported. Full comparison in [CATEGORICAL_CROSSCHECK.md](CATEGORICAL_CROSSCHECK.md). |
| Generator | Not reached; no GENERATOR_CHECK.md created. |
| Scalar consequence | Not reached; no new use of xi-f or scalar applicability claim. |

## Provenance

Repository: MoheetBrain/iut-bridge-audit. Base: `codex/e3d-native-q-restriction` at `61c4163f3bf9ff66e3d6d6cebaf7dac5b97c079b`. Task branch: `codex/e3d-formal-system-lift`. Only the seven requested files in this directory are added. Prior audits and source pins are retained; the pre-existing deletion of `recovery/2026-09-21/README.md` remains outside this change.

The prescribed current/prior artifacts were read before the source check. Primary pages were read from pinned PDFs, with visual checks of the formal-intersection notation (III pp.129–130), Ob9-1 (pp.138–139), cQ3/cQ4 (pp.141–142), enclosing-region systems (p.146), IPL diagram (p.152), and FrII localization arrows (p.65). This is a bounded source reconstruction, not independent verification of all underlying IUT results. No later ELS material or paid compute was used.

Validation on 2026-10-03:

- `python3 scripts/verify_sources.py`: PASS; 18 source pins/metadata records and 202 LANA files.
- `python3 scripts/validate_ledgers.py`: PASS; schemas, locators, references, dependency DAG and generated views.
- `python3 scripts/render_closed_loop.py --check`: PASS; 79 Stage 3.5 rows.
- `python3 scripts/render_membership.py --check`: PASS; 53 nodes, 76 edges, 83 lexical occurrences, 56 ordered pairs.
- `python3 -m unittest discover -s tests -v`: all 33 tests PASS.
- Read-only artifact checks: exactly seven requested files, valid local Markdown links and balanced fences; all 502 pre-existing tracked paths match their initial byte/missing-file snapshot.

Passing these checks verifies provenance and artifact consistency only, not mathematics. No test suite is presented as a verification of the new categorical arguments or of IUT.

## Exactly one next mathematical move

Reconstruct the **arrow-level cQ3 presentation of the formal region system used by the actual IPL output**, including its permitted root/log comparisons, from Remark 3.9.5(v),(vi), Ob4–9 and cQ3/cQ4. **Not started beyond identifying and typing this obligation.**
