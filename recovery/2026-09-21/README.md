# Recovery record — 21 September 2026

This package recovers the IUT output identified in the user's screenshot and the final response from the existing `P= NP` task. The original files were located at `/Users/moheet/Documents/ChatGPT/IUT_CHALLENGER`, outside the P versus NP repository.

The source directory and Superlinear were left intact. Recovery checked every original audit file's SHA-256 and Superlinear's HEAD, branch, working-tree status, and 359 tracked file hashes before and after the copy.

## Inventory

- 316 original working files, totaling 30,798,254 bytes, were copied: four main deliverables, source documents, two third-party source working trees, extracted text and page data, rendered evidence, and the helper script.
- 314 destination files are byte-identical to their originals.
- Two files have portability-only edits: three companion links in `IUT_STAGE1_CRITICAL_BRIDGE.md` became relative, and `tmp/build_ledger.py` now derives its root from its own path. Neither change alters the mathematical content. Exact original copies are retained under `originals/`.
- The two nested `.git` directories were excluded so their source files belong to this repository normally. Original commit hashes, branches, remotes, and clean working-tree checks are recorded in the provenance file. Their existing license files were retained.

## Records

| File | Purpose |
|---|---|
| [ORIGINAL_FINAL_OUTPUT.md](ORIGINAL_FINAL_OUTPUT.md) | Exact recovered assistant response; its absolute links intentionally preserve the historical original locations |
| [IUT_STAGE1_STATUS.txt](IUT_STAGE1_STATUS.txt) | Exact status block extracted from that response |
| [RECOVERY_MANIFEST.csv](RECOVERY_MANIFEST.csv) | Original and destination hashes for all 316 recovered files, with any edits identified |
| [PROVENANCE.json](PROVENANCE.json) | Source task, original response time, copy location, repository revisions, and preservation checks |
| [STAGES_1_3_REQUEST_REFERENCE.txt](STAGES_1_3_REQUEST_REFERENCE.txt) | Unmodified attachment from the recovery request, stored as context rather than executed instructions |
| [VALIDATION.json](VALIDATION.json) | Completed file-integrity and structural checks for the recovered package |

## Scientific boundary

The recovered audit reports neither a proof nor a refutation. Its source-specific weakest premise remains unresolved; its approximation criterion is conditional. All six proposed equivalence implications remain marked `NOT_YET_FORMALIZABLE`. No faithful countermodel or new Lean bridge formalization is supplied.

The recorded next step—Remark 3.9.5(ix), especially cQ3/cQ4—was not started during recovery. The original `COMPUTE_SPEND_GBP: 0` is the previous audit's statement, preserved verbatim, not a new accounting claim. This copy operation verifies preservation and usability of existing artifacts, not the underlying mathematical assertions or the current state of upstream research.
