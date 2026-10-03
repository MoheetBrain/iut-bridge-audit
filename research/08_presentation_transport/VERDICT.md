# E3d.2 verdict

**FIRST_PRESENTATION_TRANSPORT_UNSUPPLIED**

**Attack status: UNDECIDED.** No flaw, source-faithful countermodel, impossibility of transport, or collapse of the attack is established.

At a fixed presentation the E3d.1 result is unchanged. New progress consists of explicit transport formulas and proofs: a functor plus an equivariant linear determinant comparison gives an orbit map; an actual linear comparison without that equivariance gives a representative-independent orbit relation with a weaker composition law. Positive naive Frobenius powers give forward orbit maps. Supplied rooted presentations can be compared by equality of their images in a common powered presentation, without inverting the power functor.

The first required unsupplied operation is **γ_log^det**, the cQ4 log-Kummer adjustment acting on the local cQ3 structure-morphism orbits. The source's unit/module correspondences and its genuine global MOD comparisons have been retained. No map or sufficiently specified relation on the actual T_B fibers has been derived from them in this bounded reconstruction.

## Minimal route and transition status

| ID | Role | Transport result |
|---|---|---|
| S0 | IPL full-strip path | Actual strip isomorphisms retained. They transport the abstract strip data; no commutation of determinants with a non-ring Θ-link is assumed. |
| S1 | Collect possibilities, including Ind1/2, inside the common admissible bounded family | Uses Ob5's common H_B; no separate action of arbitrary mono-analytic changes on T_B is needed or asserted. |
| S2 | Corrected determinant at a chosen M | Introduces D_B and the fixed T_B. It is not a transport from a presheaf on arbitrary regions. |
| S3 | cQ3 formal-collapse presentation | Genuine forgetful U_B and its given category pair; no inverse or arbitrary fiber action inferred. Formal-empty expressions remain unevaluated. |
| S4 | cQ4 vertical log-Kummer adjustment | Unit/module, splitting and global MOD comparisons supplied at their stated types; **orbit-level transport first unsupplied**. |
| A1 | Optional further positive power M→dM | Forward function `[a]↦[Ψ_d(a)]` proved; compatible with localization and composition up to the source natural isomorphisms. |
| A2 | Optional root/twist comparison | Relation over a common powered image, conditional on supplied rooted objects and markings. No universal root existence or inverse function claimed. |
| A3 | Conditional hull/enclosing-region inclusion | Actual linear determinant inclusion gives the orbit relation (R); its weaker composition law (C) is explicit. Not a theorem for arbitrary set maps or a cofiltered family. |

This is a dependency-ordered core S0→S1→S2→S3→S4, with the conditional A branches attached after S2. It does not require all seven candidate classes as independent changes. Staying at a fixed permitted M avoids compulsory root extraction; the common family avoids unnecessary changes between individual hull-approximants.

## Exact first-failure record

**Transition:** the adjustment of adjacent output realizations in the native vertical column by the log-Kummer correspondence of III Ob8/cQ4. A one-edge test already remains unresolved; no reduction of all allowed iterates to one edge is claimed.

**Endpoint types:** for specified endpoint collections Y_± and determinant presentations B_±, the sets are `S_±=∏_v Aut(D_±,v)\Hom_lin(Y_±,v,D_±,v)`. The native endpoint retains the original Q and q_M. The permitted pairing/provenance of the actual IPL endpoint data must itself be retained.

**Transport needed:** at least a source-derived relation `R_log⊆S_-×S_+`, independent of orbit representatives and compatible with the source's local/global structure and consecutive changes. A total functor on every C_q object is a sufficient approach, not a necessary demand.

**Source clauses checked:** III Remark 3.9.5(v),(vi), Ob3–9, Ob9-1 and (ix), pp.129–144; Remark 3.9.7(ii),(iii), pp.146–147; Remark 3.10.2, pp.151–152; Theorem 3.11(i),(ii), pp.153–156. Exact log dependencies checked: Remark 1.1.1, pp.28–29; Proposition 1.2(iv)–(x), pp.31–34; Remark 1.2.2(i)–(iii), pp.35–37; Theorem 1.5(i),(iii), pp.48–50; Proposition 3.5, pp.103–106; Proposition 3.10 and Remark 3.10.1(i), pp.147–150. Power dependency: FrI Proposition 2.1, pp.44–45, with its defining Frobenius-arrow uniqueness.

**Strongest actual log transport:** the specified Kummer/group/unit comparisons, finite containments, archimedean covering surjections, splitting-action compatibility, and global MOD Frobenioid isomorphisms. These do not yet constitute an orbit relation between the determinant presentations. Precise mod transport must not be inferred from MOD; the source expressly distinguishes them.

**Requiredness:** Ob8, sQ4 and (ix) explicitly place the adjustment on the audited route before the coarse scalar comparison. We do not infer requiredness merely because a universal diagram would be convenient.

**Weaker alternative:** a directly supplied orbit relation at the actual IPL objects could suffice. Its construction remains unresolved. This is why the verdict is not merely that a known source orbit transition is relational instead of functional.

**Decision:** RETRY this dependency. The minimal source-derived relation is not yet specified, so this is not ready for escalation as a fully formulated missing arithmetic theorem. No independent review request or countermodel has been launched.

## Section, W*, and scope

The exact finite fragment and the missing edge are in [MINIMAL_IUT_DIAGRAM.md](MINIMAL_IUT_DIAGRAM.md). The relational section criterion is in [SECTION_TEST.md](SECTION_TEST.md). There is no completed J_IUT/Y_IUT, native-q section, or W*. No generator or scalar consequence was computed. Removing a universal FormalSys requirement simplifies the audit but does not supply the missing transport, so PREVIOUS_FORMALSYS_REQUIREMENT_TOO_STRONG is not the verdict.

Proofs and source applications: [ORBIT_TRANSPORT.md](ORBIT_TRANSPORT.md), [CQ4_TRANSPORT.md](CQ4_TRANSPORT.md), and the complete field-by-field [transition inventory](PRESENTATION_TRANSITIONS.csv).

## Repository and provenance

Repository: `MoheetBrain/iut-bridge-audit`. Base: `codex/e3d-formal-system-lift`, commit `9e1c37e96deec1e7d1f344d9e80d1c7e6fce05d2`. New branch: `codex/e3d-presentation-transport`. Only the six requested files in this directory are added. Prior audit files, source pins and the pre-existing missing `recovery/2026-09-21/README.md` are preserved.

The seven prescribed E3d.1 files were read, and the concrete E3d definitions retained. Transition formulas were checked against pinned text and visual inspections of III pp.34,105,133–134 and FrI p.44, together with the previously checked cQ3/IPL displays. No later ELS account, paid compute, universal Pro construction, stack construction, or new broad IUT audit was used.

Validation on 2026-10-03:

- `python3 scripts/verify_sources.py`: PASS; 18 source pins/metadata records and 202 archived LANA files.
- `python3 scripts/validate_ledgers.py`: PASS; existing schemas, references, source locators, DAG and generated views.
- `python3 scripts/render_closed_loop.py --check`: PASS; 79 Stage 3.5 rows.
- `python3 scripts/render_membership.py --check`: PASS; 53 nodes, 76 edges, 83 lexical occurrences and 56 ordered pairs.
- `python3 -m unittest discover -s tests -v`: all 33 tests PASS.
- Read-only checks on the new artifacts: exactly six files; eight unique dependency-ordered CSV rows with 18 fields; one first-unsupplied row; valid local links and balanced fenced blocks.
- All 509 pre-existing tracked paths match the initial byte/missing-file snapshot, including all seven frozen E3d.1 files and the pre-existing deletion.

These tests certify source/provenance and artifact consistency only. They do not certify the new categorical arguments or IUT mathematics.

## Exactly one next mathematical move

Derive the cQ3 orbit relation induced by **one adjacent log-Kummer comparison**, starting from Proposition 3.5(ii)'s actual unit/domain correspondence and testing descent under postcomposition by Aut(D_B,v). **Not started beyond identifying this obligation.**
