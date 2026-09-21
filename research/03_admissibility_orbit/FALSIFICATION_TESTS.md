# Tests for the faithfulness of this reconstruction

These are **RECONSTRUCTION / OPEN QUESTION** checks of the specification, not attempted falsifications of IUT. The automated tests check data integrity only.

| Check | Evidence and acceptance rule | Current result |
|---|---|---|
| Noncanonicity | An existential target can hold with many choices; variation alone cannot refute it [C020, LANA (9-1)] | Negative control enforced |
| Rescaling license | Any proposed rescaling must lift to the full source data, preserve the appropriate pilots/weights and satisfy all coupling conditions [R_CH01–R_CH12] | No arbitrary rescaling admitted |
| Diagram semantics | Replace strict commutativity by upper semi-compatibility exactly where the source does [C013, IUT3 Theorem 3.11(ii)] | Inclusions/surjections retained; complete η action UNKNOWN |
| Pointing tautology | Target pilot [1·S] must not be identified with the native q pilot in the definition of admissibility [C012, C023] | Separate pilots retained |
| Kummer lift | Image containment cannot alone certify a source-structured coherent inverse/factorization [C024] | U04 open |
| Measure class | General measurable regions must not silently inherit the source packet-weighted formulas [C016, R_U06] | U06 open |
| Source retention | Native unit/Galois/localization and determinant data must survive until the source says they are forgotten [C014] | U09 open |
| Same equality type | All compositions must use specified source transports rather than arbitrary line isomorphisms [R_U07] | U07 open |
| Independent choices | Independence only where the exact source asserts it [R_CH03, R_U08] | Complete coupling unresolved |
| Lean abstraction | A theorem with h312 is conditional; RHS region is an input; an abstract interface is not its IUT realization [C007–C008, C021] | Boundaries explicitly retained |
| Toy universe | No invented InputType/OutputType/ThetaLink model is treated as faithful IUT evidence | No such model created |
| Criticism/response | Include both the criticized comparison and the additional structure invoked in reply | Neither treated as a verdict |

## Executable integrity checks

`python3 scripts/verify_sources.py` checks every corpus hash and metadata record plus all 202 code-snapshot files against the pinned archive. `python3 scripts/validate_ledgers.py` checks schemas, source locators, foreign keys, statuses, graph acyclicity and generated-view freshness. `python3 -m unittest discover -s tests -v` includes deliberate corruptions for missing/unknown source IDs, unknown objects, dangling endpoints, nonexistent steps, missing invariant/claim status, invalid evidence labels, duplicate IDs, graph errors, byte tampering and code-comment masking.

A passing test cannot certify full admissibility, equivalence to IUT, TARGET ★, or the mathematical validity of a cited theorem. No abc computations or Stage-4 tests were performed.
