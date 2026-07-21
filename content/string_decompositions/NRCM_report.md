# Accuracy Report: Readable NRCM Proof

## Verdict

The theorem appears to be true, and extensive finite testing supports it. However, this document does **not yet constitute a complete proof of the theorem as stated**.

I found:

- one concrete family of false equations when the selected suffix has one column;
- a substantive gap in the central endpoint-cancellation argument;
- several smaller exposition-level omissions;
- no computational counterexample to deficit preservation itself.

## 1. False statements: the one-column suffix case

The definition allows \(k=s-1\), so \(K=I_k=\{s-1\}\) may contain one column. In that case, the definition of \(T_k\) increments the single value by \(1\); see `naive_rational_cyclic_map_readable.tex`, lines 165–170.

But the proof defines
\[
\epsilon(a,c)=\mathbf1_{L_c<L_a}.
\]
Consequently, when \(\operatorname{succ}_K(a)=a\),
\[
\epsilon(a,a)=0,
\]
even though the singleton cyclic move is precisely the wrap and must add \(1\).

Thus the following assertion is false for singleton \(K\):
\[
Q_a+\epsilon(a,\operatorname{succ}_K(a))
\]
is the value transported from \(a\); see `naive_rational_cyclic_map_readable.tex`, lines 325–335.

The same error reappears in:

- the threshold-crossing transport formula and lifted interval, lines 900–914;
- the boundary/suffix definition of \(M_t^+\), lines 1141–1146.

A concrete allowed example is
\[
r=7,\quad s=5,\quad
Q=(0,1,2,4,4),\quad k=4,\quad K=\{4\}.
\]
Here the NRCM is defined and produces
\[
Q'=(0,1,2,4,5).
\]
But \(L_4=3\), so \(\epsilon(4,4)=0\). The proof’s formula predicts \(Q'_4=Q_4=4\), whereas the definition gives \(Q'_4=Q_4+1=5\).

This is not a counterexample to deficit preservation; it is a counterexample to formulas used in the proof. A separate singleton-suffix argument, or a cycle-dependent wrap indicator with \(\epsilon_K(a,a)=1\), is required.

## 2. Main proof hole: endpoint cancellation

Even after excluding singleton suffixes, the proof of “Boundary and suffix cancellation” is incomplete.

The crucial leap occurs at `naive_rational_cyclic_map_readable.tex`, lines 1265–1300. The cocycle identity explains when a threshold changes as a label crosses a lifted arc. The proof then asserts that the reduced tokens at each level are exactly the signed boundaries of visible occupied components.

That conclusion is not derived. In particular, the document does not construct the purported occupied level set and prove that:

1. every reduced token is one of its component endpoints;
2. every interior component has precisely two endpoints with opposite signs;
3. no endpoint can occur at the extreme physical boundaries;
4. cancellation respects the transported-source and multiplicity labels.

The “Level-set endpoint cancellation” lemma assumes essentially these properties in its hypotheses, so invoking it does not establish that the actual token collection has them.

The next step, lines 1325–1339, similarly asserts without a full derivation that every unpaired endpoint must be adjacent to an omitted cut and must satisfy
\[
1\le\lambda\le\mu_h+1.
\]
The “hidden stack” used to justify this bound is not formally connected to the previously defined endpoint families.

This is a substantive hole because the final theorem depends directly on this cancellation lemma at lines 1390–1392.

Notably, `red_team_nrct_endpoint_obligations.py` describes level pairing and the omitted-cut bound as “remaining proof obligations” and explicitly says its tests are not proofs.

## 3. Smaller omissions

The final step of “Shifted suffix-window facts” says that \(\alpha_i\) lies on the wrapped side of the shifted cut, lines 653–667. This is probably correct, but the cyclic-rotation indexing needed to prove it is only implicit.

Several endpoint terms—“adjacent to a deleted endpoint,” “occupied cell,” and “visible component”—also lack definitions precise enough to support a unique formal pairing.

These are repairable; they are less serious than the singleton error and main endpoint gap.

## 4. Computational evidence

I reran the project’s theorem, threshold, overflow, moving-block, endpoint-pairing, and leak-bound checks on 7,171 path-valid NRCM moves across slopes both above and below \(1\):
\[
7/5,\ 10/7,\ 13/8,\ 2/3,\ 3/4,\ 3/5,\ 4/7,\ 5/8,\ 7/10.
\]

Every theorem-relevant check passed. This is strong evidence that the theorem and intended combinatorial identities are correct, but it cannot replace the missing general argument.

## 5. Unnecessary material

Most formal lemmas are used somewhere in the current proof chain. The clear exceptions are:

- “Label-order endpoint cancellation,” line 1072, which is not directly invoked and largely duplicates later cancellation discussion;
- all numerical examples and diagrams, which are explanatory rather than logically necessary.

The long suffix-geometry chain is necessary for this proof’s derivation of omitted-edge overflow, although a more direct proof might replace it.

Overall: the result is very likely correct, but the readable document needs a singleton-suffix repair and a genuinely explicit endpoint-pairing/leak argument before it establishes the theorem.
