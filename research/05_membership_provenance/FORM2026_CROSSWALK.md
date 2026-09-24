# Formalization 2026 crosswalk

The pinned April report is work in progress. Its Stage 1 concerns Theorem 3.11 → Corollary 3.12 (pp.3–4). The report says its skeletal code is not yet publicly released in that presentation; this audit verifies neither that code nor a completed Lean bridge.

The four triangles on p.10 have distinct roles:

1. BPS plus the 0-column constructs the multiradial representation up to Ind1/2/3 through the fixed full poly-isomorphism.
2. The descent arrow dsc expresses dependence on weaker BPS+etHT data.
3. HDD is **defined** as `(hull+det) composed with dsc`.
4. `HDD composed with SHE` restricts the input to BPS+etHT data supplied by the q-pilot construction.

Page 11 associates the fourth triangle with simultaneous comparison in one ring/common container and the final portion of the corollary argument. Its informal “3.11.5 = 3.11 + Rmk3.9.5” moves hull+det into the antecedent. The report explicitly says this numbered theorem does not occur in IUT I–IV. IPL appears both before and after that reorganization; APT is central in the second/third triangles; SHE+IPL labels the final arrow.

**Classification:** the fourth triangle is aimed at the final B1-style specialization/comparison **with B2-compatible output machinery already packaged into HDD**. It is not simply a stand-alone scalar-preservation lemma. The stated numerical aim covers both stages; the printed triangle itself does not spell out a separate Ob9 application or prove native output membership. Commutativity of a defined composite alone cannot serve as the B1 proof.

IUT_PRE → FORM: **SOURCE_CLAIM**. FORM → IUT_PRE: **PARTIAL**. FORM ↔ ELS: **PARTIAL** both ways. FORM ↔ LANA: **UNKNOWN** both ways. A full translation would need exact species/mutations, descent comparison, allowed indeterminacies and preservation of the native rigidification. Relabeling the antecedent “3.11.5” does not certify those proof obligations.
