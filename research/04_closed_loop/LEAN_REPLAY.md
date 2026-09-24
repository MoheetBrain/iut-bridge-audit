# Exact pinned Lean replay attempt

**U10 remains open: build completion and imported axiom closure UNKNOWN.** The exact toolchain installed and ran; the targeted build made progress but hit the recorded 480-second bound. This is neither a Lean error establishing a failed theorem nor a successful kernel certification.

Commands actually executed:

```sh
/Users/moheet/.elan/bin/elan toolchain install leanprover/lean4:v4.32.0
/Users/moheet/.elan/bin/elan run leanprover/lean4:v4.32.0 lean --version
/Users/moheet/.elan/bin/elan run leanprover/lean4:v4.32.0 lake build Iut.Implication.Corollary23 Iut.Tripod.Main
```

The first command exited 0. The reported compiler was Lean 4.32.0, `arm64-apple-darwin24.6.0`, commit `8c9756b28d64dab099da31a4c09229a9e6a2ef35`. The user's default toolchain was not changed. The build ran in the disposable copy whose path is recorded in [LEAN_BUILD_REPLAY.json](LEAN_BUILD_REPLAY.json), not in the pinned source directory. It was terminated as a process group after the timeout (exit -15); its last reported progress was 2408/3526 build tasks. That denominator is progress at interruption, not a certified total dependency count.

All **12 dependency Git HEADs** match the exact revisions in the unchanged pinned `lake-manifest.json`; their expected and actual SHAs are recorded. All 202 pinned source files also remain byte-identical in the working copy. No `lake update`, version substitution or bridge axiom was used.

The complete install stdout/stderr is in [LEAN_REPLAY_ATTEMPT.json](LEAN_REPLAY_ATTEMPT.json). The complete version/build command arrays, stdout/stderr, timeout, dependency checks and result fields are in [LEAN_BUILD_REPLAY.json](LEAN_BUILD_REPLAY.json). These logs preserve the actual output rather than an abbreviated success claim.

`#print axioms` was **not executed**, since the requested imports had not finished building. The replay script records the intended commands for `Iut.statementII_of_cor312`, `Iut.cor312Variant_implies_abc`, its primed variant and `Iut.Tripod.abc_of_variant`, and executes them only after a successful exact-revision build. They remain conditional downstream results; even successful replay would not prove the source-faithful IUT bridge or solve η equality.

To repeat the bounded attempt in a fresh disposable copy:

```sh
python3 scripts/replay_lana_stage35.py
```

This writes a new build-attempt record and can download/build dependencies. Preserve the present logs before rerunning if historical attempts are required. Secondary replay did not block completion of the source reconstruction and gate.
