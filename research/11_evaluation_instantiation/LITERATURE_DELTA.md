# Targeted source and literature delta

**Checked 2026-10-03.** This is a bounded search for the evaluation-to-hull application, not a controversy survey or an exhaustive priority search. The main derivation retains the previously inspected Y18 version. No AI commentary is treated as independent confirmation.

## Source identity and pagination

| ID | Version and location | SHA-256 |
|---|---|---|
| Y18 | Yamashita, *A Proof of the ABC Conjecture after Mochizuki*, [author PDF at abc2018Jan19.pdf](https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2018Jan19.pdf), 400 pages; same bytes as stage 10. The filename identifies the version; front matter retains placeholder publication dates. | `f160021befb3597c9dbe933f04e970c6837453049ed0c86c91ea8bbe39829ce1` |
| II | [Pinned IUT II](../../sources/primary/IUT_II.pdf), author version, December 2020, 174 pages. | `180bfa6aaddc4ae37af37acaad51f61e0a47b33b8255ad3169e28a970ae39b7c` |
| III | [Pinned IUT III](../../sources/primary/IUT_III.pdf), author version, May 2020, 199 pages. | `9a7ee3c77b1c7717210c0613eb39b6844649d0040dc3d9e1be7d544f8f91a0b9` |
| F26 | Mochizuki, [April 2026 preliminary formalization progress report](../../sources/primary/Formalization_2026_04.pdf), joint work in progress, 14 pages; pp.10-11 used as explanatory guidance. | `9a32b2485b5875574d7470256d3414b88ee6ac3ed8a39a82ea7332e25072ee9c` |
| Y24 | Yamashita, [author-linked June 25, 2024 revision](https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2024Jun25.pdf), 409 pages. The [author's works page](https://www.kurims.kyoto-u.ac.jp/~gokun/myworks.html) labels this the June 25, 2024 update. Publication dates in the PDF remain placeholders. | `3d61eacfd605f97ba6b329754b4b65c369610dfa1322c597cced0e9535308b9b` |

Printed page numbers and one-based PDF page numbers agree at the passages inspected. II, III and F26 remain pinned repository files. Y18 and Y24 were read from local temporary PDF caches, with their byte hashes checked; no unpinned replacement of a repository source was made. Their URLs may change, and the new report does not archive those PDFs. This is a reproducibility limit, not an access failure during this run.

## Changes that affect this proof attempt

1. **Actual radial morphisms.** Y18 Corollary 12.8, pp.317-320, and III Corollary 2.3, pp.72-75, retain an independently specified coric unit map alongside a theater-induced env/bad map, glued by a full poly-isomorphism. This gives the explicit choice calculation (4) in [PROOF_ATTEMPT](PROOF_ATTEMPT.md). It does not assert a pointwise commuting square for fixed native arithmetic realizations. II Example 1.7, pp.32-35, provides the underlying construction and explains its lift ambiguity. These are reconstructions of existing arguments.

2. **Quantifier clarification in the original IUT.** III Theorem 3.11(iii)(c)-(d), pp.157-159, makes endpoint-automorphism equivariance explicit; Remark 3.11.4, pp.171-172, explains the torsion-orbit and NF-set scope. This adds precision to Y18's shorter compatibility sentences. It supports a joint formal family, not a demand for a unique strict representative. III Remark 3.10.2, p.152, and 3.11.1(iii), pp.160-161, identify the actual evaluation/Kummer composite used in (11).

3. **Reference discrepancy, not a counterexample.** Y18 13.12(3)(d), p.351, points to `(2b)` for the final NF evaluation sentence. Its NF objects occur in `(2c)`, and III 3.11(iii)(d), p.158, points to (ii)(c). Y24 p.357 retains the `(2b)` pointer. The report records this discrepancy explicitly; it does not silently edit the source or use it as evidence against the mathematical claim.

4. **Newer author revision checked at the target.** Y24 locates (3)(c)-(d) at pp.356-357 and Corollary 13.13 at pp.359-360. The checked passage still invokes evaluation compatibility and then asserts the selected-region containment. It does not add a separate instantiated hull construction there. This is a comparison of those passages, not a claim that all 409 pages have been compared with Y18. The apparent 13.13/13.12 self-reference discrepancy in the corollary statement also remains.

5. **HDD/SHE guidance has a precise limit.** F26 pp.10-11 distinguish descent, hull-plus-determinant, and specialization to q-pilot input. They support keeping the final specialization separate from abstract switching. The definition `HDD=(hull+det) o dsc` does not by itself prove the specialization. No unpublished code or complete Lean proof was inspected or claimed.

## Bounded search record

Web searches used the queries `Yamashita "Corollary 13.13" "13.12"`, `Yamashita "13.12" "evaluation" abc`, `"Yamashita" "13.13" hull`, `site.kurims.kyoto-u.ac.jp/~gokun abc errata`, `site.kurims.kyoto-u.ac.jp "Formalization" "HDD"`, and `"IUT" "evaluation" "hull" "Hilado"`. The author's works page was then inspected directly, and its currently linked Y24 PDF checked locally. A 2019 author PDF also appeared in search results; it was not substituted for either checked version. Broad commentary and a generic common-container abstraction returned by search were not used as mathematical evidence.

The inspected results did not supply an additional completed specialization of (11) at the bounded determinant. This says nothing about novelty or the absence of such a derivation elsewhere. Scholze-Stix, Hoshi, Dupuy-Hilado and LANA were not reopened as a general survey; none is used as a premise in this attempt.

## Access and inspection record

Y18 text inspected: Definition 11.1 and Remark 11.1.1 pp.247-248; evaluation pp.277-279; Corollaries 11.21-11.23 pp.290-298; Theorem 12.5 pp.311-314; Proposition 12.6 and Theorem 12.7 pp.315-317; Corollary 12.8 pp.317-320; the relevant packet/log-Kummer/degree constructions pp.324-325, 333-345; Theorem 13.12 and Corollary 13.13 pp.345-353. Immediate context was used to type the maps, not to certify every preparatory proof. The source's deeper anabelian and theta-function results remain accepted inputs.

Fresh local renders were inspected for Y18 pp.295,315,318,319,350,351; III pp.152,158,185; and Y24 pp.357,360. Earlier stage 10 local-page inspections remain historical evidence only. No failed web screenshot is counted as a visual inspection. F26 pp.10-11 were read as text; the repository's prior renders of those pages are available, but no new visual check of them is claimed here.

The separate clarification beginning “Yamashita intends to obtain the comparison by multiradial switching...” was not found among the supplied attachments. Its interpretation and elementary lemma as reproduced in the task were considered, with no invented remainder and no attribution to a specialist reply. The user reports sending an email on 3 October 2026; delivery, reading and a reply are unverified. No correspondence was sent in this run.
