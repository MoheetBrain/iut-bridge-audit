# iut-bridge-audit
A focused, reproducible audit of the IUT III Theorem 3.11 → Corollary 3.12 bridge, testing whether the xi-e machinery genuinely implies xi-f’s q-pilot log-volume membership claim via formal dependency analysis and countermodel search.

## Recovered audit — 21 September 2026

The existing IUT work from the `P= NP` task has been recovered here. It was originally saved in the separate `IUT_CHALLENGER` directory, outside Superlinear. This recovery copies the reports and their supporting evidence; it does not advance or independently validate their mathematical conclusions.

| Deliverable | Contents |
|---|---|
| [Critical bridge report](IUT_STAGE1_CRITICAL_BRIDGE.md) | Target, source-reading boundary, attempted reconstruction, and stopping point |
| [Source ledger](IUT_STAGE1_SOURCE_MAP.csv) | Source locations, interpretations, dependencies, and evidence status |
| [Dependency graph](IUT_STAGE1_DEPENDENCY_GRAPH.json) | Typed registry and unresolved proof obligations |
| [Candidate missing-premise analysis](IUT_STAGE1_MISSING_PREMISE.md) | Conditional sufficient criterion and source-faithfulness limitations |
| [Recovered final status](recovery/2026-09-21/IUT_STAGE1_STATUS.txt) | Exact status block from the earlier response |
| [Recovery record](recovery/2026-09-21/README.md) | Original response, provenance, checksums, and scope |

The recovered result is **TARGET_NOT_YET_FORMALIZABLE_WITHOUT_LARGER_IUT_DEPENDENCY**. The critical implication was neither proved nor refuted. No faithful countermodel or prize-relevant flaw was established, and the audit created no Lean formalization of the bridge. The copied third-party source snapshots do contain their existing Lean files.

The recorded next action is to specify and check IUT III Remark 3.9.5(ix), especially cQ3/cQ4, including preservation of the native q constraint through the output construction and normalized volume comparison. That action remains unstarted by this recovery.

## Supporting material

- [`sources/`](sources/) contains the retrieved PDFs, LANA report source, original retrieval metadata, and two pinned repository snapshots. Their revision identities are recorded in [PROVENANCE.json](recovery/2026-09-21/PROVENANCE.json).
- [`tmp/`](tmp/) retains the earlier extracted texts, page data, rendered pages, and ledger-building helper. These are recovered working materials, not disposable omissions from the evidence package.
- The report's companion links now resolve within this repository. The copied helper resolves its root from its own location. Exact originals of both edited files are retained in [`recovery/2026-09-21/originals/`](recovery/2026-09-21/originals/).

The [attached stages 1–3 prompt](recovery/2026-09-21/STAGES_1_3_REQUEST_REFERENCE.txt) is retained as reference context. Its instructions were not executed during recovery. The earlier label “Stage 1” does not certify completion of the source-lock, η-reconstruction, or admissibility deliverables requested by that later prompt.
