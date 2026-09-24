# B2: actual scalarization machinery

**STATUS: PARTIAL.** The normalized-volume calculus has independent earlier support. Its application to the still-incomplete Rel_pre predicate is not yet a theorem. The status is not “arbitrary forgetting map”, and it is not “PROVED-CONDITIONAL-ON-B1” with hidden admissibility assumptions.

[LOG_VOLUME_PRESERVATION.csv](LOG_VOLUME_PRESERVATION.csv) records fifteen operations. The essential reconstruction is as follows.

At a finite place, normalize additive Haar volume by `mu(O_k)=1`. For residue cardinality `p^f`, `log mu(m_k^n)=-fn log p`; AT3 Prop5.7(i), pp.137–139, proves the translation/scaling and injective-log-patch equalities. At an archimedean place the relevant measure is radial/angular, not arbitrary planar area; the angular unit circle has length 2π (AT3 Prop5.7(ii)).

IUT3 Prop3.9(i), pp.115–116, uses the specified weighted direct summands of tensor packets and normalizes multiplication by p to add `-log p`; multiplication by e adds 1 in the archimedean packet normalization. Procession normalization averages the packet values with equal capsule weights. Rmk3.9.3, pp.119–120, explains compatibility with inclusion of the same log-shell in different capsules. It does not permit a freely chosen set of weights.

Prop3.9(iii), p.117, sums global families with all but finitely many zero contributions and relates the result to global arithmetic degree. Rmk3.9.6, p.145, transports product-formula conversion ratios using log compatibility on sufficiently small regions; it does not assert preservation for arbitrary regions under a logarithm.

Rmk3.9.4(i), pp.120–122, defines Fn(M) from nonnegative finite-valued Borel functions with relatively compact support. Integration is a surjection onto R>=0. Rss(M) is its equal-integral quotient and is isomorphic to R>=0 as a monoid with positive scaling action. Taking a logarithm and the specified positive normalization gives the logarithmic coordinate; the zero class corresponds to -infinity. This coordinate operation is not simply groupification of Rss.

Parts (iii) and (vi), pp.122–126, construct compatible Rss isomorphisms using ample patches on which log, or the archimedean exponential comparison, is injective. For tensors (v), the degree exponents are `d_A=product_alpha [k_alpha:Q_p]` and `d_alpha=product_{beta != alpha}[k_beta:Q_p]`; comparison through Rss(Q_p) makes the result independent of the chosen factor. The packet weights and degree normalization must still be applied.

Part (iv), pp.123–124, retains the native `O_k^× × q^N` splitting through the unit logarithmic sequence: the q generator is assigned `-ord_v(q_under) log p_v` (the source's local `-log q`). This is a fixed native coordinate with its root convention. Global/procession evaluation yields the q scalar in xi-d; it is not a license to independently rescale either final real line.

Hull formation gives **inclusion** and an upper volume bound, usually not equality. Individual Xi(P) hull-approximants, if they exist, have the same volume as P. Their union may have strictly larger volume (Rmk3.9.5(iv), p.129). Local Xi nonemptiness is qualified; the stated global analogue is nonempty. The weighted determinant corrects by the inverse determinant of the structure sheaf and accounts for its positive tensor power M. Arithmetic degree agrees with the original normalized volume only after these corrections (Ob3–4, pp.131–134).

Ob9, pp.138–139, states a **natural bijection of hull log-volumes** across the log-link. Ob9-1 says that once comparable determinant/hull objects have been obtained, power twists, upper-formalism and log iterates become compatibility requirements with no effect on their comparability. This is stronger than an unspecified forgetful operation. It is weaker than asserting an objectwise bijection of all raw output regions. iQ5 still forgets local Galois and Frobenius-like unit data.

Rmk3.9.7(ii)–(iii), pp.146–147, extends volume by infima over dominating finite-volume regions, or formal inverse systems; -infinity is possible. Xi-d, p.183, then declares the possible-output downset `OutVol_src(O)=R_{<=b}`, with `b=-|log Theta|` the output hull log-volume. The scalar `a_q=-|log q|` is independently defined there. This audit records that printed range; it does not identify it with the attained image of a set of LANA suitable-S choices.

Conditional application is straightforward **after the right relation is supplied**: a certified inclusion in the same normalized realization gives a volume inequality; a specified compatible formal approximation must give the corresponding bound/limit. For example, if source admissibility yields values `t_eps <= b` with `a_q-eps <= t_eps` for every eps>0, then `a_q<=b`. That condition is sufficient and target-equivalent at scalar level, not a newly discovered source premise. A fully instantiated structured relation making these laws applicable is precisely what remains open in B1/B2.
