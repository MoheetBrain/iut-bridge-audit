# Stage 3.5 deliverables

**NO-GO for Stage 4.** [Gate](../../STAGE_3_5_GATE.md) · [Principal closed-loop statement](CLOSED_LOOP.md) · [Deep native-q trace](NATIVE_Q_CLOSED_LOOP_TRACE.md).

| Package | Analysis | Structured evidence |
|---|---|---|
| A | [U04 minimality](U04_MINIMALITY.md) | [Step-6 relations](STEP6_RELATIONS.csv) |
| B | [sQ3/cQ3](CQ3_COMPATIBILITY.md) | [Types](SQ3_TYPES.csv), [formal quotients](FORMAL_QUOTIENT_LEDGER.csv) |
| C | [sQ4/cQ4](CQ4_LOG_KUMMER_TRANSPORT.md) | [Types](SQ4_TYPES.csv), [vertical shifts](VERTICAL_SHIFT_LEDGER.csv) |
| D | [Closed loop](CLOSED_LOOP.md) | [Graph](CLOSED_LOOP_GRAPH.json), [edges](CLOSED_LOOP_LEDGER.csv) |
| E | [Native q rigidity](Q_PILOT_RIGIDITY.md) | [Transport](Q_PILOT_TRANSPORT.csv) |
| F | [sQ5 information loss](SQ5_FORGETFULNESS.md) | [Pre/post fields](PRE_POST_LOG_VOLUME.csv) |
| G | [LANA↔IUT crosswalk](ETA_CLOSED_LOOP_CROSSWALK.md) | [Directional statuses](CROSSWALK.csv) |
| H | [Common equality target](COMMON_TARGET.md) | [Line/normalization types](VOLUME_LINE_TYPES.csv) |
| I | [Native-q closed-loop trace](NATIVE_Q_CLOSED_LOOP_TRACE.md) | Uses packages B–H; source claim kept distinct from verification |

The 79 ledger rows are authored in [STAGE35_DATABASE.json](STAGE35_DATABASE.json). `scripts/render_closed_loop.py` generates the CSVs and graph and validates references/statuses. [READING_LOG.md](READING_LOG.md) records full Remark 3.9.5 coverage and the exact inspection limits. [LEAN_REPLAY.md](LEAN_REPLAY.md) reports the secondary exact-toolchain attempt. [VALIDATION_RESULTS.json](VALIDATION_RESULTS.json) records executed checks.

[U04_SUPERSEDED_RECORDS.json](U04_SUPERSEDED_RECORDS.json) preserves the old over-strong requirement from the base commit. Current M09, CH07, U04, U06/U07/U09/U10 and indeterminacy records are updated in the original database. The earlier gate remains historical with an explicit correction notice. Recovered research and pinned sources are preserved.

No mathematical claim is certified by CSV validation. `SOURCE CLAIM` means that the cited source asserts the construction; it is not promoted to an independently verified theorem. The run stops at the Stage 3.5 gate.
