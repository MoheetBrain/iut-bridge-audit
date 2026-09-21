# Source map and retrieval boundary

Prepared by **Astra (Codex)**, 2026-09-21. Page numbers below are PDF/preprint page numbers, not journal pagination. Source claims are paraphrased in the registries; the PDF remains authoritative for mathematical typography.

## 1. Current-version checks

On 2026-09-21 at approximately 04:39 UTC, the six principal PDFs below were fetched again from their primary URLs. Every SHA-256 matched the recovered source file. This checks these endpoints as of retrieval, not every possible draft or unpublished revision. The full machine-readable receipts are embedded in `IUT_STAGE1_DEPENDENCY_GRAPH.json`.

| ID | Primary source | SHA-256 | Directly inspected critical scope in this audit |
|---|---|---|---|
| III | [IUT III](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf) | `9a7ee3c77b1c7717210c0613eb39b6844649d0040dc3d9e1be7d544f8f91a0b9` | Remark 3.9.5 pp. 126–145; R3.10.2 p. 152; Theorem 3.11 pp. 153–159; R3.11.1 pp. 159–166; Corollary 3.12 statement/proof pp. 173–185, including xi-b–g. This is selected-page reading, not whole-paper verification. |
| CMT | [Mochizuki Comments on Scholze–Stix](https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-05.pdf) | `d71c38308322bdb403b11c6f450f8f67797600c5c9ac7c28505c8d1c43c1f53b` | Comments pp. 4–8, particularly C12–C14 p. 5 and C17–C18 pp. 6–7. Response position, not an independent adjudication. |
| ELS | [Essential Logical Structure](https://www.kurims.kyoto-u.ac.jp/~motizuki/Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf) | `c0e63b629aa174aa065e93d08defe3e5d0837c8778aab527383798baf8ca6e32` | Section 3.10 pp. 144–156, including Stp1–8 and FxGl/NoCmpIss/Englf. The text was indexed for AND/OR, common-container, and closure terms; other sections are not certified as fully read. |
| FORM | [Formalization of IUT (2026-04)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Formalization%20of%20IUT%20%282026-04%29.pdf) | `9a32b2485b5875574d7470256d3414b88ee6ac3ed8a39a82ea7332e25072ee9c` | April 2026 note pp. 10–11: four triangles, HDD and informal 3.11.5 decomposition. Does not certify the mathematical interfaces of the skeletal code. |
| SS | [Why abc is still a conjecture](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf) | `4ec276246a2a92d2e211a0dae5afd073b5eae7e2b37e9bbabe3cb82c7e0b34a0` | Section 2.2 pp. 9–10 and adjacent discussion of the numerical comparison. Not a proof of an IUT-faithful scalar abstraction. |
| LANA | [LANA report (2026-07)](https://raw.githubusercontent.com/katobungen/LANA_report_202607/pdf/LANA_report_202607.pdf) | `aa53093aa8d69dbce5f8fb4f541069a418650260dee1ef532917aa8db89606c7` | July 2026 report pp. 45–49: §9 comparison, (9-1), §§10.2–10.5 criticism comparison and provisional assessment. |

The local PDF pages III 184, FORM 11, and LANA 46 were also rendered and visually inspected to check the membership, decomposition diagram, and η-map types against text extraction. Other mathematical expressions were checked in the extracted page text; typography-sensitive unresolved statements were not silently promoted to formal definitions.

## 2. Earlier dependencies and explicit read-depth limits

The recovered root-level ledger points into the following dependencies. Only the pages explicitly marked as re-read below were directly re-read in this audit. The other entries record a **previous audit's pointers**, not newly verified hypotheses or proofs. Local files are hash-pinned; unlike the six sources above, their public endpoints were not all fetched again in this audit.

| ID | Primary dependency | Version hash | Coverage / boundary |
|---|---|---|---|
| I | [IUT_I.pdf](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf) | `7360e3ed27c235b5497a0743d3ed1646fbb97688547d16b7c784fc7f127f1f03` | Re-read Definition 5.2(i)–(iv), pp. 134–135, for prime-strip/global-local types. Definition 3.1 and anabelian references remain source dependencies, not re-proved arithmetic infrastructure. |
| II | [IUT_II.pdf](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf) | `180bfa6aaddc4ae37af37acaad51f61e0a47b33b8255ad3169e28a970ae39b7c` | Re-read pp. 157–160: Definition 4.9(v)–(viii), Corollary 4.10(i)–(v) opening. Earlier parts of Definition 4.9 and the rest of Corollary 4.10 are recovered pointers. The full local construction/Kummer proof chain is unexpanded. |
| FRI | [Frobenioids_I.pdf](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf) | `8e5ac14e3aadb457ee4edde81a325b64b060cefb14712d70cf2ca66b373aaf53` | Recovered pointers: Theorems 5.1, 5.2, 6.4, pp. 96–97, 100–101, 114–115; III cQ3 also cites Definition 1.3(i). Not independently re-read/re-proved here. |
| FRII | [Frobenioids_II.pdf](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20II.pdf) | `0185e64c4107123a20d2fd72f6e5a5ff8e5c1356d3caee69b7d5700e291ac0a9` | Recovered pointers: Theorem 1.2 pp. 9–10; Example 5.6(iii)–(v) pp. 62–65. III cQ3 cites the local/global functors. The altered quotient-category construction is not certified by citing these functors alone. |
| ABS | [AbsTop_III.pdf](https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20in%20Absolute%20Anabelian%20Geometry%20III.pdf) | `e8115df30a86dea26e2ebf60cb333558ff28fe3e4d57017a80421787b53421a9` | Recovered pointers: Propositions 5.7–5.8 pp. 137–141, normalized log-volume and its restricted compatibility. Not independently re-proved here; no unrestricted measure-preservation assertion is imported. |
| ET | [Etale_Theta.pdf](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf) | `42c5d9180c69bc9fa6596ce1a11662494315954ed74301060bf1819f955a7406` | Recovered pointer: Proposition 1.4(iii), pp. 20–21; mono-theta/Kummer rigidity is also cited by III. No arbitrary scalar substitute is licensed. |
| IV | [IUT_IV.pdf](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf) | `5bf4b1e0a8c2686562a6859e5009d301335044cfb5efec5d3a9edf764e4af87f` | Dependency pointer for species-theoretic input/output labels in ELS Stp7, and downstream estimates. No new whole-IUT/abc verification attempted. |
| ALIEN | [Alien_Copies.pdf](https://www.kurims.kyoto-u.ac.jp/~motizuki/Alien%20Copies,%20Gaussians,%20and%20Inter-universal%20Teichmuller%20Theory.pdf) | `b2510b7276ab08f9f758e283200a4fc87205d2439d6d9b75afe8df6ccb182d1e` | Re-read §3.11(v), cld1–cld9, pp. 143–146. The first page also ends the preceding numerical analogy; that analogy is not used as a faithful countermodel. |

These dependencies are recorded because the critical passages invoke them, not as a mandate to formalize their entire subject areas. A recursive traversal would add further anabelian, Frobenioid, and Kummer prerequisites. **That traversal is incomplete.** Accordingly the audit neither declares a precise P* absent from IUT nor describes its extracted ledger as a complete `H_pre`.

The nearest unresolved interfaces are III R3.9.5(v)–(ix) (formal quotient and local/global collections), the input/output contract assembled with R3.10.2 and Theorem 3.11, and its numerical interpretation with the fixed q normalization. These are the graph's U01–U03. U04 records the translation to LANA (9-1); U05 records the missing faithful abstraction/preservation argument for the scalar criticism.

## 3. Public formalization records

Read-only `git ls-remote` checks on 2026-09-21 returned:

| Repository | Ref | Commit | Inspected meaning |
|---|---|---|---|
| [lana-agents/iut](https://github.com/lana-agents/iut) | HEAD / main | `2d8f000457da6447fa4df4bfec7365c1a49b6384` | README honesty boundary and `Iut/Cor312/Statement.lean`; the Corollary 3.12 variant is a Prop-valued definition, deliberately distinguished from the published algorithm. |
| [LANA-Project/iut4-sec1](https://github.com/LANA-Project/iut4-sec1) | HEAD / main | `a7551d2f575b7e462cf9e82c587d9c6308e7b15c` | README scope and explicit interfaces/certificates; section-IV development is not certification of the disputed III bridge. Comparator challenge templates were not treated as proven results. |
| [LANA July report](https://github.com/katobungen/LANA_report_202607) | HEAD / main | `293bdd89463473ae13d40834d70fb4b7ba81da1f` | Report repository ref; PDF fetched independently and hash-checked above. |
| [LANA July report](https://github.com/katobungen/LANA_report_202607/tree/pdf) | pdf | `b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676` | PDF branch containing the checked report. |

[Immutable variant statement](https://github.com/lana-agents/iut/blob/2d8f000457da6447fa4df4bfec7365c1a49b6384/Iut/Cor312/Statement.lean).

The two code heads matched the recovered source-snapshot provenance. No Lean build was run and no new Lean file was created. This is not an exhaustive audit of all public Lean repositories, proof dependencies, or their current trust bases. A `def ... : Prop` and a lemma unfolding that definition are not a proof of the proposition. Equally, lack of such a proof does not imply a false theorem.

## 4. Search and provenance limits

The recovered audit and source manifests were retrieval aids. A targeted primary-source web search and direct endpoint/repository checks located the required materials; journalistic commentary and unreviewed search snippets were not used as mathematical evidence. No claim of a comprehensive novelty search is made.

The target and comparison issue already appear in the named primary sources. Prior-art risk is therefore high even without a broader search. The strongest new output here is an auditable separation of established outer typing, unexpanded structured interfaces, and unsupported inferences. It is not a new IUT theorem or flaw.

No separate Stage-0 package was located in the inspected IUT/Superlinear project context. The user's Stage-0 status is not presented as independently retrieved evidence. The older root-level Stage-1 files remain historical; this directory applies the newer instruction to **stop at D**.

## 5. Artifact integrity

The six files in this directory constitute the deliverable. The CSV rows carry source locations and typed relation labels. JSON edges explicitly have `proof_edge: false`; they encode dependencies/context, not a certified derivation. Later explanations, competing formulations, and xi-f/xi-g are separated from the pre-xi-f ledger. Registry IDs, source references, twelve directed comparison entries, and local hashes are checked by a small consistency script kept outside the repository.

No files from the parity/Superlinear programme were changed. Existing unrelated IUT work and source acquisitions are not included in this deliverable.

Consistency validation passed: 42 object rows, 38 source-claim rows, 103 graph nodes, 290 dependency/context edges, and all 12 directed formulation comparisons. All relation/status labels and referenced IDs were valid; all local artifact links resolved. The 326 previously tracked IUT paths matched their content baseline, including the pre-existing edited README and deleted recovery README. Superlinear's working tree remained clean. These are artifact-integrity checks, not mathematical proof verification.
