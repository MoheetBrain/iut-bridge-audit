# W*: stop before asserting a source-native lifting type

**W* is not yet well-typed in the recovered source formalism.** This follows from the Section 5 stop in [FORMAL_SYSTEM_TYPE.md](FORMAL_SYSTEM_TYPE.md), before native Q can be represented as Q_sys. Consequently there is no source-justified list of full W* quantifiers or compatibility equations to report. Writing such a list using undefined FormalSys objects would conceal the present result.

| Required part of a W* statement | State at this stop |
|---|---|
| Quantified output system X_sys | IPL's strip path and the stated multiradial data are available; their formal cQ3 diagram presentation, including arrows, is unresolved. No arbitrary C_B object is substituted for actual IPL provenance. |
| Source category FormalSys_B | Unresolved; fixed C_B and raw region records are explicitly typed. |
| Target category FormalSys_q | Unresolved; fixed C_q and native q_M are explicitly typed. |
| System operation U_B^sys | Generic postcomposition is proved for each specified J. Its source-specific domain and permitted comparisons are unresolved. |
| Native target Q_sys | Unresolved; the complete retained native fields are in [Q_SYSTEM.md](Q_SYSTEM.md). |
| Comparison relation | Equality, poly-isomorphism, refinement, inclusion/surjection, and formal quotient have not been shown interchangeable. None is chosen merely to make the statement type-check. |
| Permitted indeterminacies | Ob4-3 tensor-power twists, Ob5's formal collapse, and Ob8 log iterates are named by Ob9-1, pp.138–139. Their action/comparison rules on the required whole diagram remain to be recovered. Ind3 is not a group action. |
| Compatibility equations | Equations (1),(2) of [CQ3_FUNCTOR_OR_PAIR.md](CQ3_FUNCTOR_OR_PAIR.md) are established within a fixed presentation. No equation identifying returned IPL splitting with native s_q is yet justified through the system. |

## Two fully typed auxiliary tests, explicitly not W*

**Exact-object test.** With Q,B,M and the fixed presentation as in E3d, ask for

`X∈Ob(C_B), η:U_B(X)≅q_M in C_q`.

For every v its equations are `[a_Z,v f_v]=[a_X,v]` for upper arrows and, for η,

`loc_v(η_g) ρ_X,v = ρ_qM,v r_v(η_v)`.

The iso-comma morphisms h:(X,η)→(X',η') satisfy `η' U_B(h)=η`. This is equivalent to choosing an element of T_B(q_M), by the proof in the companion file. It is not imposed: it can require exact attainment, and even a solution need not carry the IPL pilot provenance or the full native marking.

**Fixed-diagram test.** For every specified small J and Y:J→C_q^loc-lin, an ordinary strict lift is exactly

`∀j∈Ob(J), ∀v, [a_j,v]∈Aut(D_B,v)\Hom_lin(Y(j)_v,D_B,v)`

subject to

`∀(α:i→j), ∀v, [a_j,v Y(α)_v]=[a_i,v]`.

The given Y already contains its global objects, localization isomorphisms and commuting localization squares. This is a real conditional mathematical statement, proved by explicit construction, but neither Y nor the identity comparison with a native Q_sys has been recovered for the actual output. No further limit-attainment condition is inserted.

## Over-strength check

Source approximation is weaker than demanding an attained exact hull-approximant; formal intersections can be retained unevaluated. Thus an exact object, a canonical representative, a universal quotient and effective gluing into a single arithmetic object are not necessary assumptions here. E3d already declined to impose the exact-object test. Removing it therefore does not prove the verdict PREVIOUS_WSTAR_REQUIREMENT_TOO_STRONG or construct a weaker W*. The unresolved issue is the source-derived comparison type itself.

Locators: III Remark 3.9.5(v),(vi), pp.129–130; Ob4–9, pp.133–139; cQ3/cQ4, pp.141–142; Remark 3.9.7(ii),(iii), pp.146–147. The target language in Remark 3.12.2(ii), pp.187–189, is not an inference rule.
