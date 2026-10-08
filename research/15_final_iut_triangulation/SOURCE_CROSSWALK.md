# Joshi–IUT source crosswalk

8 October 2026. **The focused test was not already completed.** A search of the research archive found only Stage 14's discussion of Construction III's final Theorem 9.11.1/Corollary 9.11.1.1 and the separate untilt theorem. It found no prior audit of 9.8.1, 9.9.4 or 9.10.8.1. This run starts at `09a6ce36ff1f055063fc65992487c39ecbf56987`, without repeating the OpenAI catalogue, localization, Rss or local Hom calculations.

## Source objects before audit notation

In [Construction III v4](https://arxiv.org/pdf/2401.13508v4), §§2.4,3.1,3.3, pp.25–30, the inputs include a totally imaginary number field L, a punctured elliptic curve X=C\{O}, its field of moduli Lmod, a Galois extension L/Lmod containing C[6], and a prime ell>=5 not dividing [L:Lmod]. The mod-ell image must contain SL2; L'=L(C[ell]); one chooses a set V of places of L' bijective with the places of Lmod. The relevant bad places have **odd residue characteristic and split multiplicative reduction**. These global conditions are retained as source inputs; no isolated local field is substituted for them.

At a finite place w, an untilt point provides an embedding L'_w into a characteristic-zero perfectoid field K_y with a specified tilt. The adelic Ansatz is an m-tuple of such points, m=(ell-1)/2. The standard tuple z_Theta has its **last** coordinate y_m equal to the standard point y_0 (§§4.4–4.5, pp.35–36). Tate parameters are computed for the given curve in these labelled arithmetic structures. They are not independently chosen arbitrary positive numbers.

Two constructions must be kept separate:

* **Period-ring lifts:** §§6.4–6.6, pp.45–49 define tuples `[u_j]+i_j(lambda)t_{K_j}` in `B_{L'_w}^m`, using Teichmuller lifts, a Lubin–Tate Tate-module generator and a **common** lambda in O_{L'_w}. Their images under the respective untilt quotient maps recover the selected theta/Tate values. At the other places the tuple is ([1],...,[1]). These capital-Xi tuples form a period-ring locus, subsequently enlarged by §5.3's operations.
* **Crystalline cohomology classes:** §§9.6–9.7, pp.108–112 instead use the Kummer class of the **1-unit** `1+p* q_w^(1/(2 ell))`, with p*=p for odd p and p*=4 at p=2. These classes belong to H_e^1(G_{L'_w},Z_p(1)), after the cited p-adic Hodge input. The source's normalized logarithm is `log_p(1+p* q_w^(1/(2 ell)))/p*`. This is not the nonunit native Kummer class `[q_w^(1/(2 ell))]` itself. Its norm is recoverable by Lemma 9.8.2.7, not by identifying the two classes.

Theorem-Definition 9.8.1.1, pp.113–116, constructs **lowercase xi** tuples of cohomology classes, adds the auxiliary 1+p* entries for the procession, collates their images in a standard arithmetic structure via Proposition 9.7.5.1, and takes convex closures. Its subsequent tensor images are called `tilde Theta^I_Mochizuki` and `tilde Theta^I_Joshi`. Theorem 9.11.1's notation capital Xi from 9.8.1 therefore needs this type distinction; a period-ring lift cannot simply be fed to log_BK without a specified cohomological construction.

Only now use these audit names:

| Name | Actual meaning in this audit |
|---|---|
| A_J | The collated tensor-image locus **defined by Joshi** in 9.8.1(4)–(6), using his Mochizuki-labelled codomain. Its name does not establish identity with original IUT. |
| H_J | Its hull for the split-field integral structure, when defined. The ordinary closed Z_p convex hull is denoted C_J separately. |
| A_IUT | The correlated possible outputs of original IUT III Theorem 3.11, subject to its prime-strip, Kummer/evaluation and Ind1/2/3 conditions. It is not every class in a log-shell. |
| H_IUT | The original hull of the collection of possible regions, with the corrected weighted determinant `det^tensor M`, formal quotients and degree comparison of Remark 3.9.5(vii)–(ix). |

## The actual translation test

| Construction III location | Correspondence tested | Result and assumption boundary |
|---|---|---|
| 4.2.2.1, pp.32–34 | Ansatz gives j^2 valuation scaling | Explicit construction via the local precursor's 6.9.1. Accepted at that scope. It does not construct original IUT's bounded output. |
| 4.4–4.5 | Standard z and Tate parameters | Specified within Joshi's labelled family. Standard coordinate is j=m; this matters numerically. |
| 6.4.3,6.6 | Admissible capital-Xi lifts | Admissible **by Joshi's period-ring definition**, with common lambda and labelled quotient maps. IUT admissibility is not proved by this definition. |
| 8.3,8.5–8.7; Rosetta fragments | Groups, units, monoids and labels | Gives candidate objects, isomorphisms and analogies. No theorem here supplies a marking- and bound-preserving translation of the entire algorithmic output. |
| 9.4.2.4, pp.101–102 | Restriction/corestriction | Their composite is multiplication by n_w=[L'_w:Lmod,v]. This explains a local extension-degree factor, not the complete packet/procession/determinant normalization. |
| 9.4.6–9.4.9, pp.103–106 | Product/tensor presentations | Containers are explicitly defined. The pure-tensor operation is multilinear, **not** a homomorphism from the additive direct product; 9.9's wording cannot justify linear functoriality. Set images can still be taken. |
| 9.6–9.7 | Crystalline class from native Tate data | Retains the input q **before collation**, through a nonlinear 1-unit encoding and a normalized logarithm. Root choices modulo torsion do not themselves establish receiving native provenance. |
| 9.7.5.1, p.112 | Collation into a standard structure | Union of images under all the topological isomorphisms supplied by the cited amphoric cohomology result. No explicit subgroup calculation proves that these are precisely the original IUT permitted indeterminacies or preserve its receiving q-degree. |
| 9.8.1(7), p.116 | These loci “are” IUT's multiradial representations | **Claimed identification, not independently established translation.** The proof says to assemble preceding facts. Remark 9.8.1.2 acknowledges that these crystalline classes are not used by Mochizuki. |
| 9.9.7, p.121 | Recover multiplicative theta action | Equality of the computed **norms** does not establish equality of actions, allowed histories or hull incidence. |
| 9.10.8.1, p.126 | Holomorphic hull equals convex closure | False as a universal assertion under the stated finite-dimensional hypotheses; explicit tensor-lattice counterexample in PROOF_OR_OBSTRUCTION. One-sided inclusion survives. |
| 9.11.1, p.127 | Lower volume bound from standard classes | Claimed for Joshi's locus, via 9.9.1 and 9.10.7.1. Internal norm calculation can be recovered; receiving normalization and full-region containment remain additional requirements. |
| 9.11.1.1, p.128 | Original IUT Corollary 3.12 | Literal printed signs are inconsistent in the nonempty bad-place case; see NUMERICAL_COMPARISON. Correcting the signs still does not prove the object/normalization translation. |
| Appendix 10.11.3–10.11.5, pp.139–141 | Build Hodge theaters/Frobenioids | Provides objects from holomorphoids and an Lmod projection. Does not instantiate cQ3/cQ4 with the same native input and independent H_IUT bound. |

The immediate collation dependency was checked: [II½ v12](https://arxiv.org/pdf/2305.10398v12), 7.4.1 and 7.5.1, pp.48–50, assert cohomology isomorphism classes and unions of images under those topological isomorphisms. They do not add the missing bounded-output comparison. [II v3](https://arxiv.org/pdf/2303.01662v3), 8.7.1, p.25 explicitly distinguishes its period-ring locus from Mochizuki's locus.

Construction IV v2, §§5.7–5.8, pp.53–58 supplies a claimed global initial-data existence theorem; its full proof is not independently verified here. Its 6.10.1, pp.65–68 compares Frobenius-shifted and standard arithmeticoids with simultaneous number-field normalization, invoking Construction III and IUT IV. Identical normalization of the number field alone does not prove identity of the measured collated hulls. Frobenius stability is relevant candidate input, but must be attached to the actual locus and its measure. The [Final Report](https://arxiv.org/pdf/2505.10568v1) is the author's assessment, not another proof of these translations. No author position is adopted on authority.

## Original target cross-check

Original III Remark 3.9.5(ix)cQ3/cQ4, pp.141–143 requires local-global structured comparisons before passing to coarse volume data. Proposition 3.9, pp.115–117 fixes packet normalization and the procession average. Remark 3.9.4 allows weaker numerical comparisons, so no canonical field map across the theta-link, full determinant-orbit transport or exact witness is imposed. Corollary 3.12(xi-d–f), pp.183–184 consumes native-q coverage, possibly by approximation; (xii), pp.185–186 preserves the global normalization issue. Remark 3.12.2(ii), pp.187–189 does not authorize arbitrary line identifications.

Yamashita June 2024, 13.12(3)c–d, pp.356–357 retains evaluation and NF localization compatibility up to the stated indeterminacies; 13.13, pp.359–360 claims an **isomorphic**, not equal, q-region in the hull. Neither is a theorem about Joshi's enlarged collation family. These prior IUT/Yamashita inputs remain accepted at their stated scopes, with their recursive verification incomplete.

Scholze–Stix §2.2, pp.9–10 concerns coherent arithmetic-degree identifications and j^2 scaling. Writing down j^2 is insufficient to answer it. Conversely their compressed diagram is not imposed as the necessary form of original IUT's proof. LANA July 2026, pp.46–49 asks for equation (9-1), `eta^q = eta^anab_S`, and distinguishes this from the hexagon. Neither that variant equality nor its equivalence to original IUT is derived here.

## Frozen source provenance

The arXiv histories checked on 8 October 2026 still list III v4, IV v2, II v3, II½ v12 and Final Report v1 as latest. Page numbers below are printed/PDF one-based numbers, which coincide for the cited passages. New PDFs remain in the temporary retrieval cache; only the four requested reports are committed. Explicit version URLs and hashes permit reacquisition.

| Source | Version and SHA-256 |
|---|---|
| [Joshi III](https://arxiv.org/pdf/2401.13508v4) | 24 February 2025 v4; `86a92ca893e774e1ea591ed9825a30627f3f19d8df0b26b7f5855dc0923f0429` |
| [Joshi IV](https://arxiv.org/pdf/2403.10430v2) | 24 February 2025 v2; `ef8851fe656c705f7e9881778b4dd0c592c9f35a2980be6a335412a15542547a` |
| [Joshi II](https://arxiv.org/pdf/2303.01662v3) | 24 February 2025 v3; `a25e58456673d905f6be328773926ec8a5dbb419fe278ca478827f163ccdf4af` |
| [Joshi II½](https://arxiv.org/pdf/2305.10398v12) | 24 February 2025 v12; `6fd09e29096eeafc52589f6ef3f06dee2f944614c116ef9892316c2b4e3c74c0` |
| [Joshi Final Report](https://arxiv.org/pdf/2505.10568v1) | 29 April 2025 submission, v1; `8594bb5218dbc778c6d61cf362589d61509c6c43693091cc95beb1ee93aedac8` |
| [Original IUT III](../../sources/primary/IUT_III.pdf) | May 2020 author version; `9a7ee3c77b1c7717210c0613eb39b6844649d0040dc3d9e1be7d544f8f91a0b9` |
| [Scholze–Stix](../../sources/primary/Scholze_Stix.pdf) | July 2018 pinned version; `4ec276246a2a92d2e211a0dae5afd073b5eae7e2b37e9bbabe3cb82c7e0b34a0` |
| [Yamashita June 2024](https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2024Jun25.pdf) | 25 June 2024; `3d61eacfd605f97ba6b329754b4b65c369610dfa1322c597cced0e9535308b9b` |
| [LANA report](../../sources/primary/LANA_report_202607.pdf) | July 2026 PDF-branch `b8e4636edea64d0b9fdc1d7f6a51e63c1f5d1676`; `aa53093aa8d69dbce5f8fb4f541069a418650260dee1ef532917aa8db89606c7` |
| [Schneider, Nonarchimedean Functional Analysis](https://www.uni-muenster.de/IVV5WS/WebHop/user/pschnei/lectnotes/nfa.pdf) | Author-hosted text retrieved 8 October 2026, convexity definition Chapter I §2; `aea90059bb94d6f5a822995742fc418a66671327da1545cfeb64ce29dc0649bf` |

Visual inspection confirmed III v4 pp.121,126,128 and original III p.127. In particular, it recovered absolute-value bars missing from text extraction on Joshi p.128. A fresh download of the explicit III v4 URL also matched the recorded hash. Historical source pins were not replaced.
