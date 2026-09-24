# Stage 3.5 source inspection record

All identifiers refer to the unchanged, hashed [source manifest](../01_source_lock/SOURCE_MANIFEST.csv). Page numbers below are one-based PDF indices; the printed pages of the cited IUT3 passages coincide. The full dependency corpus was not recursively proof-checked. A locator to a cited dependency does not mean its entire proof was reverified.

**IUT3 Remark 3.9.5 was read in full**, beginning at the end of p.126 and ending in the first portion of p.145. Coverage:

| Portion | Pages | Material inspected |
|---|---|---|
| (i)–(ii) | 127–128 | Region/hull classes, proper hull restriction, minimality and containment |
| (iii)–(iv) | 128–129 | Φ/Ξ hull approximants, nonemptiness qualifications, union-volume distinction |
| (v)–(vi) | 129–130 | Explicit upper set quotient, formal empty systems, induced hull comparisons |
| (vii) Ob1–Ob3 | 131–133 | Arithmetic modules versus regions; weighted determinant and structural-sheaf correction |
| Ob4–Ob6 | 133–135 | Tensor powers, naive Frobenius/roots, bounded-family hulls, approximation |
| Ob7 | 135–137 | Galois actions, same-label Frobenius-like units and splitting/value coupling |
| Ob8–Ob9 | 137–139 | Vertical mismatch, formal quotient indeterminacies and coarse invariant compatibility |
| (viii) | 139–141 | sQ1–sQ5, q/Θ-intertwining, retained-structure constraints |
| (ix) | 141–144 | cQ3 categories and local-global tuples, cQ4, iQ5, full-strip closed loop |
| (x) | 144–145 | Why general region categories or an immediate norm-to-Q replacement are insufficient |

The neighboring Remark 3.9.4 was read in full, pp.120–126, including Fn/equal-integral semisimplification, logarithmic comparison, the native splitting, tensor factors and archimedean version. Remark 3.9.6, p.145, was checked for its restricted region-compatibility scope.

Additional inspected primary passages in this run:

- **LANA_TEX:** lines 1890–2035, the detailed theta action including Steps 4–8; lines 2420–2559, schematic η algorithm and target. The omitted mono-theta environments and rough Gaussian formula are recorded as exposition boundaries. **LANA** PDF §9.1–9.3, pp.44–46, remains the equation-number authority; the two pinned report artifacts are not assumed identical versions.
- **IUT1:** Example 3.2(iv), p.71, root convention and splitting.
- **IUT2:** Definition 4.9(viii) and Corollary 4.10, pp.158–160, full prime-strips, pilots, evaluation and poly-isomorphisms. Earlier label/theorem references were followed as locators, not all recursively re-proved.
- **IUT3:** Remark 3.1.1, pp.94–97; Proposition 3.3 and Remark 3.3.2, pp.100–101; Proposition 3.4, pp.101–103; Proposition 3.5(ii), pp.104–106; Definition 3.8, pp.112–113; Proposition 3.9 and nearby remarks, pp.115–120; Remark 3.10.2, pp.151–152; Theorem 3.11(ii)–(iii), pp.155–158; Corollary 3.12 statement, p.174; proof xi-c–h and xii, pp.182–186; Remark 3.12.2(ii), pp.188–189, and (iv)–(v), pp.192–195.
- **FR1/FR2/ET/AT3:** exact dependency pointers are retained where the inspected primary passages invoke them. This run does not claim a new complete verification of their categorical reconstruction theorems.

Text extraction used the existing `tmp/*.pages.json` from the byte-identical recovered PDFs. Those caches are not the source authority; the pinned PDFs are. Visual inspection of newly rendered IUT3 pp.142, 174, 189 checked the category-pair clauses, explicit exclusion of native q from Ind1/2/3, divided-star diagonal label and logical AND display. The PNGs and exact successful commands are under `evidence/` and [PDF_RENDER_COMMANDS.json](PDF_RENDER_COMMANDS.json).

No source hash, upstream Lean file or dependency revision was changed. No Stage-4 mathematical search was performed.
