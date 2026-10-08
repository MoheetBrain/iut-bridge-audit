# Theorem studies and acceptance boundaries

## Coverage, versions and trust

OpenAI commit **fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb**, dated 8 October 2026, 05:20 UTC, is the current inspected source. Initial commit **adc7f1241b42e322a6451854ab7e4b4c146bf78a** exists. Complete preprints-subtree listings were compared. The repository-wide and OAI recursive trees are truncated; neither was used as a complete inventory.

The catalogue independently yields **372 families / 719 distinct manuscript links**, each matched to an actual current Git blob. Family IDs are noncontiguous: 045,061,070,123,163 are absent. All family descriptions were screened; manuscript titles/abstract metadata were inventoried. All **242 linked Lean scope documents** were retrieved. Catalogue-rejected rows explicitly mark full hypotheses and conclusions as uninspected metadata. The ordinal 0–5 score means inspection priority, not similarity or probability of truth. This is not an audit of 719 complete proofs.

The advertised **300/719 = 41.72%** formalization rate is a **RELEASE_CLAIM**. Independently counted units are 242 family scope documents, 173 YAML source articles, 200 named main-results entries and 416 comparator configs. These units differ; they do not independently certify 300 whole manuscript headlines. YAML says “Partial progress” and imports `lana-agents/iut`; that dependency does not discharge LANA's explicit Corollary-3.12 input.

History records three **WITHDRAWN** manuscripts: split abelian eightfold Weil classes, unrestricted Kuga–Satake correspondence algebraicity for K3 surfaces, and the rational Hodge conjecture for products of K3 surfaces. The originating defect is a sign error in stabilization-trace cancellation. Fourteen other manuscripts have fixes of mixed scope, including one obsolete citation; thirteen further manuscripts have dependent citation/version updates. No withdrawn theorem is used. Current032's principal CM theorem and its restricted/conditional K3 companions are distinct from the withdrawn assertions.

009/031 show no changes to common source blobs. For019, all eight main-paper section blobs of October6 are identical to the initial September24 edition: a dated/citation revision is not a proof repair. Principal001/032 current notes concern citations. These facts do not certify their mathematical correctness.

A **MANUSCRIPT_PROOF** here means a published argument is present. An inspected **FORMALIZED_EXACT_STATEMENT** is limited to the documented endpoint; no independent Lean kernel/comparator replay was performed. Only the restricted deductions in `PROOF_AND_FALSIFICATION.md` are independently checked here. The OpenAI theorem proofs and their complete dependency closure have not been independently certified.

## 1. Family031: the strongest arithmetic-domain candidate

Source: [031 main theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/sections/introduction.tex), `thm:main`, and the characters/generation/matching/identification sections.

Let F_i be number fields and E_i/F_i possibly infinite Galois extensions. Each E_i is solvably closed, meaning it admits no nontrivial abelian algebraic extension. For every **continuous open** homomorphism

\[
\alpha:\operatorname{Gal}(E_1/F_1)\to\operatorname{Gal}(E_2/F_2),
\]

the manuscript asserts a **unique contravariant field embedding** j:E_2 into E_1 such that `g j = j alpha(g)`. Cyclotomic compatibility is recovered, not assumed. If alpha is an isomorphism, j is an isomorphism carrying F_2 to F_1.

**Mechanism inspected.** Uchida's local correspondence starts with active decomposition/inertia information and auxiliary-prime-dependent exceptions. Global class-field characters are constrained by a logarithmic-rank lemma: m rows of n units satisfy strong joint multiplicative independence modulo roots of unity for **every nonzero integer combination**, with `m>n(n-1)`. An algebraic determinant becomes too small p-adically relative to its archimedean control; product formula forces full rank. This is not a statement about arbitrary local unit-group automorphisms.

Faithful signed representations over totally imaginary Galois extensions and finite-quotient amplification recover cyclotomic information. Uniform Kummer/S-unit multiplicity bounds control missed primes independently of the auxiliary prime. Frobenius-power comparison identifies characters. The final identification uses **one fixed coefficient prime**, while auxiliary primes vary; finite pigeonhole and compactness across composita synchronize conjugacies. Hoshi's theorem then produces the field embedding.

**Dependency interfaces checked.** Hoshi's 2025 published theorem is Theorem3.4 in the December2021 RIMS1955 author preprint: open global Galois homomorphism plus full cyclotomic compatibility iff equivariant field embedding. The February2025 revised RIMS1977 preprint, published2026, reformulates Uchida's conjecture via root/absolute-Galois conditions. Those preprints' main statements were read; publisher PDF endpoints returned non-PDF responses. They are not asserted byte-identical to published editions. The manuscript also depends on Uchida1979/1981, Chebotarev, class field theory and logarithmic-rank literature. Not all dependency proofs were independently rechecked.

**Novelty control:** the **isomorphism** reconstruction was already known to Uchida. The new claimed strength is arbitrary open homomorphisms. Applying031 only to a full poly-isomorphism would not automatically provide a new tool at the old IUT boundary.

**Verdict:** `TRANSFER_WITH_MULTIPLE_OPEN_LEMMAS`. Across lambda, the audit has no continuous open map between the required *global solvably closed* Galois groups with the actual arithmetic realizations and coupled choices. A prime-strip comparison is not that map by definition. Even a reconstructed field embedding must induce the particular Kummer comparison and attach the marked pilot to the bounded record. A field map is a sufficient proposed route, not a requirement imposed on original IUT.

## 2. Family019: recovering a point while retaining its realization

Sources: [019 exact statements](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-p-adic-section-conjecture-October-6-2026/build/sections/01-introduction.tex), `thm:section`, `thm:completion`; patching, tame/arbitrary roots, realization and section arguments.

For finite k/Q_p and X/k smooth proper geometrically connected of genus>=2, consider the **full arithmetic etale** extension

\[
1\to\Delta_X\to\Pi_X\to G_k\to1.
\]

The manuscript asserts a bijection between X(k) and continuous sections modulo Delta_X-conjugacy. A group isomorphism, quotient or tempered label is not a section of this specified extension.

The completion theorem fixes a rank-one norm on k(X), extending the p-adic norm with zero support and a prolongation to its separable closure. It places the **specified** separable closure in the completion H of a universal finite-etale tower inside the completed separable closure E. Its proof retains an H-valued point, not only the underlying Berkovich point.

**Existence mechanism inspected.** Tame metrized-complex lifting and Picard divisibility give roots on **all** inverse annular sheets. Separating edges first become nonseparating in an unramified cover. Mochizuki–Tsujimura resolution of nonsingularities reaches the appropriate stable model/collars. Arbitrary exponents use stable-Jacobian toric characters, multiplication pullbacks, period lattices and analytic unit roots. Patching all collars produces an actual finite etale algebraic cover after proper base-change descent. Composita, Galois closure and normality preserve the specified copy of each finite field in H.

The section proof uses decomposition/valuation recovery, a birational lift and cited Koenigsmann/Pop–Stix results; F.K.Schmidt rules out inequivalent henselian rank-one valuations. Injectivity uses Jacobian Kummer theory. The global companion requires extra finite-descent/diagonal-adelic/Stoll–Selmer inputs; local points do not automatically assemble globally. RNS and other cited dependencies are accepted at their interface, not fully independently recertified.

**Verdict:** `HYPOTHESIS_MISMATCH`, useful mechanism only. Proper genus>=2 full-section data do not match the IUT punctured elliptic/orbicurve and tempered prime-strip interface. Passing to a cover needs an actual compatible cover, transported section and native-marking descent; none is supplied. Even point recovery does not select the native Tate parameter, its powered Picard class or the bounded Theta realization. No019 Lean scope link is advertised.

## 3. Family009: the manuscript's existence versus Lean uniqueness

Sources: [mod-ell statements](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/build/sections/01-introduction.tex), [actual field existence](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/build/sections/07-field.tex), [compatibility](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/build/sections/08-compatibility.tex), [Bogomolov-Pop existence](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/build/reconstruction.tex), [equal-characteristic theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Reconstruction-from-Milnor-K-theory-modulo-the-characteristic-October-5-2026/build/build/sections/01-introduction.tex), [009 Lean scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/009.md).

Away from the characteristic: K/k and L/l are finitely generated over **algebraically closed constants**, relative transcendence degree>=2, characteristic different from ell. Data are K1^M/ell, K2^M/ell and the full product/Steinberg relations. Compatible linear isomorphisms reconstruct perfect closures and constants modulo **one F_ell^× scalar** on data and Frobenius ambiguity on fields in positive characteristic. In characteristic zero there is no Frobenius ambiguity. Trivial scalar ambiguity at ell=2 does not restore integer valuation information forgotten by a quotient.

The Bogomolov–Pop companion uses continuous pro-ell abelianizations with a compatible class-two central extension/commutator bracket, and asserts a bijection

\[
\operatorname{Isom}_F^i(K,L)\to
\operatorname{Isom}^c(\Pi_L^a,\Pi_K^a)/\mathbf Z_\ell^\times.
\]

The equal-characteristic-p companion recovers the **original** field and named constants from mod-p K1 and degree-two Steinberg relations, modulo one F_p^× scalar, without the perfect-closure/Frobenius ambiguity of the away-from-p version.

**Actual realization mechanism inspected.** Commuting-pair theory detects quasi-divisorial data. A **uniform** support bound for every member of a pencil `Theta[t-a]`, rather than separately finite supports, permits incidence recovery of curve subfields. Five anchors and Riemann–Hurwitz control residual maps. True divisors, rational subfields, point inertias and commuting quotient diagrams are then recovered.

In the mod-ell existence step, the exceptional divisor of a blowup at a common smooth point has `ord(t_i-t_i(P))=1` for all good functions. This detects simultaneous algebraic relations. Relation varieties for `(t,s,t+cs)` recover transported addition, align constants and assemble a field embedding; generation/perfection makes it onto. Common exceptional divisors propagate one scalar across rational pencils. In the Bogomolov–Pop proof, final existence explicitly invokes **Pop's global decomposition-graph/rational-quotient reconstruction**. The actual map and all quotient restrictions are retained; residual targets are not independently rescaled.

**Formalization boundary:** `OAI.BogomolovPop.main_graph_injective` proves that two already supplied field-isomorphism orbits inducing the same Galois-data orbit coincide modulo the stated ambiguities. It does **not** prove existence for every admissible data orbit. PhiGraph explicitly includes an actual inducing field isomorphism. The challenge `sorry` is the intentional comparator placeholder; a separate solution module supplies the advertised proof. The solution/Kummer imports and statements were inspected, but imported closure and kernel validation were not replayed. Allowed comparator axioms are propext, Quot.sound and Classical.choice; `enable_nanoda=false` alone is not evidence of failure.

**Verdict:** `HYPOTHESIS_MISMATCH` and `USEFUL_METHOD_ONLY`. Number fields have transcendence degree zero; curve function fields have degree one. Algebraically closed constants change the arithmetic input. The requisite preserved K2/Steinberg structure is not supplied by IUT unit-group identifications. Scalar/Frobenius orbit recovery does not retain an independently normalized native pilot.

## 4. Families001/032: shared reference across actual realizations

Sources: [Milne rationality](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/build/sections/00_intro.tex), [CM Hodge theorem](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/01-introduction.tex). Principal001: for an abelian variety over Qbar with good reduction, a rational Hodge class and complementary product of divisor classes on the reduction pair to **one rational number** in every prime-to-p etale and crystalline realization, including p=2. Algebraic specialization of all Hodge classes uses032. Principal032 asserts surjectivity of the rational cycle-class map to rational (r,r) Betti classes of every complex CM abelian variety, in every codimension.

001 compares two **actual rational quasi-isogenies on the special fibers**, from CM transport and a separate lift with prescribed weakly admissible flag. A shared rational divisor pairing fixes the local similitude scalar. 032 assembles balanced four-label tensors from nonzero surface periods, fixed theta inputs, actual correspondences and CM source identification. The mechanism is richer than arbitrarily identifying vector spaces.

**Verdict:** `USEFUL_METHOD_ONLY`. A nonzero reference fixes scale only after a genuine comparison relates the realizations. Stage13 has a reference but lacks its receiving specialization. No cohomology/quasi-isogeny interpretation of the actual horizontal native-to-hull operation is supplied. The surviving CM theorem needs independent proof scrutiny if used; the eightfold/K3 withdrawal neither certifies nor refutes it.

## 5. Family312: retain the attaching witnesses

Sources: [elementary expansion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/build/sections/00-introduction.tex) and [312 Lean scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/312.md). In the Ara–Henry convention, C is a Grothendieck coherator, X a boundary-cellular model, and an actual pushout attaches an (n+1)-disk along its source n-face. The elementary expansion is a weak equivalence on components and all based homotopy groups. Lean's selected endpoint is elementary expansion; later semi-model structure and full comparison with spaces are excluded. The solution import chain Main → HomotopyGroups → ElementaryExpansion was retrieved; the solution theorem signature matches the inspected comparator endpoint. Its deeper imports were not compiled or certified.

The mechanism uses dimension induction, interpretations ordered by cellular generators, matched cylinder endpoints and actual filler witnesses. Family317 has different strict higher-category/Street-nerve hypotheses. Neither identifies IUT formal-output systems with its models.

**Verdict:** `USEFUL_METHOD_ONLY`. Quotient-class agreement does not supply a matching middle witness. Stage9 already exposed this problem. A new encoding must prove a source-faithful matching/lifting lemma; arbitrary coherators or universal pro-stacks would repeat the rejected construction.

## Other mandatory and surviving controls

|Family|Scope and first mismatch|
|---|---|
|008|Rational GRT Lie equations, Ihara bracket, odd generators and weight completion; Lean excludes regularized transport and graph consequences. No relevant global/local profinite arithmetic map.|
|015|Fixed prime-degree n>=5 totally real torus packets with arbitrary local lattice type and discriminant tending to infinity equidistribute tightly to Haar. Lean scope excludes quartic/sextic companions. Asymptotic weighted averages do not bound one finite marked pilot. Exact localization bookkeeping is already present in Stage13.|
|033|Projective log pairs/orbifold fibrations with boundary hypotheses. Lean selected additivity covers negative-fiber branch only; finite and negative-base branches are excluded. Geometric Kodaira dimension is not p-adic log-volume.|
|034|Log abundance/conditional Kahler minimal models, positivity and effectivity. No canonical-bundle interpretation as the corrected IUT hull determinant. No family scope link; supporting code is not a complete family proof.|
|057|Special complex Kahler groups virtually abelian; stated open complex linear images virtually class-two nilpotent. Wrong specialness and topological/linear pi1 input.|
|208|Finite symmetric tensor categories over algebraically closed characteristic-p constants have fiber functors to higher Verlinde levels. Frobenioids are not these finite linear tensor categories.|
|209|Integral Gersten counterexamples in K3/K5 on explicit two-dimensional mixed-characteristic-(0,5) regular local rings. Wrong K-theory degree; no necessary IUT Gersten-injectivity premise located.|
|240|AEC eventual categoricity; separate CH threshold obstruction. Lean selected endpoint is CH obstruction, not the full eventual-categoricity theorem. Cardinal uniqueness is not marked Frobenioid reconstruction.|
|243|Finite unordered CPT/counting and strictly stronger witnessed symmetric choice. Useful witness/history discipline, but no finite CPT encoding of the arithmetic source algorithm.|
|245|System-wide weak beta normalization implies strong beta normalization for arbitrary pure type systems. No such typed IUT system or global weak-normalization premise supplied; beta normalization is not arithmetic degree.|
|317|Strict n-category Thomason models, finite n>=1 and omega, with Street nerve and specified Quillen adjunction. No source equivalence to IUT formal enclosing-region systems.|

## Public methodology

The October README reports approximately 4,000 posed problems, a mostly fixed procedure, significance filtering and an unreleased internal model, with three Pro-thinking-equivalent hours per result on average. That is not a cost estimate for our audit. CM and zeta work are exceptions; one zeta exposition was human edited. The August release describes human manuscript preparation and formal artifacts for that earlier selection; it does not certify all October papers.

There are ten abridged public reasoning summaries, not full private inference transcripts. Targeted reading of197 Kaplansky and221 Mezard–Parisi illustrates repairs through counterexamples, characteristic-dependent scalar/matrix checks, retaining witnesses, rejecting too-strong conditional identities, changing represented states and checking normalization constants. The releases do not establish the precise sequential/parallel internal search protocol. We do not possess the internal model or hidden process.

The reproducible improvement is: start at the first **typed open arrow**; test the smallest claimed invariant against the actual ambiguity group; distinguish `forall data, exists witness` from `given witness, unique`; inspect comparator endpoints; retain source-side witnesses before quotienting. A graph node or a newly defined admissibility predicate is not progress unless it proves an actual source lifting/calibration/effectivity/approximation assertion.
