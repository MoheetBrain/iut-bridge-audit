# LANA source-code audit

**SOURCE FACT [C007–C008, C021, C025, C027].** Repository: `lana-agents/iut`; branch: `main`; commit: `2d8f000457da6447fa4df4bfec7365c1a49b6384`; acquired 2026-09-21. The 202-file working snapshot in `sources/lana_agents_iut/` matches the fresh immutable archive. Exact per-file hashes are in `sources/metadata/LANA_FILE_MANIFEST.csv`.

This is a **lexical source and local-import audit**. It is not Lean elaboration, theorem-specific kernel checking or an external-dependency axiom audit. No new Lean file was created. `LANA_STATIC_AUDIT.json` records `kernel_replayed: false`.

## Exact variant declaration

Module `Iut.Cor312.Statement`, namespace `Iut`, universes `u v`. The implicit parameters are `{AG : AnabelianGeometry.{u}} {TG : TemperedGeometry AG}`. The data bundle at lines 66–74 has fields `data : InitialThetaData AG TG`, `qPilot : QPilotData data`, and `rhsData : RHSData.{u,v} data`.

At `Iut/Cor312/Statement.lean:89–91`:

```lean
noncomputable def Corollary312Variant (X : Corollary312VariantData.{u, v} AG TG) :
    Prop :=
  X.qPilot.lhs ≤ X.rhsData.rhs
```

This defines a proposition. It does not prove it. The lemma `corollary312Variant_iff` at lines 95–97 has proof `Iff.rfl`: it unfolds the definition, without proving the inequality. No general bridge proof or project-level bridge axiom was found [C007].

## Specification boundaries

`Statement.lean:43–52` explicitly distinguishes the variant from published Corollary 3.12. The theta region is an input; its value is real under the recorded admissibility hypotheses, while the published construction permits an extended value. Correspondence of container/hull interfaces to IUT is documented but not itself a theorem.

`Iut/Cor312/RightHandSide.lean:61–91` packages the container, standard procession, finite/infinite-place compatibility, volume and hull. In particular:

- `thetaPilot` at line 83 is supplied data;
- `thetaPilot_hullAdmissible` at line 87 is supplied admissibility;
- `thetaPilot_le_shell` at line 91 is a supplied containment hypothesis.

`thetaHull` and `rhs` at lines 98–106 form the hull and its procession log-volume from these inputs. `HullSystem` (`HolomorphicHull.lean:112–136`) supplies its admissible class, hull-region class, hull and leastness/closure properties. This code does not implement the nine-step η algorithm to produce the source-faithful theta region [C007–C008].

Residual interfaces include `AnabelianGeometry`, `TemperedGeometry`, and the model's `EtalePi1Theory`/`TemperedPi1Theory`. They have typed fields; they must not be confused with global axioms or silently treated as constructions of the actual fundamental groups. The source README asserts source fidelity of its model parameters; this audit verifies the explicit parameters, not that assertion's full mathematical realization.

## Downstream implications and remaining arguments

At `Iut/Implication/Corollary23.lean:119–125`, with the file's ambient height formalism T and geometry parameters:

```lean
theorem cor312Variant_implies_abc {P : Corollary312VariantData.{u, v} AG TG → Prop}
    (A : T.ProofPackage) (I : ∀ (K : T.CBS) (d : ℕ), Corollary22Inputs T K d)
    (ex : ∀ K d, ThetaDataExistence P (I K d))
    (cheb : ChebyshevBound) (pnt : PrimeCountingBound)
    (h312 : ∀ X : Corollary312VariantData.{u, v} AG TG, P X → Corollary312Variant X) :
    ABC T :=
  T.statementII_implies_statementI A (statementII_of_cor312 I ex cheb pnt h312)
```

Thus the conditional implication has a source-code proof term. It does not introduce a global axiom for the bridge, and it does not remove `h312`. The unrestricted form at lines 128–134 also takes `h312`. The path includes `Theorem110Invariants.theorem110`, `Corollary22Inputs.c2` (`Corollary22.lean:384` onward), and `statementII_of_cor312` (`Corollary23.lean:56–112`). `ABC T` is the code's `T.StatementI` abstraction (`Iut/Abc/Target.lean`). The source does not thereby provide a theorem of actual IUT from the mere existence of this abstraction [C008].

| Source theorem | Exact locator at pinned commit | Boundary retained |
|---|---|---|
| `Iut.cor312Variant_implies_abc_concrete` | `Iut/Concrete/Main.lean:80–89` | Variant on concrete data; height proof package, suitable inputs/existence and bounds |
| `Iut.cor312Variant_implies_abc_curves` | `Iut/Concrete/Existence.lean:532–544` | Curve/provider assumptions and variant; see exact signature in snapshot |
| `Iut.Anabelian.cor312Variant_implies_abc_model` | `Iut/Anabelian/Existence.lean:584–597` | Etale/tempered theory parameters and remaining providers/h312 |
| `Iut.Tripod.abc_of_variant` | `Iut/Tripod/Main.lean:125–143` | Pi1, Tp, residual cyclic bound hcyc and concrete h312; concludes `tripodTheory.StatementII` |

The tripod theorem's exact hypotheses (with `Pi1 : EtalePi1Theory.{0}` and `Tp : TemperedPi1Theory Pi1` at lines 78–79) are:

```lean
    (hcyc : ∀ (K : CompactlyBounded) (d : ℕ),
      ∃ TK : ℝ, CyclicGraphBoundHyp (tripodProviders) K d TK)
    (h312 : ∀ (D : InitialThetaData (modelAG Pi1) (modelTG Pi1 Tp)) (LT : LocalTheory.{0, 0} D.Kt)
      (TL : ThetaLocalData D LT) (QI : QPilotInputs D),
      Corollary312Variant (concreteVariantData.{0, 0} D LT TL QI)) :
    tripodTheory.StatementII
```

Its proof invokes constructed curve/local/prime-counting data; it still requires these stated hypotheses [C027]. The generic and tripod targets must not be conflated. The README describes the additional role of the external genl proof package for Statement I; that package is not kernel-audited here.

## Complete local scan and inventories

`scripts/audit_lana.py` scans **all 172 Lean files**, masking comments and strings. Results [C025]:

- **10 `sorry` tokens**, all in `Comparator/Challenge.lean`, lines **27, 39, 48, 60, 67, 73, 93, 98, 103, 133**;
- **0 `axiom` keywords** and no additional `admit`/`sorryAx` tokens;
- **143 modules** in the local import closure of the six root modules listed in `LANA_STATIC_AUDIT.json`, including `Iut.Tripod.Main`;
- **0 placeholder/axiom tokens in that closure**;
- **2,385 lexical declaration records** and **50 structure/class records** in that closure.

`LANA_DECLARATION_INVENTORY.csv` gives module, file, line span, kind and commit for each lexically recognized declaration in the slice. `LANA_INTERFACE_INVENTORY.json` additionally retains the source text of structure/class declarations so fields can be reviewed. Short declaration names are not fully elaborated names; the line spans are lexical, not exact kernel dependency spans. These inventories cover the local imported sources, not every external declaration in Mathlib/genl/tate-curves-theta.

`lakefile.toml` uses `warn.sorry=false`, and defines separate challenge/solution libraries. Therefore a repository-wide claim of “sorry-free” would be false. Zero tokens in the selected closure is the narrower verified result. Actual theorem axiom closure is **UNKNOWN** until an exact build and `#print axioms` are performed [R_U10].

## External pins and README conflict

The pinned toolchain is `leanprover/lean4:v4.32.0`. `LANA_STATIC_AUDIT.json` retains the full `lake-manifest.json`, including mathlib v4.32.0 and its exact revision, tate-curves-theta `ca6c2279d3cea0690cdb01328e727118d5485d68`, and genl `6e9a6543b46a2a02fd7fe7ec8ab203d878f32859`. Those external working trees were not newly fetched or built in this run. The exact toolchain was not installed locally; no alternate-version replay is reported as equivalent.

**SOURCE FACT [C021]:** The `Statement.lean:32–37` docstring denies that any declaration assumes the variant and warns against adding it as a hypothesis. The downstream signatures above explicitly take `h312`. This documentation conflict is preserved. A conditional hypothesis is neither an unconditional bridge proof nor a hidden global axiom.

The README also explicitly says that the repository does not verify IUT and describes residual interfaces. We report the code's precise signatures where README prose is broader or older. No upstream failure theorem is inferred.
