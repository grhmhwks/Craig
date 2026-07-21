# Response to the NRCM accuracy report

We thank the reviewer for the careful reading and for distinguishing the truth of the deficit-preservation statement from the completeness of the proof presently given. We have checked the objections against the definitions and the proof. Our assessment is that the singleton-suffix objection and the endpoint-cancellation objection are valid. The indexing comment in the shifted-window lemma is also fair, but minor. The comments about examples and unused explanatory material are editorial and do not affect correctness.

No claim in this response relies on the reported computations as a substitute for proof.

## 1. The one-column suffix

**Assessment: valid.**

The reviewer is correct that the definition permits the selected suffix to be the singleton
\[
K=I_{s-1}=\{s-1\}.
\]
For this suffix, the definition of \(T_{s-1}\) sends the sole value around its one-element cycle and adds \(1\). On the other hand, the proof defines
\[
\epsilon(a,c)={\bf 1}_{L_c<L_a},
\]
so that \(\epsilon(a,a)=0\). Consequently, the formula
\[
Q_a+\epsilon(a,\operatorname{succ}_K(a))
\]
does not describe the transported value when \(|K|=1\). The same defect propagates to the later lifted-arc and transported-target formulas that use this expression.

The example in the report is a genuine example in the domain of the theorem. For
\[
r=7,\qquad s=5,\qquad Q=(0,1,2,4,4),
\]
we have \(H=(0,1,2,4,5)\) and \(P=(0,0,0,0,1)\), so \(Q\) is valid. The candidates beginning at \(k=1,2,3\) fail capacity, while the singleton candidate beginning at \(k=4\) is valid and gives
\[
Q'=(0,1,2,4,5).
\]
Thus this is not merely a convention at an unreachable boundary case.

**Planned correction.** We will separate the singleton case at the start of the proof. For \(|K|\ge 2\), the existing strict label-wrap indicator correctly records the unique wrap in the suffix cycle. For \(|K|=1\), we will prove deficit preservation directly, using the fact that the sole coordinate is increased by \(1\), the validity of both paths, and the capacity failure of the preceding suffix. This is preferable to silently changing the global definition of \(\epsilon\), since that indicator is also used for ordinary comparisons between labels and those uses should retain their present meaning. We will also state explicitly that all later transport formulas are being used only in the nonsingleton case.

This correction repairs false intermediate formulas; the report does not give, and we do not find here, a counterexample to deficit preservation itself.

## 2. Endpoint cancellation in the boundary and suffix block

**Assessment: valid and substantive.**

The passage from the cocycle identity to the claimed level-set boundary description is not presently proved. The cocycle identity identifies when a transported label arc crosses a cut, but it does not by itself establish that the reduced endpoints constructed from the sets \(L_X(t,e)\) and \(U_X(t,e+1;e)\) are exactly the two signed boundaries of maximal occupied components.

In particular, the current application does not explicitly prove all of the following facts:

1. every surviving token in \(\partial B\) is an endpoint of the asserted occupied set at its stated source and level;
2. every interior component has two endpoints, with opposite signs and matching source/multiplicity data;
3. the physical ends of the visible list introduce no additional unmatched endpoints;
4. every token left unmatched by visible pairing is represented at a particular omitted cut; and
5. the levels available at that omitted cut are exactly the positive integers satisfying \(1\le \lambda\le \mu_h+1\).

The abstract level-set lemma is correct under its hypotheses, but the present proof effectively asserts rather than derives those hypotheses for the actual token multiset. Similarly, the phrase "hidden stack" conveys the intended picture but is not yet a defined object tied to those tokens. The reviewer is therefore right that this is a gap in the proof rather than only a request for more exposition.

**Planned correction.** We will replace the informal part of Steps 4 and 5 with an explicit pairing lemma tailored to the token multiset in Step 2. A token will retain its state, sign, transported source, target, physical edge, lower/upper family, integer height, and local level. The revised argument will:

- define the occupied \(\lambda\)-cells directly from the inequalities defining \(L_X\) and \(U_X\);
- verify, cut by cut, that the lower and upper families give the two oppositely signed changes of occupancy, including the half-open endpoint conventions;
- construct the pairing (equivalently, a sign-reversing involution) within every maximal visible component while preserving source and multiplicity labels;
- handle the two physical ends of the visible edge strip explicitly; and
- define the hidden cells at each omitted cut and prove algebraically that their possible local levels are precisely \(1,\ldots,\mu_h+1\) when \(\mu_h\ge0\), and none when \(\mu_h<0\).

The omitted-edge overflow lemma then gives \(\mu_h<0\) at every omitted column, eliminating all possible hidden partners and forcing complete visible cancellation. Until this token-level lemma is supplied, we agree that the displayed boundary/suffix identity should not be regarded as established by the current draft.

## 3. Shifted suffix-window indexing and terminology

**Assessment: partly valid, but minor.**

The final paragraph of "Shifted suffix-window facts" compresses a cyclic-rotation argument into the statement that \(\alpha_i\) lies on the wrapped side of the shifted cut. The preceding inequalities strongly indicate the intended conclusion, and the reviewer does not identify a counterexample, but one more explicit indexing argument is warranted.

**Planned correction.** We will write the shifted cyclic order explicitly, identify \(\alpha_i\) as the predecessor of its shifted minimum in that order, and derive
\[
L_i+R(\alpha_i+b-i)\ge s
\]
before concluding \(L_{\alpha_i}<L_i\). This is a local clarification, not a change in the proof strategy.

The related concern about "adjacent to a deleted endpoint," "occupied cell," and "visible component" is valid in the present boundary/suffix application because those notions carry logical weight there. They will be replaced by precise definitions in the explicit pairing lemma described above. We do not think that every informal geometric phrase elsewhere in the exposition requires separate formalization; only the terms on which the cancellation inference depends do.

## 4. Computational evidence

**Assessment: useful corroboration, but not part of the proof.**

We appreciate the extensive testing and the absence of a counterexample to deficit preservation. We agree with the reviewer that these checks neither repair the singleton formulas nor discharge the endpoint-pairing obligation. The revised proof will be self-contained and will not cite finite testing as justification for either point.

## 5. Allegedly unnecessary material

**Assessment: editorial, and only partly calls for a change.**

The observation that examples and diagrams are not logically necessary is true in the ordinary sense that examples are not premises in the proof. It is not, however, an objection to this document, whose stated purpose is to give a readable proof. The numerical examples and diagrams help distinguish physical order from label order and make the suffix and endpoint mechanisms easier to follow. We therefore plan to retain representative examples and diagrams, subject to ordinary shortening if the repaired proof becomes too long.

The "Label-order endpoint cancellation" lemma is not directly invoked in the current proof and overlaps the later level-set lemma. We agree that leaving two near-duplicate abstract lemmas obscures the dependency chain. In revision, we will remove it or absorb its useful content into the new explicit token-pairing lemma. This is streamlining, not a correction to the theorem.

The longer suffix-geometry chain is used in deriving omitted-edge overflow. The report itself recognizes this. We do not plan to replace that chain unless a genuinely shorter proof of the same implication is available.

## Conclusion

We agree with the report's central conclusion in the following precise sense: the present draft contains a genuine singleton-case error in its transport formulas and a genuine gap in its main endpoint-cancellation argument, so it is not yet a complete proof as written. We will repair the former by a separate singleton argument and the latter by an explicit, source- and level-preserving token pairing with a proved omitted-cut bound. We will also expand the one compressed shifted-order step and consolidate the redundant abstract cancellation material. We do not regard the presence of explanatory examples and diagrams as a defect, and we plan to retain them where they serve the stated readability goal.
