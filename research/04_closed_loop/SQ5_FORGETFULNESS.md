# sQ5 and the xi-e → xi-f interface

**sQ5 is qualitatively different from cQ3/cQ4.** IUT3 Remark 3.9.5(ix)(iQ5), pp.142–143, expressly says that passage to log-volumes forgets the local Galois groups and Frobenius-like units. Before it, those structures are part of the compatibility with the codomain arithmetic holomorphic structure. Afterwards a real scalar does not reconstruct them.

## A typed evaluation where it is supplied

For an actual realized arithmetic hull/line object with the prescribed component weights, structural-sheaf normalization, tensor power M and compatible local-global data, define the **audit notation**

`ev_norm : realized normalized determinant data -> R`

by the normalized arithmetic degree described in Ob3, pp.131–133 and Proposition 3.9, pp.115–117. This notation packages a source evaluation; it is not a definition on every formal quotient class. On positive finite-measure local regions it can be written as the positive prescribed normalization of `log(integral characteristic_function)`. Zero measure requires `-infinity`; unbounded/general region classes require a separate domain restriction and cannot silently be assigned finite real values.

The local semisimplification in Remark 3.9.4(i), pp.120–122, is explicit:

`Fn(M) -> Rss_mu(M)=Fn(M)/(equal integral) -> R_{>=0}`.

The last map is an isomorphism of additive monoids with positive scalar action. Groupification gives an ordered real line. Taking the **logarithm** of positive integral is a different coordinate operation; it is not additive for the original Fn addition. The distinctions matter when comparing LANA's pointed real-line notation.

## Why the whole formal quotient is not a scalar equality quotient

The set upper formalism collapses everything in a selected proper hull. Distinct smaller hulls can have different volumes [Remark 3.9.5(iii)–(vi), pp.128–130]. Their union may also have larger volume than an individual equal-volume approximant [iv, Ob6]. Consequently the instruction “apply ev_norm to the collapsed point” does not define a single scalar by ordinary quotient descent.

The source instead keeps the upper-category/formal presentation and uses hull bounds and possible output values. Its scalar description at xi-d is the downward region `R_{<=-|log(Theta)|}`. The audit therefore distinguishes:

- Numerical evaluation of a **realized** normalized object.
- The **set/order interpretation** of a family and its hull bound.
- Semisimplified log-link transports that preserve designated numerical evaluations.

Ob9, pp.138–139, claims that tensor twists, the upper formalism and arbitrary log iterates function as compatibility conditions for coarse invariants after comparability has been obtained. This must not be weakened to arbitrary quotienting or strengthened to constancy on all underlying collapsed hulls.

## Exact interface to be verified

Let D denote the source initial/log-theta data, Q its native q constraint, and O the **actual source output presentation**, retaining the cQ3/cQ4 data. Write `CL_src(D,Q,O)` for the source's simultaneous-intertwining condition from the closed loop; this is currently only a partially expanded predicate. Let `OutVol_src(O)` denote the output scalar downset of xi-d with its prescribed normalization. The isolated checking obligation is:

\[
\mathrm{CL}_{\rm src}(D,Q,O)
\quad\Longrightarrow\quad
\mathrm{ev}_{\rm native}(Q)\in\mathrm{OutVol}_{\rm src}(O).
\]

Its intended native value is `-abs(log(q))`. **This implication is asserted by the source**, especially xi-e–f and Remark 3.12.2(ii)(fitw); it is not a newly proposed missing axiom or a proof supplied by this audit. To verify it independently, the formal quotient compatibility must be expanded enough to show that Q's constrained realization remains represented by the source output's scalar interpretation, including any approximation allowed at xi-f. An attained representative S with exact η equality is stronger than what this membership sentence alone supplies.

The smallest unresolved interface identified here is thus the descent of the simultaneous q condition to the normalized output downset. “Smallest” means the narrowest interface isolated in this audit; logical minimality among all possible IUT propositions is not established. See [PRE_POST_LOG_VOLUME.csv](PRE_POST_LOG_VOLUME.csv).
