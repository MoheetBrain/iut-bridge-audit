# Pilot specialization via localization reconstruction

**2026-10-04 — SAME_REALIZATION_BOUNDARY_STILL_OPEN.**

The source's localization recipe has been expanded and applied to the MOD portions of the fixed Gamma_chi. It reconstructs more than a principal-divisor test: it gives the valuation quotient, its nonnegative cone, the realified divisor localization and localization of a supplied global torsor with its local trivializations. It does **not**, in the completed derivation, construct the native-marked receiving datum in the same formal record as the bounded Theta-hull determinant. No numerical Gamma defect or new nontrivial global inequality is established.

## What changed beyond eb2cf594

[LOCALIZATION_RECONSTRUCTION](LOCALIZATION_RECONSTRUCTION.md) supplies explicit formulas for the omitted localization calculation. For a global element acting in one distinguished tensor factor, the packet-normalized local increment is `log|m|_w`. Its contribution to the full packet is `([F_w:Q_u]/[F:Q]) log|m|_w`, with the separate procession average. The tensor dimensions and selected-extension factors cancel as shown in (R1)-(R4). Direct-product change of variables proves independence from the test region.

The map `m -> -log|m|_w` recovers the kernel of local units, the quotient of the perfection, and its nonnegative cone. Its ordered real-ray extension, with I 3.5's actual factor `1/[K_v:F_w]`, gives the divisor localization. Pushing out the source torsor and retaining its local trivializations extends this to supplied line objects. An arbitrary realified Picard element is not substituted for that torsor record.

A positive divisor supported at one finite place supplies a **nonzero** calibration reference, of normalized degree `([F_w:Q_p]/[F:Q]) log(p)`. This is distinct from the total principal divisor of p, which has degree zero. The reconstruction therefore does not merely recover zeros or orientation. What remains unverified is the transport of this marking, or a sufficient marked specialization of the native class itself, through the entire horizontal/coric application into the record used for D_H.

These are the genuinely new results. The local Hom-set construction and rational diagnostic from stage 12 were not repeated.

## Actual application and first unresolved operation

[PILOT_SPECIALIZATION](PILOT_SPECIALIZATION.md) retains

`Gamma_chi = d_1^e A_1^e h_E K_0,E (A_0^F)^(-1) lambda^(-1)`

and the same fixed `(0,0)->(1,0)` record. The reconstruction is instantiated on `K_0,L`, the jointly transported MOD/NF record associated to `T_L`, and the same-presentation MOD-to-mod comparison `d_1^e`. Its naturality is proved by subtracting the two volume values in the matched action square. Ordinary II 4.6 Kummer quotients are not confused with the MOD-derived log-compatible construction.

The last actual datum is `z_chi=gamma_chi([Q_M])` with its abstract pilot/local divisor record and the reconstructed MOD torsor-localization maps. The attempted next operation was to identify its native-marked specialization with a receiving arithmetic or formal term measured by the **independent** corrected-determinant normalization of D_H. The prescribed coric arrow, the compensating delta_1 and the same NF family remain part of that test.

Remark 3.11.2(iv) applies to the MOD group actions just instantiated and concludes reconstruction of localization maps. This calculation does not supply the additional marked receiving term or show that a choice of ordinary receiving Theta-pilot is the same permitted comparison. In particular lambda's full-prime-strip type does not itself provide the action-intertwining equation used for the MOD components. Requiring a field map across lambda would be excessive; a source-defined marked formal term could suffice. None was constructed here.

Accordingly:

| Requested output | Result |
|---|---|
| Native receiving datum y_chi in the D_H record | Not constructed |
| Its normalized value or numerical Gamma defect | Not reported; no such datum was obtained |
| Same-record effective residual / bounded selected term | Not derived |
| Compatible calibrated approximation family | Not constructed |
| Original nontrivial inequality b>=a | Does not follow from this run |
| Fatal flaw, nonexistence theorem or faithful countermodel | None established |

The native degree a is finite, negative and nonzero under the given initial Theta-data. Finiteness of b remains separate. The elementary b>=0 case is immediate; it does not close the finite negative case. Exact attainment, uniqueness, raw-output membership and all-orbit transport have not been imposed as necessary conditions.

## Accepted inputs and source access

The categorical and anabelian reconstruction theorems, Kummer/evaluation algorithms, NF coupling, stated equivariance, product formula and vertical small-region compatibility are accepted at their stated scopes. Their full proofs and deeper dependencies were not independently reverified. The new arithmetic deductions are the weighted action calculation, quotient/cone construction, explicit divisor normalization and torsor pushout, and the scope test of their application. [SOURCE_INSTANTIATION.csv](SOURCE_INSTANTIATION.csv) records 21 source instances and limits.

All calculations use the repository's pinned primary PDFs. Printed and one-based PDF page numbers agree at the inspected passages.

| Source | Version; pages | SHA-256 |
|---|---|---|
| [IUT I](../../sources/primary/IUT_I.pdf) | May 2020; 186 | `7360e3ed27c235b5497a0743d3ed1646fbb97688547d16b7c784fc7f127f1f03` |
| [IUT II](../../sources/primary/IUT_II.pdf) | December 2020; 174 | `180bfa6aaddc4ae37af37acaad51f61e0a47b33b8255ad3169e28a970ae39b7c` |
| [IUT III](../../sources/primary/IUT_III.pdf) | May 2020; 199 | `9a7ee3c77b1c7717210c0613eb39b6844649d0040dc3d9e1be7d544f8f91a0b9` |
| [Frobenioids I](../../sources/primary/Frobenioids_I.pdf) | June 2008; 126 | `8e5ac14e3aadb457ee4edde81a325b64b060cefb14712d70cf2ca66b373aaf53` |

The exact recipe at III pp.119,168-169 was not already expanded in research reports found by the repository search. Required stage 11/12 files were read; the previous numerical-control suite was not rerun. The direct source dependencies checked include I 3.5 and 5.2(iv); II 4.6(v), 4.10; III 3.1.1, 3.3, 3.6-3.7, 3.9, 3.9.6, 3.10 and 3.11; FrI 6.3-6.4. Six fresh source renders were visually inspected: III pp.94,119,169; I pp.84,135; II p.139. Display inspection confirmed the local/global divisor-map type and the reciprocal extension-degree factor.

The [author-hosted III PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf) was accessible and identifies the May 2020 version. The committed derivation remains tied to the local hashes, not to a later unpinned download. There was no primary-source access failure. The limitation is the mathematical instantiation and the accepted-proof boundary, not inaccessible files.

## Validation and continuity

`python3 scripts/verify_sources.py` passed the 18 source pins/metadata records and 202-file LANA archive check. `python3 scripts/validate_ledgers.py` passed schema, evidence-label, locator, foreign-key, nine-step, DAG and generated-view checks.

A new, temporary exact-rational control checked the coefficient calculation (R3), restricted-packet renormalization, the procession factor and (R7). It enumerated local-degree lists `(1,2,3)`, `(2,2)`, `(1,1,2)`, capsule widths 1, 2 and 4, and each distinguished place, using selected-extension degrees `n_v=v+2`. For each tensor tuple with its first place fixed, it summed `prod(n_v*d_v)/(prod(n_v)*d^width)` and verified `d_w/d`; division by that coefficient gave 1, division by a five-capsule average gave `d_w/(5d)`, and the local rho factor gave `(n_w*d_w)/(n_w*d)=d_w/d`. All 24 configurations passed. This tests the new normalization calculation only; the general proof is in (R2)-(R4). No new test file is committed and the old 171-case suite is not counted as progress.

Source/reference checks establish artifact integrity; arithmetic controls establish only their stated identities. Neither certifies the IUT bridge.

Artifact checks passed for exactly four requested files, 21 unique complete CSV records, 11 local links, balanced display/code delimiters and unique equation tags. All four cited source hashes and PDF page counts were rechecked. Comparison against the initial snapshot of 530 tracked paths found only the intended STATUS.md change; the pre-existing recovery README deletion remained untouched. The staged set is limited to the four outputs and STATUS.md.

Repository: `MoheetBrain/iut-bridge-audit`, root `/Users/moheet/Documents/ChatGPT/IUT 🧮`. Actual starting SHA: `eb2cf594fea860c9a35b43e1941966396ef91ab1`. Continuation branch: `codex/pilot-picard-specialization`. Fetch and branch checks found no existing continuation under that name. The Git root, remote, ancestry and working changes were checked. No applicable AGENTS.md was found. Only these four new files and a brief STATUS notice are intended changes. Historical reports and the pre-existing deletion of `recovery/2026-09-21/README.md` are preserved. No other project, email, reminder, submission or paid/cloud/GPU service was used. Additional spend: GBP 0.

## One next decision

**STOP.** This explicit reconstruction has reached the same marked receiving/boundedness boundary after supplying its missing localization calculation. Retain the exact application test in PILOT_SPECIALIZATION, section 6; do not automatically launch another renamed audit stage.
