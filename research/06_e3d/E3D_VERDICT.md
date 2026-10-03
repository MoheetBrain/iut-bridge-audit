# E3d verdict

**FIRST_WITNESS_NOT_SUPPLIED**

This means not supplied by the present reconstruction of the pinned source/dependency slice. It does not mean that no such witness can exist in IUT. The remaining problem is specifically the native-marking rule in the formal output presentation, not another unspecified list of dependencies.

## First-failure record

**LAST SUCCESSFULLY CONSTRUCTED DATUM:** the span `C_B → C_q ← {q_M}`, with the cQ3 structure-map orbits, local pullback actions, global/localization data, and the stipulated cQ4 log-Kummer comparison family. Here q_M is formed from the original native q-pilot using the same positive power bookkeeping as D_B. A native-q tensor comparison is also constructed, but changes D_B to D_B⊗L_q^M.

**NEXT REQUIRED WITNESS:** W*, the native-marked restriction of the **actual IPL pilot comparison** to the cQ3/cQ4 formal output presentation.

**EXACT TYPE / FIRST TYPE DEPENDENCY:** the exact-representative candidate is the comma category `Fib_q(U_B)={(X,η): X∈C_B, η:U_B(X)≅q_M}`, with the explicit localization equations in [E3D_TYPED_DIAGRAM.md](E3D_TYPED_DIAGRAM.md). It is not imposed as the necessary witness. The required weaker datum is a family/diagrammatic relation carrying the returned pilot marking to the original splitting and localization marking, using the source's permitted formal operations. Its marked-image rule, and consequently its precise index/arrow data, have **not** been reconstructed from the category-pair description. Merely saying “formal image” does not define them. Thus this verdict is a **reconstruction/typing limitation**, not a fully typed minimal source requirement with a proved missing theorem.

**WHY REQUIRED:** U_B retains ambient objects and their structures, but does not say which native marking is the return of the IPL pilot. An arbitrary ambient comparison, or compatibility of group actions, cannot supply that identification. The closed-loop conclusion of III Remark 3.9.5(ix) explicitly concerns the simultaneous marked realization.

**CANDIDATE SOURCE CLAUSES CHECKED:** III Remark 3.9.5 cQ3/cQ4, Ob7–9 and (ix); Remark 3.10.2; Theorem 3.11(i)–(iii); Remark 3.11.1(ii)–(v); Remark 3.12.2(ii). Definitions, coricity, pullbacks, tensor powers and local/global constructions used from I/II, III Propositions 3.5/3.7/3.10, and FrI/FrII are recorded at their applications in [E3D_PROOF.md](E3D_PROOF.md).

**WHAT THEY PROVE HERE:** the strip path, the output representation subject to its indeterminacies, the bounded-domain hull/determinant presentation, and local/global and log-Kummer comparisons.

**WHAT THEY DO NOT YET PROVE HERE:** the native-marked formal restriction W*. The closed-loop, SHE and final special-case assertions have been read as arguments to reconstruct; their concluding claims have not been used as replacement hypotheses.

**POSSIBLE OVER-STRENGTH:** a single exact lift, canonical representative, global section, strict equality of regions, universal quotient, or fixed exact S is not required. The exact comma-type test is set aside for this reason. This prevents concluding a flaw from its failure. It also prevents declaring `OUR_REQUIREMENT_WAS_TOO_STRONG` for the entire E3d task: removing that excess has not constructed the weaker native-marked relation.

## Answers

- **Q:** the marked native vertical column `(Hq,•,0,ι:P≅Ffull(Hq,0))`, restricted to the splitting/unit realization in its local rings, Π_v↠G_v rigidifications, native global realified Frobenioid, localization maps and q-pilot. Its bad-place splitting sends `r` to `[q̲_v^r]`, with `q̲_v=qTate,v^(1/(2ℓ))` modulo the prescribed torsion. It is not just P or a scalar.
- **IPL:** preserves the complete abstract strip tuple and pilot through the stated isomorphism family. The original native realization remains a marked endpoint; transport of its marking through the subsequent formal output has not been obtained.
- **cQ3:** adds D_B, linear structure-morphism orbits, their local/global upper category and U_B; retains the source's pullback Galois/unit structures and localization. These are actual data, not just a common strip name.
- **cQ4:** compares Galois/étale-unit data and Frobenius-like unit presentations modulo allowed log iteration; finite inclusions and archimedean surjections retain their directions and domains. Native q is not varied under Ind1–3.
- **W / theorem constructing W:** no completed W. The accepted inputs construct the intermediate data, not an independently reconstructed native-marked formal restriction.
- **Does E3d close?** No derivation of closure in this attempt; no disproof of closure.
- **Scalar step:** no E3d-based application made. Separate native/output log-volumes and local log-volume compatibility do not manufacture W. No optional scalar-check file is created.
- **Attack status:** **UNDECIDED**. Neither a collapse of this attack nor a source-faithful obstruction/countermodel has been established.

## Quality control

The ten requested adversarial checks were applied: P and Q remain distinguished; no ring identification follows from IPL; q stays fixed; poly-isomorphisms retain their representatives; inclusion/surjection directions are preserved; no section is demanded; labels and power twists are tracked; xi-f and target-equivalent claims are not inputs; scalar equality is not used to reconstruct structure; and the unconstructed marking rule is exposed rather than hidden in a new compatibility assumption.

Validation run on 2026-10-03:

- `python3 scripts/verify_sources.py`: PASS, 18 source pins/metadata records and 202 archived LANA files.
- `python3 scripts/validate_ledgers.py`: PASS, existing schemas, references, dependency DAG and generated views.
- `python3 scripts/render_closed_loop.py --check`: PASS, 79 existing Stage 3.5 rows.
- `python3 scripts/render_membership.py --check`: PASS, 53 nodes, 76 edges, 83 lexical occurrences and 56 ordered pairs.
- `python3 -m unittest discover -s tests -v`: all 33 tests PASS.
- Read-only E3d check: exactly these four files; 10 unique CSV rows with the requested 11 fields and allowed statuses; cited source-page bounds; local Markdown links and fenced-block balance.
- Manual primary-source reading, including visual inspection of the pinned III p.152 diagram, checked arrow directions and the cited hypotheses. This is a bounded reconstruction, not independent verification of all accepted IUT inputs.
- All 498 pre-existing tracked paths matched their initial byte/missing-file snapshot. The pre-existing deletion of `recovery/2026-09-21/README.md` was preserved and excluded from this task's staging.

These checks concern source integrity and artifact consistency, not mathematical certification. Work is based on `6d94a31640ace4cf034fa3fb3f809a6a518a7cec`, in `codex/e3d-native-q-restriction`, with only this directory added.

## One next mathematical move

Specify the native-pilot restriction in cQ3's category pair using its permitted root, log and formal-intersection diagrams, then compute that restriction on the IPL splitting generator. **Not started.**
