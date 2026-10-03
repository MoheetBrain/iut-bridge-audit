# cQ3: a category pair with a derived forgetful functor

The source explicitly specifies a **pair of categories**. Its object and morphism records also determine a genuine forgetful functor. This latter statement follows from the records; it does not identify that functor with a universal quotient or assert essential surjectivity.

Source: [IUT III](../../sources/primary/IUT_III.pdf), Remark 3.9.5(ix), cQ3, pp.141–142. Linear means Frobenius degree one: [Frobenioids I](../../sources/primary/Frobenioids_I.pdf), Definition 1.2(i), p.21. We use the bounded, admissible, fixed-presentation setting of [E3d](../06_e3d/E3D_TYPED_DIAGRAM.md). No assertion that the union of every possible IPL output is bounded is added.

## Fixed input and ambient category

Fix the native column, a permitted tensor/root presentation and a positive integer M clearing the determinant conventions of Ob3–5. Write H_B=φ(P_B) and D_B,v=det^(⊗M)(H_B,v), including the structural-lattice correction and component weights. These are objects in the specified local Frobenioids, not raw exterior powers of arbitrary regions.

At each place v let C_v be the local Frobenioid, R_v its realification, and r_v:C_v→R_v the realification functor. Let C_g be the global realified Frobenioid and loc_v:C_g→R_v its localization, with the prime labels fixed. These symbols include the given local/global comparison identifications. The localization constructions are those recalled by cQ3 from [Frobenioids II](../../sources/primary/Frobenioids_II.pdf), Example 5.6(iii),(iv), pp.63–65: restriction to completions, with the stipulated divisor and coefficient hypotheses. We use the given prime-strip data, not a reconstruction of arbitrary local data into a global Frobenioid.

An object of C_q is the record

`Y = ((Y_v ∈ C_v)_v, Y_g ∈ C_g, (ρ_Y,v : r_v(Y_v) ≅ loc_v(Y_g))_v)`.

A morphism f:Y→Z is `((f_v:Y_v→Z_v)_v, f_g:Y_g→Z_g)` satisfying, for every v,

`loc_v(f_g) ∘ ρ_Y,v = ρ_Z,v ∘ r_v(f_v)`.                         (1)

Identities and composition are componentwise. Objects and arrows remain in the source's local/global categories and admissible collections. At archimedean places retain the stipulated torsion-quotient system and its compatible components; do not replace it by a chosen complex representative. The formulas here apply at a fixed Frobenioid presentation. Changing torsion/root presentations is a separate system-level question.

## Upper category and forgetful operation

A local upper object is `(X_v,[a_v])`, where

`a_v:X_v→D_B,v`, `deg_Fr(a_v)=1`, ` [a_v]=Aut(D_B,v)·a_v`

and the action is **postcomposition**. A local arrow f_v:(X_v,[a_v])→(Z_v,[b_v]) is an arrow of C_v satisfying

`[b_v ∘ f_v]=[a_v]`.                                           (2)

Thus C_B has objects `((X_v,[a_v])_v,X_g,(ρ_X,v)_v)` and morphisms satisfying both (1) and (2). This is cQ3's unrestricted upper category. The optional restriction to objects arising from hull-approximants on p.141 is a different subcategory; statements below about all fibers do not silently transfer to that restriction.

Define `U_B:C_B→C_q` by deleting only the orbits [a_v] and leaving every arrow component unchanged. Identities satisfy (2). For f:X→Z and g:Z→W,

`[c_v g_v f_v]=[b_v f_v]=[a_v]`.

Equation (1) is also closed under composition. Hence U_B is a functor, and is faithful. It is not thereby full, essentially surjective, or a categorical quotient. It forgets the **structure poly-morphisms**, not all of the native q-marking; that marking was never included in the definition of every C_B object.

## Exact category-of-elements description

Let C_q^loc-lin be the wide subcategory of C_q whose arrows have deg_Fr(f_v)=1 at every v. Degree is multiplicative (FrI Remark 1.1.1, p.21); automorphisms have degree one. Equation (2) therefore forces every C_B arrow to be locally linear. No assertion about the independent global degree is needed.

For this base define the set-valued presheaf

`T_B(Y) = ∏_v (Aut(D_B,v) \ Hom_lin,C_v(Y_v,D_B,v))`,

`T_B(f)(([b_v])_v) = ([b_v f_v])_v`.

Composition of linear arrows is linear. Changing b_v within its postcomposition orbit does not change [b_v f_v]. Associativity gives the presheaf law. An object of its category of elements is precisely `(Y,a)` with a∈T_B(Y); an arrow f:(Y,a)→(Z,b) satisfies T_B(f)(b)=a, exactly (2). Thus, at this fixed presentation,

`C_B ≅ ∫ T_B`, and `U_B : ∫ T_B → C_q^loc-lin ↪ C_q`.

This is a proved identification of records, not an imported model. Over C_q^loc-lin the projection is a **discrete Grothendieck fibration**: for f:Y→Z and (Z,b), its unique lift has domain (Y,T_B(f)b). The global object and all localization squares are already supplied by Y. This construction does not glue a new global object from independent local inputs. See [the categorical cross-check](CATEGORICAL_CROSSCHECK.md).

This calculation concerns the fixed local Frobenioid categories. It asserts neither that taking automorphism orbits commutes with limits of torsion systems nor that one archimedean level replaces the full source system. Compatibility between presentations must still be retained separately.

The same argument does not give a fibration over all of C_q. An arrow of higher local Frobenius degree cannot lift into C_B by (2). We neither assume such an arrow exists into every particular collection nor extend the fibration claim beyond its proved base.

## Ordinary essential image and fixed diagrams

For Y∈C_q, the strict fiber is the discrete category with object set T_B(Y). Its nonemptiness is the exact ordinary lifting criterion. The iso-comma test `(X,η:U_B(X)≅Y)` is equivalent to this strict fiber: transfer [a_v] to `[a_v η_v^−1]` on Y; (1) transfers the local/global tuple. This does not assert T_B(Y) is nonempty or that an arbitrary lift arose from IPL.

For every specified small category J, postcomposition defines

`Fun(J,U_B):Fun(J,C_B)→Fun(J,C_q)`.

For a specified Y:J→C_q^loc-lin, strict lifts are exactly families

`a_j∈T_B(Y(j))` for every j, with `T_B(Y(α))(a_j)=a_i`

for every α:i→j. Equivalently they form `lim_(J^op)(T_B∘Y^op)`. Proof: these equations make the prescribed arrows Y(α) arrows of C_B; identities and composition then follow from those of Y and faithfulness of U_B. Conversely every lift satisfies the equations. No limiting object in C_B and no descent-effectivity theorem is needed for this **unevaluated diagram**. Pointwise nonempty fibers alone do not supply a compatible family.

This lemma works without cofilteredness. It does not yet identify the source's actual formal output with such a specified J-diagram; that is the boundary in [FORMAL_SYSTEM_TYPE.md](FORMAL_SYSTEM_TYPE.md).
