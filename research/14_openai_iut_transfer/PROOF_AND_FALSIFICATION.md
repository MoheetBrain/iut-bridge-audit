# Proof attempt, falsification and typed dependency graph

## Acceptance boundary

The strongest **theorem-transfer** attempt uses Family031. Its source theorem is not independently certified here; the restricted normalization lemma below is proved from actual field-map hypotheses. The follow-up strategy selected in `STRATEGIC_VERDICT.md` is a different, bounded negative-invariant test. That follow-up sprint has **not** been launched.

Root A: no bridge validated. Root B: no faithful obstruction/countermodel. Root C: no novel source-instantiated supporting theorem. Restricted standard lemmas and counterexamples below cannot change those outcomes.

## 1. The precise 031 application attempted

Accept the 031 main theorem at OpenAI commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`: a continuous open homomorphism of Galois groups of solvably closed Galois extensions of number fields is induced by a unique contravariant field embedding. See `HIGH_PRIORITY_THEOREMS.md` for its full input and source URL.

The proposed source substitution is **not** `alpha=Gamma_chi`. Gamma_chi is the already constructed composite on the arithmetic/Picard comparison side. One would first have to extract an actual group map `alpha_chi` from the **same** admissible prime-strip/evaluation record, between specified global Galois extensions, and prove it induces the Kummer comparison used in Gamma_chi.

|031/application assumption|Proposed IUT substitution|Audit result|
|---|---|---|
|Number fields F_0,F_1|Non-realified NF records in the two selected holomorphic realizations|Native/vertical record available before forgetting; the required receiving record in the bounded construction is not independently supplied.|
|Specified solvably closed E_i/F_i|Solvable closures of those exact fields|Can be formed for supplied fields; does not identify the relevant prime-strip groups with their Galois groups.|
|Continuous group homomorphism alpha|Map extracted from the actual coupled comparison|**OPEN_LEMMA**. Full prime-strip poly-isomorphism alone is not this global group map.|
|Open image|Openness of that exact alpha|**OPEN_LEMMA**, conditional on its construction.|
|Group isomorphism, if using placewise calibration|A selected isomorphism from the full poly-family|**UNVERIFIED** as a global Galois statement. Iso case of reconstruction was already known to Uchida.|
|Field-induced Kummer map|The source's K0, h, A and evaluation maps|Same-h vertical compatibility is established in Stage11/13 scope; horizontal/receiving identification remains **OPEN_LEMMA**.|
|Matching local extensions, tensor factor, M and weights|The same packet/procession/localization record|Stage13 computes these once supplied; transporting them to the missing bounded record is **OPEN_LEMMA**.|
|Native pilot and output comparison|Image of x_q in the corrected hull's formal record|**OPEN_LEMMA**; not a conclusion of031.|

Thus there is not one small omitted hypothesis. The first open arrow is constructing the correct **global Galois map**, with source compatibility. Subsequent marking and hull arrows remain even if it succeeds.

## 2. Restricted field-calibration lemma — proved

**Statement.** Suppose j:F_2→F_1 is an actual isomorphism of number fields. Let w_1 correspond to w_2 under j, and normalize each finite absolute value by its restriction to Q. Use the degree weights `d_w/d`. Suppose the source comparison on local multiplicative classes is actually induced by the extension of j, and the paired tensor/packet/procession records have the same exponent M, indexing and distinguished factor. Then, for every supplied multiplicative element m,

\[
\frac{[F_{1,w_1}:\mathbf Q_p]}{[F_1:\mathbf Q]}\log|j(m)|_{w_1}
=
\frac{[F_{2,w_2}:\mathbf Q_p]}{[F_2:\mathbf Q]}\log|m|_{w_2}.
\]

The corresponding nonzero positive single-place Picard reference and weighted degree are preserved. A native local pilot is calibrated **if** the actual receiving Kummer realization is induced by this local field map and has the same source power/root conventions.

**Proof.** A unital characteristic-zero field isomorphism fixes Q, hence p. It maps the valuation ring and its maximal ideal at w_2 to those at w_1. Discrete valuation and ramification index are equal, so the absolute values extending the Q_p normalization agree. It extends to an isomorphism of completed local fields. Both global degrees and local Q_p-degrees agree. Substituting proves the displayed equality. The formal component reference for p has positive degree `(d_w/d) log p`, so its image has the same nonzero degree. A real-linear comparison on that one-dimensional Picard line fixing this reference has scalar 1. Tensor powering multiplies both degrees by M; the same packet/procession averaging divides equally. Apply the same map to every coefficient/reference in the Stage13 pilot expression. This proves the claim from its hypotheses. □

For a mere embedding F_2→F_1, **individual** place weights need not agree. The valid statement is the aggregated pullback formula:

\[
\sum_{w_1\mid w_2}\frac{[F_{1,w_1}:\mathbf Q_p]}{[F_1:\mathbf Q]}
\log|j(m)|_{w_1}
=\frac{[F_{2,w_2}:\mathbf Q_p]}{[F_2:\mathbf Q]}\log|m|_{w_2}.
\]

Indeed the normalized absolute value of j(m) is equal at each extension place, and the sum of local relative degrees is `[F_1:j(F_2)]`. Global degrees cancel that factor. This does not identify arbitrary individual IUT local q-pilots with a global principal element.

**What is new here?** This explicitly tests the proposed OpenAI×Stage13 chain and its normalization. The lemma is standard field/valuation functoriality, not a novel Root-C theorem. The isomorphism part would already follow from existing Uchida reconstruction. It neither constructs y_chi nor proves boundedness against D_H.

## 3. First attempted new lemma and where it fails

**Proposed application lemma (unproved):** the actual permitted cQ4/evaluation comparison underlying Gamma_chi induces the field/Kummer map in §2 on a positive integral valuation reference, within the **same** receiving formal record as D_H, or supplies a weaker source-faithful replacement sufficient for the numerical comparison.

Backward attempt:

1. IUT III cQ3 provides structured local/global categorical presentations and cQ4 unit/Galois/evaluation compatibility (Remark3.9.5(ix), pp.141–144).
2. Stage11 constructs a same-h radial lift and NF localization comparison, yielding the abstract coupled composite. Stage13 calibrates its supplied action-on-volume record.
3. To apply031, those comparisons would have to yield a global Galois homomorphism between the two particular non-realified NF realizations. Neither cQ3's categorical pair nor cQ4's unit-group compatibility has been shown to produce that map across lambda.
4. Replacing a unit-group isomorphism by a field embedding would assume the very hypothesis that must be proved. Replacing the receiving NF record by an arbitrary field copy would lose the source marking and output history.
5. Even granting that map and §2's calibration, the image must be represented/compared in the permitted bounded hull record. No031 conclusion establishes containment, effectivity, residual control or source-admissible approximants.

The attempt therefore stops at the first input translation. This is a **failed application**, not a disproof of031 or IUT. No artificial field-map requirement is made necessary for all possible source proofs.

## 4. Concrete scalar controls — independently checked

### Cyclotomic compatibility is insufficient for a separately chosen Kummer map

Take k=Q_5 and ell=3. The identity G_k map preserves the full cyclotomic character. On `Z_3(1)`, multiplication by2 is a G_k-equivariant automorphism, since the action is scalar. It induces multiplication by2 on

\[
H^1(G_k,\mathbf Z_3(1))\cong\widehat{k^\times}_{3}.
\]

Under the Kummer identification, `[5]` is sent to `[25]`. The valuation quotient is Z_3: these classes have values1 and2. Hence cyclotomic compatibility of the group map plus an independently selected equivariant coefficient/Kummer isomorphism does **not** imply valuation calibration. The field-induced map for identity is identity; coefficient multiplication by2 is not that induced map.

This falsifies the shortcut “cyclotomic-compatible ⇒ every accompanying equivariant Kummer map preserves the marked valuation.” It is **not** a counterexample to031,009 or original IUT. IUT includes additional mono-theta/global rational-integral restrictions; 2 is a unit in Z_3 but not in the full profinite integer unit group. In particular `Q_{>0} intersect Zhat^×={1}` excludes it when those compatible global hypotheses are actually present. Whether those restrictions act on the missing receiving specialization is the source question, not assumed here.

### Mod-ell data cannot directly retain integer valuation

In Q_5^× modulo cubes, `[5]=[5^4]`, because their ratio is `5^3`. Their integer valuations are1 and4. This is an elementary quotient-information control, **not** an instance or refutation of009's transcendence-degree>=2 theorem. The corresponding pro-3 classes distinguish1 from4 in Z_3; the two controls concern different data levels.

### Primitive-reference rigidity, with the required hypothesis exposed

Let V be a Z_ell-module with a surjective valuation map `v:V→Z_ell`. If a Z_ell-linear T preserves `ker(v)`, its induced quotient map is multiplication by some c in Z_ell. If a supplied reference r has `v(r)=1` and `v(T r)=1`, then c=1 and `v(T x)=v(x)` for all x. Proof: the quotient is rank one, and c is its value at the generator. For actual k^× representatives, the embedding Z→Z_ell is injective, so equality of these values gives equality of integer valuations. A pro-ell class need not be the specific actual receiving representative; that existence/marking obligation remains. Equality of weighted real degrees additionally requires the same prime, local/global weights, power and procession conventions.

This elementary lemma proves exactly what one primitive marked reference would fix. It does not construct that reference's output image and is not a new publication-level theorem. FrII Remark5.6.3 supplies an existing integral-lattice rigidity mechanism at its own stronger compatible categorical input.

## 5. Multi-paper chains: first unproved arrow

|Combination|Complete proposed chain|First open arrow and residual issue|
|---|---|---|
|019+009|Actual IUT section/curve datum →019 rational point with marked local realization →009 compatible high-dimensional K1/K2 datum →field realization →native Picard calibration →bounded hull comparison|First arrow has proper/full-section mismatch. The next one has dimension/constants mismatch; no common restricted hypothesis package was constructed. A point does not supply K2 or a hull.|
|031+IUT localization|Actual global alpha_chi →031 field embedding →field-induced Kummer/localization map →Stage13 weighted degree →admitted bounded comparison|First global map open; iso part already known. Matching Kummer map and hull attachment are further open arrows.|
|009+Frobenioids|Preserved IUT symbol datum →009 field/valuation reconstruction modulo ambiguities →compatible ordered integral divisor/localization datum →FrII degree1 →native bounded realization|Preserved compatible K2 datum and dimensional fit fail first. Scalar quotient cannot silently provide integral marking.|
|001/032+simultaneous comparison|Actual shared cohomological realizations + actual quasi-isogenies →001 rational pairing, with032 for cycle existence →shared nonzero reference →calibrated IUT receiving term →hull bound|No supplied cohomological/quasi-isogeny realization of the actual IUT comparison. A formal nonzero reference is already known; its receiving map is still needed.|
|009/312 Lean method+LANA|Precise source witness relation →existence theorem for compatible witnesses →endpoint-preserving quotient composition →normalized bounded comparison →LANA h312 →conditional ABC|Source witness relation and existence theorem unproved. Injectivity/PhiGraph or elementary expansion cannot be used as the existence proof. LANA still explicitly assumes h312.|

None replaces the gap with a solved arrow. A generic combination containing multiple new hypotheses is not `TRANSFER_WITH_ONE_NEW_LEMMA`.

## 6. Typed dependency graph with source locations

IDs are local to this report; no historical graph was rewritten. `SOURCE_CLAIM` records a theorem/compatibility printed in a source without independent recertification. `PROVED_FROM_STATED_INPUTS` records the exact conditional scope. Formalized endpoints were inspected but not rerun.

|Edge|From → to|Type|Location / mathematical reason|
|---|---|---|---|
|E01|IUT full cQ3/cQ4 record → native constrained closed loop|SOURCE_CLAIM|IUT III Remark3.9.5(ix), pp.141–144.|
|E02|Same-h radial/evaluation/NF input → Gamma_chi|PROVED_FROM_STATED_INPUTS|`research/11_evaluation_instantiation/PROOF_ATTEMPT.md`, radial lift and composite; Yamashita2018 13.12(3)c-d pp.350–351 /2024 pp.356–357.|
|E03|Supplied global multiplication/packet/localization record → weighted action on volume|PROVED_FROM_STATED_INPUTS|`research/13_pilot_picard_specialization/LOCALIZATION_RECONSTRUCTION.md`; IUT III Proposition3.9 packet normalization p.115 and Proposition3.5 localization.|
|E04|Actual coupled IUT comparison → global solvably closed Galois alpha_chi|OPEN_LEMMA|§1 hypothesis table above; III cQ4 pp.143–144 /Stage13 RESULT do not supply this type across lambda.|
|E05|Global open alpha +031 hypotheses → equivariant field embedding|SOURCE_CLAIM|031 introduction `thm:main`; identification section final application of Hoshi.|
|E06|Cyclotomic-compatible global alpha → field embedding|SOURCE_CLAIM|Hoshi RIMS1955 Theorem3.4, printed pp.11–13; 2025 publication.|
|E07|Actual field isomorphism + matched weights → calibration|PROVED_FROM_STATED_INPUTS|§2 proof, with Stage13 weighted formula. This scope is standard and already compatible with Uchida iso reconstruction.|
|E08|Reconstructed field embedding → particular Gamma_chi Kummer map|OPEN_LEMMA|§1/§3; exact same-h vertical maps are insufficient to identify horizontal receiving map.|
|E09|Calibrated abstract pilot image → bounded receiving record|OPEN_LEMMA|Stage13 RESULT; Stage5 MINIMAL_BRIDGE; III xi-e–xi-f pp.183–184.|
|E10|Admitted approximants with a-epsilon<=LV<=b → a<=b|PROVED_FROM_STATED_INPUTS|Ordered-real epsilon argument; Stage10 REVIEW_NOTE. No existence of approximants proved.|
|E11|Proper genus>=2 full section → rational point|SOURCE_CLAIM|019 introduction `thm:section`, section07.|
|E12|IUT punctured tempered comparison →019 section input|HYPOTHESIS_MISMATCH|019 introduction versus IUT I Definition3.1 and III cQ4; no full section/cover translation.|
|E13|Specified all-sheet cover/point input → specified field in H|SOURCE_CLAIM|019 sections03 patching,04 tame roots,05 arbitrary roots,06 realization.|
|E14|IUT number/curve field →009 field-theorem input|HYPOTHESIS_MISMATCH|009 mod-ell introduction `thm:main`: algebraically closed constants, trdeg>=2.|
|E15|Compatible mod-ell symbol datum → field existence|SOURCE_CLAIM|009 section07 `thm:field-isomorphism`, simultaneous-values/constant-alignment arguments; section08 scalar compatibility.|
|E16|Class-two group datum → compatible decomposition/rational graph|SOURCE_CLAIM|Bogomolov-Pop curve recovery and reconstruction `reconstruction:pop`.|
|E17|Compatible full graph/quotients → field existence|SOURCE_CLAIM|Bogomolov-Pop reconstruction invoking Pop2012 graph Isom theorem.|
|E18|Two actual inducing field maps with same orbit → uniqueness|FORMALIZED_EXACT_STATEMENT|009 scope; comparator BogomolovPopInjectivity; solution main_graph_injective. Source inspection, NO_KERNEL_REPLAY.|
|E19|Injectivity alone → existence for all data|REFUTED|Logical implication fails: an injective map can have empty domain/nonempty codomain. §4/009 PhiGraph explicitly includes an actual witness.|
|E20|Independent equivariant Kummer map + cyclotomic-compatible alpha → calibrated valuation|REFUTED|Q_5,ell=3,multiplication-by2 control in §4. Not a faithful IUT model.|
|E21|Primitive quotient reference fixed → valuation map fixed|PROVED_FROM_STATED_INPUTS|§4 rank-one quotient proof; actual representative and real-degree data remain extra inputs.|
|E22|Compatible integral local Frobenioid lattices → degree scalar1|SOURCE_CLAIM|Frobenioids II Remark5.6.3 p.65, with Example5.6(v); compare FrI6.4(ii)-(iv).|
|E23|Realified category equivalence alone → scalar1|UNVERIFIED|FrI6.4(ii) supplies only positive real scalar; Stage12 RESULT distinguishes calibration assumptions.|
|E24|Actual001 quasi-isogenies/divisors → common rational pairing|SOURCE_CLAIM|001 introduction main statement and proof mechanism;032 only for algebraic specialization corollary.|
|E25|IUT comparison →001 cohomological input|OPEN_LEMMA|001 hypotheses versus Stage13 actual Gamma_chi; no supplied variety/cohomology/quasi-isogeny model.|
|E26|Coherator/cellular pushout → elementary weak equivalence|FORMALIZED_EXACT_STATEMENT|312 scope/comparator `elementary_expansion`; full later comparison excluded; NO_KERNEL_REPLAY.|
|E27|IUT formal system →312 model/cellular pushout|OPEN_LEMMA|Stage7 TYPE_VERDICT; no source-justified coherator interpretation.|
|E28|Compatible local Rss charts → numerical native preservation|PROVED_FROM_STATED_INPUTS|Stage9 LOCAL_CALCULATION, unit-chart integration quotient.|
|E29|Rss preservation → admissible hull history|OPEN_LEMMA|Stage9 DECISION; Stage10 REVIEW_NOTE; numerical labels do not prove provenance.|
|E30|LANA h312 + supplied downstream data → ABC|SOURCE_CLAIM|Current Iut/Tripod/ClassicalAbcGenuineCanLift.lean `classicalABC_of_variant_genuine'`; no kernel rerun here.|
|E31|Original IUT bounded construction →LANA variant input/h312|OPEN_LEMMA|Current Iut/Cor312/Statement.lean explicitly makes thetaPilot an input and disclaims proved correspondence.|

The cheapest concrete falsifier is E20. It blocks an invented shortcut. The first substantive031 source-application arrow is E04. Neither becomes an original-IUT flaw without the full source hypotheses and permitted weaker comparisons.

## 7. Adversarial acceptance audit

All eleven controls were applied: wrong dimension (009); proper/punctured and etale/tempered (019); existence/uniqueness (009 Lean); field recovery/theta-link mismatch (031); scalar ambiguity (§4); local/global assembly (Stage12/13 and alternatives); labels alone (008/033/034); formalization scope (009/033/312/LANA); circular admissibility (no assumed hull witness); excessive historical requirements (no global Step6 section, full orbit necessity or exact representative mandate); withdrawals and revisions (current version/statement scope checked).

No candidate passes input, morphism, existence, marking, normalization, choice, bound and original-theorem matches together. **No direct transfer, one-open-lemma transfer, faithful obstruction or novel source-instantiated Root-C theorem is established.**
