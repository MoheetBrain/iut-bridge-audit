# Source priority and evidence discipline

Audit date: 2026-09-21. Scope: Stages 1–3. Source IDs resolve through `SOURCE_MANIFEST.csv`; each has a matching JSON metadata record in `sources/metadata/`.

1. **IUT1–IUT4** govern their own hypotheses, constructions and conclusions. The author's current downloadable PDFs are pinned by SHA256. A hash fixes bytes; it does not certify a theorem.
2. **LANA** governs the report's η reformulation. **LCODE** governs what its pinned Lean code actually defines or proves conditionally. Neither is silently substituted for the full IUT structures [C004, C007–C008, C015].
3. **ELS, FORM, REPLY, ALIEN** are primary evidence for Mochizuki's explanations and responses. Distinguish a claimed compatibility from a completely checked derivation [C009, C014].
4. **SS** is primary evidence for Scholze–Stix's criticism. A criticism is not adopted as a faithful countermodel merely because it is published by its authors.
5. **DH** is clarificatory literature for IUT initial data. Its v2 explicitly excludes the multiradial construction [C019]. It is secondary for assertions about Mochizuki's theory; its own new results are its authors' primary work.
6. **IUT1, IUT2, IUT4, ET, AT3, FR1, FR2, ALIEN** are the bounded additional dependency set: initial data; splitting monoids/rigidity; downstream arithmetic; étale theta normalization; reconstruction/log-shells; Frobenioid realization; structured-copy explanations. No unrelated corpus expansion was undertaken.

## Evidence labels

- **SOURCE FACT:** a verifiable fact about what a pinned text or code contains.
- **SOURCE CLAIM:** a mathematical assertion of that source whose full dependency proof is not certified here.
- **RECONSTRUCTION:** this audit's translation or organization, retaining stated restrictions.
- **INFERENCE:** a stated deduction with its premises, not a quotation.
- **OPEN QUESTION:** an uncompleted source-fidelity, typing or proof obligation.

The claim `status` is separate from `evidence_type`. `VERIFIED_PRIMARY` can certify that a paper states a result; it must not be read as a recursive proof audit. Source claims and reconstruction rows record that difference explicitly.

## Pins and locators

PDF pages are one-based PDF page indices. LANA's inspected printed numbers coincide with these indices. Journal page numbers are not substituted by guessed offsets. File/line citations refer to the immutable LCODE commit `2d8f000457da6447fa4df4bfec7365c1a49b6384`.

LANA's report PDF is from branch `pdf`, commit `b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676`. Its main-branch TeX/bibliography are separately pinned at `293bdd89463473ae13d40834d70fb4b7ba81da1f`. Earlier section numbering differs [C011]; PDF citations do not automatically cite the TeX. Author PDFs without immutable URLs are fixed by saved bytes, retrieval time and hash. Re-downloading an author URL later is not equivalent to reproducing this snapshot.

## Recovered work

The older root reports, `sources/` snapshot and `recovery/2026-09-21/` provenance came from the earlier misplaced audit. They remain historical inputs. Current mathematical claims were checked against the pinned passages/code; their authority does not come from those reports. No P-vs-NP/Superlinear file is an input to the mathematical specification or a target of edits.

The pre-existing deletion of `recovery/2026-09-21/README.md` is recorded in `WORKTREE_BASELINE.json` and is excluded from this change. The root README is rewritten under the present request.
