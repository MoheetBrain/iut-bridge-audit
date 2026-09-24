# What the closed loop asserts

**Source claim, not an independently verified theorem of this audit:** on a single fixed abstract full prime-strip P, with its native codomain q-intertwining Q, the construction supplies the Θ-intertwining modulo the specified indeterminacies **while Q remains in force**.

In explicit logical notation,

\[
Q(P)\ \Longrightarrow\ Q(P)\wedge T_{\mathcal I_{\rm src}}(P)
\ \Longrightarrow\ T_{\mathcal I_{\rm src}}(P).
\]

This is a transcription of **IUT3 Remark 3.12.2(ii)(fitw), p.189**, read with **Remark 3.9.5(ix), pp.141–144**. Only the second implication is purely formal. The first names the substantive source construction. `T_I` is a shorthand for the source's intertwining with its specified indeterminacies, not a newly defined group orbit, existential predicate over arbitrary S, or formal Lean axiom.

## Candidate mathematical structure and exact boundary

The base object is an abstract full `F^(full-value,units)` prime-strip (the typography `F^{⊩▶×μ}` in the source), known up to isomorphism. Its presentations retain local Frobenioids/unit data, a global realified Frobenioid, the prime indexing and localization isomorphisms [IUT2 Definition 4.9(viii), p.158; IUT3 Definition 3.8, pp.112–113]. Q is its realization as the strip arising from the native q-pilot in the codomain arithmetic holomorphic structure. T is the corresponding domain Θ-pilot realization.

The candidate is a **diagram of structured presentations and relations**, rather than an ordinary category of regions with one endomorphism:

- The Θ-link supplies a full poly-isomorphism of the weakened full prime-strips. The loop traverses its inverse family from the native codomain side.
- sQ1/sQ2 induce the prime-strip poly-isomorphisms represented by Kummer detachment and Galois evaluation. The commutative diagram of Remark 3.10.2, pp.151–152, gives a specific compatibility witness here.
- sQ3 constructs hulls, normalized weighted determinant lines and tensor-power comparison objects. cQ3 retains the compatible Galois/unit actions in local upper categories and their local-global collections.
- The formal quotient is represented by the pair of categories described in cQ3, together with tensor-power twists. It is not replaced by a bare set of log-volumes.
- sQ4 uses the log-Kummer correspondence to adjust the vertical realizations in the codomain column. cQ4 preserves the appropriate Galois and unit comparison, with Frobenius-like units considered up to permitted log iterations.

Objects at intermediate stages are therefore different **types** of structured presentation. The ledger classifies elementary transitions, rather than falsely calling the region-to-hull step an isomorphism of regions. `CLOSED_LOOP_GRAPH.json` intentionally contains a source-asserted return edge. Its cycle is not a machine proof of closure.

The start is `(P,Q)` in the native codomain. The terminal presentation is the cQ3/cQ4 output whose formal quotient and vertical-adjustment diagram is asserted to represent `(P,Q,T_I)` over that same abstract strip. Its return condition is: the comparison preserves the full unit/value prime-strip data and local-global compatibility **in the codomain q-constrained structure**, subject only to the stated formal quotient indeterminacies. Bare isomorphism of abstract strips, equality of scalar values, or distinct labeled Q and T existing separately is insufficient.

## Not an ordinary composite identity

The whole loop is not asserted to be a literal identity on a field, a strictly commutative square of ring maps, or a single endomorphism whose value on every point can be calculated. It crosses poly-isomorphisms, reconstructions, category-pair quotients and log-link relations. The source describes closure **up to formal quotient indeterminacies**, with the simultaneous intertwining condition above.

This does not deny the genuinely commutative Kummer/evaluation diagram of Remark 3.10.2. That smaller diagram is explicitly called commutative; the upper semi-compatibility of Ind3 and the entire formal loop cannot be upgraded to such a diagram merely by analogy.

## sQ5 leaves the loop's structured level

Only after cQ3/cQ4 does sQ5 forget the local Galois and Frobenius-like unit portion [iQ5, pp.142–143]. The loop is claimed to permit the scalar consequence

\[
a_q=-|\log(q)|\ \in\ \operatorname{OutVol}_{\Theta}
=\mathbb R_{\le -|\log(\Theta)|},
\]

with the normalization and output interpretation of Corollary 3.12(xi-d)–(xi-f), pp.183–184. This is not a derivation performed here. The exact descent from simultaneous intertwining to that scalar membership remains the principal original-source interface to check. LANA's exact suitable-S equality is a further crosswalk problem.

The full categorical quotient/descent model and all its dependencies have not been recursively reconstructed. Consequently closure is **precisely identified as a source claim**, but not upgraded to `PROVED_BY_AUDIT`. See [CLOSED_LOOP_LEDGER.csv](CLOSED_LOOP_LEDGER.csv), [SQ5_FORGETFULNESS.md](SQ5_FORGETFULNESS.md) and the [Stage 3.5 gate](../../STAGE_3_5_GATE.md).
