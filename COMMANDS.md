# Reproduction and command record

## Stage 3.5 addition — 2026-09-24

Branch `codex/stage-3-5-closed-loop` starts at exact commit `ecd62b5f6f82eae722c9dcc68e5e0c83c3186f47`. The prior deletion of `recovery/2026-09-21/README.md` remains unstaged. Source inspection, renders and the exact Lean replay are recorded in `research/04_closed_loop/READING_LOG.md`, `PDF_RENDER_COMMANDS.json` and `LEAN_REPLAY.md`. The new canonical source ledger is `STAGE35_DATABASE.json`; regenerate/check with `python3 scripts/render_closed_loop.py` / `python3 scripts/render_closed_loop.py --check`. The new validation record is `research/04_closed_loop/VALIDATION_RESULTS.json`.

The command record below describes the earlier Stages 1–3 run. Its statement that no Lean replay was attempted is historical and is superseded by the exact-toolchain timeout record above.

All relative paths below are relative to `/Users/moheet/Documents/ChatGPT/IUT 🧮` (the clone of `https://github.com/MoheetBrain/iut-bridge-audit.git`). This run creates branch `codex/stages-1-3-audit` from recovered-source commit `5098565e7f88e75718344702640d5d769e3f3074`. `sources/metadata/WORKTREE_BASELINE.json` records the pre-existing changes. No command targets P-vs-NP/Superlinear for mutation.

## Acquisition and pinning

Executed to acquire the bounded corpus:

```sh
python3 scripts/acquire_sources.py
```

The source log retains each URL, retrieval time, result and hash. Python's TLS handshake initially failed for SS. This exact fallback succeeded:

```sh
curl --fail --location --max-time 45 --silent --show-error --output sources/primary/Scholze_Stix.pdf https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf
```

The acquisition script now includes that curl fallback, refuses different-byte overwrites and preserves the first acquisition log by writing later runs to timestamped logs. Mutable author URLs may return changed bytes later. To reproduce this snapshot, use the saved files and verify their pins; do not update a hash to hide a mismatch.

The immutable download URLs are in `SOURCE_MANIFEST.csv`. Remote branch-tip checks used during pinning and repeated for the final record are saved with exact argument arrays/results in `sources/metadata/REMOTE_REFS.json`. They establish what the public branches returned at those checks, not their state forever.

The code archive was compared in memory against all 202 recovered source files, without extracting over the recovered snapshot. `verify_sources.py` reproduces this comparison. Every original overlapping recovered source PDF/TeX hash was compared against its new pinned copy; all 15 match. The pinned downloaded code and all inspected code are byte-identical.

## Source inspection

The PDF skill was used for source inspection only. Page extraction used pypdf; the pre-existing `tmp/*.pages.json` files correspond to the identical recovered source bytes. DH v2 was extracted to `research/01_source_lock/DUPUY_HILADO.pages.json` with bundled Python:

```sh
/Users/moheet/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 - <<'PY'
from pathlib import Path
import json
from pypdf import PdfReader
src = Path('sources/secondary/Dupuy_Hilado_Initial_Theta_Data_v2.pdf')
out = Path('research/01_source_lock/DUPUY_HILADO.pages.json')
out.write_text(json.dumps([page.extract_text() for page in PdfReader(src).pages], ensure_ascii=False, indent=2) + '\n')
PY
```

The following page rendering was executed; all three images were visually inspected for the printed algorithm and notation:

```sh
pdftoppm -f 44 -l 46 -scale-to 1700 -png sources/primary/LANA_report_202607.pdf research/02_eta_reconstruction/evidence/LANA
```

Page numbers in the ledgers are one-based PDF indices unless otherwise specified. Source inspection focused on the locators recorded in each row; the entire dependency corpus was not recursively proof-checked.

## Derived research views and source-code audit

The authored database is `research/RESEARCH_DATABASE.json`. Prose target/admissibility/gate documents are authored analysis; CSV tables, schemas, algorithm, question and candidate-invariant views are generated. Update the database first, then run:

```sh
python3 scripts/audit_lana.py
python3 scripts/render_ledgers.py
python3 scripts/build_dependency_graph.py
python3 scripts/verify_sources.py
python3 scripts/validate_ledgers.py
python3 scripts/render_ledgers.py --check
python3 scripts/build_dependency_graph.py --check
python3 -m unittest discover -s tests -v
```

The latest executed offline validation commands, exit codes and output are saved in `research/VALIDATION_RESULTS.json`. Checks use Python's standard library; the fixture tests do not invoke Lean or assert mathematical facts. `.gitignore` excludes Python caches. `.gitattributes` preserves byte-exact upstream sources and excludes their existing whitespace from authored-file checks. Generated CSVs use LF line endings.

The code audit masks nested Lean comments/strings and inventories local imports/declarations. The selected closure includes the generic, concrete, anabelian-model and tripod consequences. It is not a Lean parser or elaborator. No exact Lean 4.32.0 kernel replay or external dependency axiom inspection was executed; no generated Lean file or alternate-version replay is presented as certification.

## Final repository checks

```sh
git diff --check
git diff --cached --check
git diff --stat
git status --short
```

Only the files belonging to this audit are staged. The pre-existing deletion of `recovery/2026-09-21/README.md` is left unstaged. Historical root reports and recovered source files are not rewritten.
