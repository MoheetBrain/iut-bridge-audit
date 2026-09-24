# IUT bridge audit

Is the native q comparison map in the family of admissible anabelian reconstructions?

\[
\exists\ S\ \text{suitable},\qquad\eta^q=\eta^{\mathrm{anab}}_S.
\]

This is LANA's equation (9-1), §9.2, p.46 [C003]. Its exact source-faithful admissibility predicate and common equality type remain only partly reconstructed. The term “orbit” names the intended image family; no full group action is assumed.

The question concerns the Theorem 3.11 → Corollary 3.12 bridge. LANA relates its compatibility goal to that bridge, while Mochizuki's sources retain local/global, unit/Galois, tensor and normalization structure that must also enter a faithful comparison [C004, C009, C014–C016]. Their full equivalence is not established by this audit.

## What is known

The pinned LANA report explicitly describes nine η steps and does not claim to prove or disprove its final compatibility [C001–C006, C022]. Its Lean repository defines `Corollary312Variant` and supplies conditional downstream implications requiring that variant as a hypothesis [C007–C008, C027]. The original IUT corpus asserts additional compatibilities, including cQ3/cQ4; those assertions are preserved and traced.

## What is not known here

A complete Adm(D), the induced effect of every choice, the common normalized equality type, and native-q preservation through the formal quotient have not been certified. No flaw, countermodel, independence result or unconditional bridge proof is claimed. Scoped normalization laws are recorded without presenting them as invariants of the entire η family.

## Current deliverables

**Stage 3.5 delivered. Stage 4: NO-GO.** Start with [STATUS.md](STATUS.md), the twelve-question [current gate](STAGE_3_5_GATE.md), and the [closed-loop audit index](research/04_closed_loop/README.md). The [Stages 1–3 gate](STAGE_1_3_GATE.md) is historical; its global-lift requirement has been corrected.

The mandatory U04 audit finds **GLOBAL LIFT NOT REQUIRED** by the detailed printed route. The source asserts a closed loop preserving q-intertwining while constructing Θ-intertwining up to indeterminacies on one fixed abstract full prime-strip. Its independent verification and both directions of the LANA exact-S crosswalk remain incomplete. Native q log-volume is explicitly excluded from Ind1/2/3; it is not placed in the Θ-output orbit.

- [Source manifest](research/01_source_lock/SOURCE_MANIFEST.csv), [claim registry](research/01_source_lock/CLAIM_REGISTRY.csv), [priority](research/01_source_lock/SOURCE_PRIORITY.md) and [gaps](research/01_source_lock/SOURCE_GAPS.md).
- [Exact target](research/02_eta_reconstruction/ETA_TARGET.md), [nine-step algorithm](research/02_eta_reconstruction/ETA_ALGORITHM.md), object/map dictionaries, [dependency DAG](research/02_eta_reconstruction/DEPENDENCY_DAG.md) and [code audit](research/02_eta_reconstruction/LANA_CODE_AUDIT.md).
- [Partial admissibility](research/03_admissibility_orbit/ADM_DEFINITION.md), choice/indeterminacy/orbit ledgers, [candidate invariants](research/03_admissibility_orbit/INVARIANT_CANDIDATES.md), [orbit specification](research/03_admissibility_orbit/ORBIT_SPEC.md) and [faithfulness checks](research/03_admissibility_orbit/FALSIFICATION_TESTS.md).

`research/RESEARCH_DATABASE.json` is the canonical Stages 1–3 record, updated with the Stage 3.5 corrections. `research/04_closed_loop/STAGE35_DATABASE.json` contains the new 79-row source reconstruction. Scripts generate CSV/Markdown views and schemas. Every substantive ledger row has source provenance and an epistemic label. The older audit recovered from the misplaced task remains in the repository as historical material; it is not a substitute for the current source checks. The other project was not edited.

## Scientific rules

Keep SOURCE FACT, SOURCE CLAIM, RECONSTRUCTION, INFERENCE and OPEN QUESTION distinct. Cite pinned primary passages for source mathematics. Noncanonicity does not refute existence. Arbitrary rescaling is not assumed admissible. Ind3 upper semi-compatibility is not replaced by strict commutativity. A toy abstraction is not a faithful IUT countermodel. UNKNOWN is an acceptable result.

## Reproducibility

Python 3.9+ standard library suffices for the offline checks:

```sh
python3 scripts/verify_sources.py
python3 scripts/validate_ledgers.py
python3 scripts/render_closed_loop.py --check
python3 -m unittest discover -s tests -v
```

To regenerate the derived audit views:

```sh
python3 scripts/audit_lana.py
python3 scripts/render_ledgers.py
python3 scripts/build_dependency_graph.py
python3 scripts/validate_ledgers.py
```

See [COMMANDS.md](COMMANDS.md) for acquisition, source-rendering and verification commands. Source downloads are separate from offline verification. Current author URLs may change; saved hashes and immutable code/report commits define this audit snapshot. The exact Lean 4.32.0 build was attempted in an isolated copy with all 12 dependency revisions verified; it timed out before completion or `#print axioms`. See the [replay record](research/04_closed_loop/LEAN_REPLAY.md). Passing data-integrity tests does not certify the mathematics.
