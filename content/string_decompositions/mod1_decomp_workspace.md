# Working notes for `mod1_decomp.tex`

## Finite checks

Checked 2026-07-19 using the definitions and routines in `code.py`.  For every
parameter pair below, the check exhaustively enumerated normalized
step-\(\tau\) Dyck words \(D\) satisfying

\[
 0\le \defc_\tau(D)\le (s-2)\tau-1,
 \qquad
 \area(D)\le
 \left\lfloor\frac{\tau\binom{s}{2}-\defc_\tau(D)}2\right\rfloor-1.
\]

The three UP checks were:

1. validity of the injection in the full-skeleton branch;
2. existence of an extractable occurrence outside the final position;
3. after East3 failure, existence of an extractable occurrence outside the
   final two positions of the current prefix.

| tau | s | eligible words | UP 1 tested/fail | UP 2 tested/fail | UP 3 tested/fail |
|---:|---:|---:|---:|---:|---:|
| 2 | 5 | 90 | 16 / 0 | 74 / 0 | 1 / 0 |
| 2 | 6 | 343 | 38 / 0 | 305 / 0 | 4 / 0 |
| 2 | 7 | 1,118 | 83 / 0 | 1,035 / 0 | 13 / 0 |
| 2 | 8 | 3,205 | 169 / 0 | 3,036 / 0 | 30 / 0 |
| 2 | 9 | 8,360 | 328 / 0 | 8,032 / 0 | 60 / 0 |
| 3 | 5 | 336 | 41 / 0 | 295 / 0 | 5 / 0 |
| 3 | 6 | 1,610 | 121 / 0 | 1,489 / 0 | 18 / 0 |
| 3 | 7 | 6,470 | 324 / 0 | 6,146 / 0 | 50 / 0 |
| 3 | 8 | 22,531 | 797 / 0 | 21,734 / 0 | 122 / 0 |
| 4 | 5 | 883 | 83 / 0 | 800 / 0 | 11 / 0 |
| 4 | 6 | 5,161 | 295 / 0 | 4,866 / 0 | 46 / 0 |
| 4 | 7 | 24,712 | 933 / 0 | 23,779 / 0 | 142 / 0 |
| 5 | 5 | 1,938 | 147 / 0 | 1,791 / 0 | 26 / 0 |
| 5 | 6 | 13,254 | 609 / 0 | 12,645 / 0 | 105 / 0 |
| 5 | 7 | 73,416 | 2,225 / 0 | 71,191 / 0 | 337 / 0 |
| **Total** |  | **163,427** | **6,209 / 0** | **157,218 / 0** | **970 / 0** |

The original UP 3 statement with \(s=5\) is nevertheless false for large
\(\tau\); its counterexample is recorded below.  After correcting UP 3 to
\(s\ge6\), exhaustive searches found no counterexample for \(s=6\),
\(2\le\tau\le10\), or for \(s=7\), \(2\le\tau\le8\).  Random searches of
\(100{,}000\) normalized candidates for \(s=6\) at each

\[
 \tau\in\{11,15,20,30,50,75,100,150,200,300,500,1000\}
\]

also found none.

The auxiliary bounds in the DOWN proofs were exhaustively audited on all
normalized words for

\[
 (\tau,s)\in
 \{(2,5),(2,6),(2,7),(3,5),(3,6),(4,5)\}.
\]

There were no failures of the skeleton-append bound, the double-zero
terminal-gap bound, or the rapid-chain midpoint bound.  All finite checks are
evidence only.

## Common hypotheses and notation

Fix \(\tau\ge2\), \(s\ge5\), and set

\[
 M_s=\tau\binom{s}{2},
 \qquad
 L_d=\left\lfloor\frac{M_s-d}{2}\right\rfloor.
\]

For nonnegative integers \(u,v\), write

\[
 d_\tau(u,v)=
 \begin{cases}
  (u+\tau-v)_+,&u\le v,\\
  (v+\tau+1-u)_+,&u>v,
 \end{cases}
\]

and put

\[
 K_\tau(u,v)=\tau-d_\tau(u,v)
 =
 \begin{cases}
  \min(\tau,v-u),&u\le v,\\
  \min(\tau,u-v-1),&u>v.
 \end{cases}
\]

For a word \(X=(x_0,\ldots,x_{N-1})\), define

\[
 \lambda_j(X)=\sum_{i<j}K_\tau(x_i,x_j)-x_j.
\]

Then

\[
 \defc_\tau(X)=\sum_j\lambda_j(X).
 \tag{1}
\]

The six proofs use the following five principles.

## Principle I: record payment

Let

\[
 0=r_0<r_1<\cdots<r_h=m
\]

be the record values preceding an occurrence \(u\) in a normalized word.
Consecutive record gaps are at most \(\tau\).  The records at or below \(u\)
pay \(u\):

\[
 \sum_{r_i\le u}K_\tau(r_i,u)\ge u.
 \tag{2}
\]

Indeed, each record contributes at least the next record gap, and the last
record below \(u\) contributes the remaining distance to \(u\).  Consequently

\[
 \lambda_j(X)\ge0
 \tag{3}
\]

at every position of a normalized word.

If the word begins with two zeros, the second zero is not needed in (2).
It is therefore available as an additional kernel contribution.  In
particular, if the record peak is \(m\), then

\[
 \sum_j\lambda_j(X)\ge m,
 \tag{4}
\]

because at each positive record \(r_i\) the second zero contributes
\(K_\tau(0,r_i)=\min(\tau,r_i)\), and

\[
 \sum_i\min(\tau,r_i)
 \ge\sum_i(r_i-r_{i-1})=m.
\]

## Principle II: failed-splice propagation

Suppose \(X=(x_0,\ldots,x_{N-1})\) is normalized and \(x_1>0\).  The entry
\(x_1\) has the unique predecessor \(x_0=0\).  If it is nonfinal and is not
extractable, its splice must fail:

\[
 x_2>x_0+\tau.
\]

Normalization then shows that \(x_2>x_1\) and that \(x_1\) is the unique
predecessor of \(x_2\).  Iterating gives the following propagation rule:

> If none of \(x_1,\ldots,x_h\) is extractable, then
> \[
>  x_{i+2}>x_i+\tau\qquad(0\le i<h),
>  \tag{5}
> \]
> and the entries through \(x_{h+1}\) are strictly increasing records.

Two consequences will be used repeatedly.

- A full skeleton of length at least two begins with \((0,0)\).  Otherwise
  (5) propagates to the final entry, where the unique-predecessor occurrence
  is extractable.
- A leftmost extractable occurrence is a record.  Before the first such
  occurrence, (5) propagates through records.

The same argument gives the blocking rule used below: if a final leftmost
extractable occurrence is made nonextractable by a valid appended entry,
the unique-predecessor chain continues to that appended entry, which is then
extractable at the new right boundary.

## Principle III: extraction transport

Let \(e\) be a leftmost extractable occurrence, let \(C\) be obtained by
deleting it, and put \(p=e-1\).  Then

\[
 \area(C:p)=\area(D)-1,
 \qquad
 \dinv_\tau(C:p)=\dinv_\tau(D)+1,
 \qquad
 \defc_\tau(C:p)=\defc_\tau(D).
 \tag{6}
\]

To prove this, write \(D=A:e:B\).  For \(b\in B\), reversing the orientation
of the pair and lowering \(e\) gives

\[
 d_\tau(e,b)=d_\tau(b,e-1).
\]

For \(a\in A\),

\[
 d_\tau(a,e-1)-d_\tau(a,e)
\]

equals \(1\) precisely on the predecessor interval of \(e\), equals \(-1\)
when \(e<a\le e+\tau\), and is zero otherwise.  Principle II says that
\(e\) is a record, so the negative case does not occur.  Extractability gives
exactly one predecessor, hence the dinv change is \(1\).  The area change is
\(-1\), proving (6).  Repeating the argument after \(k\) extractions gives

\[
 \area(T_k)=\area(D)-k,
 \quad
 \dinv_\tau(T_k)=\dinv_\tau(D)+k,
 \quad
 \defc_\tau(T_k)=\defc_\tau(D).
 \tag{7}
\]

These are pairwise identities even when the appended stage word is not
normalized.

## Principle IV: the double-zero boundary ledger

The following four configurations are the same kernel calculation.

| configuration | conclusion |
|---|---:|
| normalized length-\(s\) word beginning \((0,0)\), with only its final occurrence extractable | \(\defc_\tau\ge\tau(s-2)\) |
| full prefix \(R\) of length \(s-1\), followed by its first lowered extraction \(p\), where \(R:p\) is invalid or not full | \(\defc_\tau(R:p)\ge\tau(s-2)\) |
| first-extraction stage \(C:p\), where \(C\) begins \((0,0)\), East3 fails, and \(C\) has no extraction outside its final two positions | \(\defc_\tau(C:p)\ge\tau(s-2)\) |
| second-extraction stage \(R:p:q\), where \(R\) begins \((0,0)\), West3 fails, and \(R\) has no extraction outside its final position | \(\defc_\tau(R:p:q)\ge\tau(s-2)\) |

Here \(|C|=s-1\) and \(|R|=s-2\) in the last two rows.  In the East case
failure means

\[
 C[-1]>p+\tau,
 \tag{8}
\]

while in the West case it means

\[
 p>R[-1]+\tau.
 \tag{9}
\]

We prove all four statements at once.  Use the preceding record chain to pay
the subtraction in every lambda increment, as in Principle I.  The second
initial zero remains unused.  Scan the remaining entries from left to right.
If an entry has at least two predecessors, the two corresponding kernel
triangles provide a full \(\tau\)-unit.  If it has a unique predecessor and
is not extractable, Principle II forces its outgoing splice to fail.  The
unpaid part of the same \(\tau\)-unit is then carried to the next record.
Since record jumps are at most \(\tau\), every carry is nonnegative and all
interior carries telescope.

At the right boundary the carry is closed in one of four equivalent ways:
by an extractable final entry, by the invalid/fullness-obstructing append, by
the far pair (8), or by the reverse far pair (9) together with the two
extraction anchors.  The resulting count is

\[
 \underbrace{\tau}_{\text{second zero}}
 +\underbrace{(s-5)\tau}_{\text{interior, if present}}
 +\underbrace{2\tau}_{\text{terminal block}}
 =\tau(s-2).
 \tag{10}
\]

In the first two configurations the split between the interior and terminal
block moves by one position, but the total number of \(\tau\)-units remains
\(s-2\).  Every kernel term omitted from the ledger is nonnegative.  This
proves all four boundary estimates.

For reference, the first row also has the following explicit record/nonrecord
form.  If the final extractable value is \(e\), then \(e\ge\tau+1\).  Let
\(0=r_0<\cdots<r_h=m\) be the prefix records and let \(N\) be the number of
nonrecord middle occurrences.  The far-pair inequality

\[
 K_\tau(0,u)+K_\tau(u,e)\ge\tau
\]

pays each nonrecord, while the record chain pays \(\tau h\); since
\(N+h=s-3\), the total is \(\tau+\tau N+\tau h=\tau(s-2)\).

## Principle V: rapid-chain estimates

Let

\[
 R=(r_0,\ldots,r_{m-1}),
 \qquad r_0=0,
\]

be strictly increasing and normalized, with

\[
 r_{i+2}>r_i+\tau.
 \tag{11}
\]

Only adjacent pairs of \(R\) contribute to dinv, so

\[
 \dinv_\tau(R)
 =\sum_{i=0}^{m-2}\bigl(\tau-(r_{i+1}-r_i)\bigr)
 =\tau(m-1)-r_{m-1}.
 \tag{12}
\]

For any nonnegative target \(u\), the contributing records on either side of
\(u\) form two truncated triangles.  Condition (11) prevents three records
on either side from occupying an interval of width \(\tau\), and pairing the
two closest records on each side gives

\[
 \sum_i d_\tau(r_i,u)\le2\tau.
 \tag{13}
\]

Finally, integrality in (11) gives

\[
 r_{2k}\ge k(\tau+1),
 \qquad
 r_{2k+1}\ge1+k(\tau+1).
 \tag{14}
\]

For a rapid word of length at least five this implies

\[
 \area(R)>\tau(|R|-1)\ge\dinv_\tau(R).
 \tag{15}
\]

We shall also use the shorter-chain estimate, valid for \(m\ge3\) and
\(c=r_{m-1}\),

\[
 \area(R)+3c+2>\tau(m+1).
 \tag{16}
\]

For \(m=3\), the minimal chain \((0,1,\tau+1)\) gives a surplus of \(7\).
On adjoining \(c'>c\), the surplus in (16) grows by

\[
 4c'-3c-\tau\ge c+4-\tau\ge5,
\]

which proves (16) by induction.

## Applications to the three UP lemmas

Throughout this section,

\[
 0\le d=\defc_\tau(D)\le\tau(s-2)-1,
 \qquad
 \area(D)\le L_d-1.
 \tag{17}
\]

The second inequality implies

\[
 \dinv_\tau(D)-\area(D)\ge2.
 \tag{18}
\]

### UP Lemma 1: validity of the full-skeleton branch

Let \(a=D[-1]\), let \(R\) be the prefix, and let \(m=\max R\).  Suppose
there is no anchor for \(a+1\).  Then no prefix entry lies in

\[
 [\max(0,a+1-\tau),a].
\]

This forces \(a\ge\tau\).  It also forces every prefix entry to be at most
\(a\): the first entry greater than \(a\), if one existed, would have an
immediate predecessor in the forbidden interval.  Hence

\[
 m\le a-\tau.
\]

The final Dyck inequality gives

\[
 a\le D[-2]+\tau\le m+\tau\le a,
\]

so

\[
 a=m+\tau,
 \qquad D[-2]=m.
 \tag{19}
\]

The full skeleton begins with \((0,0)\), by Principle II.  Principle I gives
at least \(m\) defect before the final position.  By (19), every prefix entry
is at most \(a-\tau\), so every prefix-to-final kernel equals \(\tau\), and

\[
 \lambda_{s-1}(D)=\tau(s-1)-a=\tau(s-2)-m.
\]

Therefore

\[
 \defc_\tau(D)\ge m+\tau(s-2)-m=\tau(s-2),
\]

contrary to (17).  Thus an anchor exists.  Inserting \(a+1\) immediately
after the first anchor preserves the new left adjacency; the old Dyck
inequality preserves the new right adjacency.  The injected word is therefore
normalized.

### UP Lemma 2: a nonfinal first extraction

Suppose the only extractable occurrence of \(D\) is its final one.  If
\(D[1]=0\), the first row of Principle IV gives

\[
 \defc_\tau(D)\ge\tau(s-2),
\]

contrary to (17).  If \(D[1]>0\), Principle II makes the whole word rapid,
and (15) gives \(\area(D)>\dinv_\tau(D)\), contrary to (18).  Hence some
extractable occurrence is nonfinal.

### The necessary correction to UP Lemma 3

The statement is false for \(s=5\) and every \(\tau\ge7\).  Let

\[
 D_\tau=(0,1,\tau,\tau+1,\tau+1).
\]

Then

\[
 \area(D_\tau)=3\tau+3,
 \qquad
 \dinv_\tau(D_\tau)=4\tau-2,
 \qquad
 \defc_\tau(D_\tau)=3\tau-1.
\]

Thus its defect is exactly \((s-2)\tau-1\), and for \(\tau\ge7\),

\[
 3\tau+3\le
 \left\lfloor\frac{7\tau+1}{2}\right\rfloor-1.
\]

The first extraction is \(e_1=1\), leaving

\[
 C_1=(0,\tau,\tau+1,\tau+1),
 \qquad
 C_1:(e_1-1)=(0,\tau,\tau+1,\tau+1,0).
\]

East3 fails, while the only extraction in \(C_1\) is its penultimate
\(\tau+1\).  Therefore UP Lemma 3 requires \(s\ge6\).

### UP Lemma 3 for \(s\ge6\)

Let \(e=e_1\), let \(C=C_1\), put \(p=e-1\), and write

\[
 \Sigma=C:p.
\]

If the last entry of \(C\) is \(c\), East3 failure says

\[
 c>p+\tau.
 \tag{20}
\]

Assume that \(C\) has no extractable occurrence outside its final two
positions.  If \(C[1]=0\), the third row of Principle IV and (6) give

\[
 \defc_\tau(D)=\defc_\tau(\Sigma)\ge\tau(s-2),
\]

a contradiction.  Hence \(C[1]>0\).

Principle II now makes

\[
 R=C[0:-1]=(r_0,\ldots,r_{m-1}),
 \qquad m=s-2,
\]

a rapid chain.  Write \(B=r_{m-1}\).  The pair \((c,p)\) has zero dinv by
(20), and (12)--(13) give

\[
 \dinv_\tau(\Sigma)
 \le \tau(m-1)-B+4\tau.
\]

Since \(B\ge1\), transport gives

\[
 \dinv_\tau(D)\le\tau(s+1)-2.
 \tag{21}
\]

The defect cutoff and (18) imply

\[
 2\dinv_\tau(D)
 \ge M_s-\tau(s-2)+3.
 \tag{22}
\]

For \(s\ge7\), (21)--(22) are incompatible because

\[
 \bigl(M_s-\tau(s-2)+3\bigr)
 -2\bigl(\tau(s+1)-2\bigr)
 =\tau\frac{s(s-7)}2+7>0.
\]

It remains to treat \(s=6\).  Write

\[
 R=(0,a,b,c),
 \qquad
 \Sigma=(0,a,b,c,z,p).
\]

Rapid growth, normalization, and East3 failure give

\[
 1\le a\le\tau,
 \quad \tau<b\le a+\tau,
 \quad a+\tau<c\le b+\tau,
 \quad z\le c+\tau,
 \quad z>p+\tau.
 \tag{23}
\]

Put

\[
 I=\sum_{r\in\{0,a,b,c\}}
 \bigl(d_\tau(r,z)+d_\tau(r,p)\bigr),
 \qquad X=a+b+z+p.
\]

Then

\[
 \area(\Sigma)=X+c,
 \qquad
 \dinv_\tau(\Sigma)=3\tau-c+I.
 \tag{24}
\]

We use the following four-record estimate:

> Under (23), if
> \(\dinv_\tau(\Sigma)-\area(\Sigma)\ge4\), then
> \[
>  X+I\le8\tau.
>  \tag{25}
> \]

To check (25), substitute the two triangular formulas for \(d_\tau\) and
split at the positions of \(p\) relative to \(a,b,c\) and of \(z\) relative
to \(b,c\).  The possible rows are

| position of \(p\) | position of \(z\) | bound |
|---|---|---:|
| \(p<a\) | \(z\le b\) | \(X+I\le8\tau\) |
| \(p<a\) | \(b<z\le c\) | \(X+I\le8\tau\) |
| \(p<a\) | \(z>c\) | \(X+I\le8\tau\) |
| \(a\le p<b\) | \(b<z\le c\) | \(X+I\le8\tau\) |
| \(a\le p<b\) | \(z>c\) | \(X+I\le8\tau\) |
| \(b\le p<c\) | \(z>c\) | \(X+I\le8\tau\) |

The other rows are excluded by \(z>p+\tau\), \(b\le a+\tau\), and
\(c\le b+\tau\).  Within a row, further kernel endpoints give the same
affine inequality.  The hypothesis used in each row is the rearrangement

\[
 I\ge X+2c-3\tau+4
\]

of (24).  This proves (25).

By (6) and (18), the hypothesis of (25) holds.  Equations (24)--(25) give

\[
 \area(\Sigma)+\dinv_\tau(\Sigma)
 =X+3\tau+I\le11\tau.
\]

But this sum equals \(\area(D)+\dinv_\tau(D)\), while the cutoff requires it
to be at least \(11\tau+1\).  This contradiction completes UP Lemma 3.

## Applications to the three DOWN/West lemmas

Now assume

\[
 0\le d=\defc_\tau(D)\le\tau(s-2)-1,
 \qquad
 \area(D)\le L_d,
 \tag{26}
\]

and that DOWN is applicable.  Let \(e_1\) be the first extracted value and
\(C_1\) its normalized remainder.

### DOWN Lemma 1: the skeleton branch

Put \(p=e_1-1\).  If \(C_1:p\) is full, then \(C_1\) is full: every
nonfinal extraction of \(C_1\) persists after appending \(p\), while if its
only extraction is final and the append blocks it, the blocking rule in
Principle II makes \(p\) extractable.

Conversely, suppose \(C_1\) is full.  It begins with \((0,0)\).  If
\(C_1:p\) were invalid or not full, the second row of Principle IV and
transport would give

\[
 \defc_\tau(D)=\defc_\tau(C_1:p)\ge\tau(s-2),
\]

contrary to (26).  Hence \(C_1:p\) is normalized and full.  In particular,

\[
 e_1-1\le C_1[-1]+\tau.
\]

This proves the stated equivalence and validity.

### DOWN Lemma 2: the next extraction

This is definitional: a normalized word is not full precisely when it has an
extractable occurrence.  Hence if \(C_1\) is not full, its leftmost
extractable occurrence \(e_2\) exists, with no position restriction.

### DOWN Lemma 3: an extraction before the final position

Let \(C_2\) be obtained by deleting \(e_2\) from \(C_1\), and put

\[
 p=e_1-1,
 \qquad q=e_2-1,
 \qquad T_1=C_2:p:q.
\]

Write \(c=C_2[-1]\).  West3 failure is

\[
 p>c+\tau.
 \tag{27}
\]

Suppose that \(C_2\) has no extractable occurrence outside its final
position.  Twofold transport and the weak lower-half inequality give

\[
 \dinv_\tau(T_1)-\area(T_1)
 =\dinv_\tau(D)-\area(D)+4\ge4.
 \tag{28}
\]

If \(C_2[1]=0\), the fourth row of Principle IV gives

\[
 \defc_\tau(D)=\defc_\tau(T_1)\ge\tau(s-2),
\]

contrary to (26).

Assume instead that \(C_2[1]>0\).  Principle II makes

\[
 C_2=R=(r_0,\ldots,r_{m-1}),
 \qquad m=s-2,
 \qquad c=r_{m-1},
\]

a rapid chain.  The unique predecessor of \(e_1=p+1\) is at least
\(p+1-\tau>c\).  It cannot remain in the increasing word \(C_2\), whose
maximum is \(c\), so it must be the second extracted value \(e_2\).  Hence

\[
 q=e_2-1\ge p-\tau>c.
 \tag{29}
\]

No pair from \(R\) to \(p\) contributes to dinv.  By (12)--(13),

\[
 \dinv_\tau(T_1)
 \le \tau(m-1)-c+2\tau+\tau
 =\tau(m+2)-c.
 \tag{30}
\]

From (27), (29), and integrality,

\[
 \area(T_1)=\area(R)+p+q
 \ge\area(R)+2c+\tau+2.
 \tag{31}
\]

Principle V, equation (16), now gives

\[
 \area(T_1)-\dinv_\tau(T_1)
 \ge\area(R)+3c+2-\tau(m+1)>0,
\]

contradicting (28).  Thus \(C_2\) has an extractable occurrence outside its
final position, as required.

## Invertibility of UP and DOWN through level 5

We now prove that the UP and DOWN constructions are inverse on every branch
used here.  Both members of the distinguished global pair
\((0,\ldots,0,\tau)\leftrightarrow\epsilon_{s,\tau}\) have defect
\(\tau(s-2)\), so they lie one step outside the present cutoff.  If they are
retained in a larger domain, their two declared global rules plainly invert
one another.

### Two inverse mechanisms

Write \(\operatorname{inj}_e(X)\) for insertion of \(e\) immediately after
the first occurrence of its predecessor interval.  The following facts are
used in all six branch calculations.

**Extraction--injection stack.**  If an occurrence \(e\) is extracted from
\(D\), leaving \(C\), then

\[
 \operatorname{inj}_e(C)=D.
 \tag{32}
\]

Conversely, the occurrence inserted in \(\operatorname{inj}_e(C)\) is
extractable: the first-anchor convention puts exactly one predecessor before
it, and deleting it restores the two old neighboring entries.  In the
admissible level-3 and level-5 configurations below, several entries injected
right to left are therefore extracted in reverse injection order.  We use
this local statement as the stack property.

At a level-3 or level-5 stage there is a retained suffix entry.  The position
lemmas proved above ensure that the relevant extraction anchors lie in the
prefix before that retained entry.  The inequalities in the corresponding
East/West case then provide, successively, the anchors for the other injected
entries.  Consequently all local injections land before the retained suffix,
so the displayed decompositions \(Q:r\), \(Q:x\), and so forth are literal
decompositions of the resulting word.

We shall also use the successive-extraction inequality.  If \(e_1\) and
\(e_2\) are successive leftmost extracted values, then

\[
 e_1\le e_2+\tau.
 \tag{33}
\]

Suppose instead that \(e_1>e_2+\tau\).  Then \(e_1\) is not in the
predecessor interval of \(e_2\), so deleting \(e_1\) does not improve the
predecessor count of \(e_2\).  If the two occurrences are not adjacent, it
does not change the splice at \(e_2\) either, and \(e_2\) would already have
been extractable before \(e_1\).  If \(e_2\) immediately precedes \(e_1\),
the original Dyck inequality directly gives \(e_1\le e_2+\tau\), a
contradiction.  If \(e_1\) immediately precedes \(e_2\), removing the larger
left neighbor cannot turn a previously failed splice at \(e_2\) into a valid
one; again \(e_2\) would already have been extractable.  Thus (33) holds.

**Local inversion.**  East3 and West3 are identity moves on their respective
domains.  East5 and West5 are mutually inverse.  More explicitly, if

\[
 \operatorname{East}_5(*,b,c,x,y)=(*,r,j,k,y),
 \tag{34}
\]

then

\[
 j>r+\tau,
 \qquad
 \operatorname{West}_5(*,r,j,k,y)=(*,b,c,x,y).
 \tag{35}
\]

The first inequality says that West3 fails on \((r,j,k)\).  It follows
directly in both East5 cases: in case 2b, \((r,j,k)=(x,c,b)\), so it is the
original inequality \(c>x+\tau\); in case 2a, \(j\) is the appropriate one
of \(b,c\), and the defining inequalities again give \(j>x+\tau=r+\tau\).
Reversing the same case calculation proves the converse statement for a
West5 input.

### UP followed by DOWN

#### The full-skeleton branch

Write the initial full skeleton as

\[
 S=C:a.
\]

The prefix \(C\) is full.  Otherwise an extractable occurrence of \(C\)
would persist in \(S\); if its final extraction were blocked by appending
\(a\), the blocking rule in Principle II would make \(a\) extractable in
\(S\).  Either conclusion contradicts fullness.

UP injects \(a+1\) into \(C\).  By the stack property, the inserted
occurrence is the first extractable occurrence.  DOWN extracts it, recovers
the full prefix \(C\), and therefore takes its skeleton branch.  That branch
appends

\[
 (a+1)-1=a,
\]

recovering \(C:a=S\).

#### The East3/West3 branch

Write the initial word as

\[
 D=P:b,
 \qquad
 P=\operatorname{inj}_{x+1}(P').
\]

After extracting \(x+1\), the East3 stage is

\[
 P':b:x.
\]

East3 is the identity, and UP injects the raised final entries right to left:

\[
 Q=
 \operatorname{inj}_{b+1}
 \bigl(\operatorname{inj}_{x+1}(P')\bigr).
 \tag{36}
\]

By the stack property, DOWN extracts \(b+1\) and then \(x+1\).  In
particular, after the first extraction another extraction remains, so the
DOWN skeleton branch does not apply.  The two extractions reproduce
\(P':b:x\).

Because the original extraction of \(x+1\) from \(P:b\) was valid,
\(P':b\) is normalized.  Hence

\[
 b\le P'[-1]+\tau,
\]

which is exactly the West3 condition on the final window of \(P':b:x\).
West3 leaves the window unchanged.  Finally DOWN injects \(x+1\) into
\(P':b\).  Its original anchor is in \(P'\), before the appended \(b\), so
(32) recovers \(P:b=D\).

#### The East5/West5 branch

Write the word remaining after the two UP extractions as \(P':b:c\), and
write the extracted values as \(x+1,y+1\).  The East5 stage is

\[
 P':b:c:x:y.
\]

Suppose, in the notation of (34), that

\[
 P':b:c:x:y
 \xrightarrow{\operatorname{East}_5}
 P':r:j:k:y.
\]

UP injects \(y+1,k+1,j+1\), in that order, into the base \(P':r\).
The second extraction occurred before the last two positions, so \(y+1\)
has an anchor in \(P'\).  The East5 inequalities then give prefix anchors for
\(k+1\) and \(j+1\).  Thus all three injections occur before \(r\), and the
UP output has the form

\[
 Q:r.
\]

DOWN successively extracts

\[
 j+1,\qquad k+1,\qquad y+1.
\]

After its first extraction at least two further extractions remain, so the
skeleton branch cannot apply.  After its second extraction, the West3 window
is \((r,j,k)\); it fails by (35).  DOWN therefore performs the third
extraction and reaches

\[
 P':r:j:k:y.
\]

West5 sends this back to \(P':b:c:x:y\).  Finally, DOWN injects \(y+1\) and
then \(x+1\), reversing the original two extractions and recovering the
initial word.

### DOWN followed by UP

#### The DOWN skeleton branch

Suppose DOWN extracts \(x+1\), leaving a full prefix \(C\), and returns

\[
 S=C:x.
\]

DOWN Lemma 1 says that \(C:x\) is itself full.  UP therefore takes its
full-skeleton branch: it removes the terminal \(x\), raises it to \(x+1\),
and injects it into \(C\).  By (32), this recovers the original DOWN input.

#### The West3/East3 branch

Suppose DOWN extracts \(x+1\) and then \(y+1\), leaving \(P':b\).  Its
West3 stage is

\[
 P':b:x:y.
\]

West3 is the identity.  DOWN injects \(y+1\) before the retained \(x\), so
its output has the form

\[
 Q:x.
\]

The inserted \(y+1\) is extractable, so \(Q:x\) is not full and UP does not
take its skeleton branch.  UP extracts \(y+1\), appends \(y\), and reproduces
the window \((b,x,y)\).  The successive-extraction inequality (33) gives

\[
 x\le y+\tau,
\]

which is exactly the East3 condition.  East3 leaves the stage unchanged.
UP then injects \(y+1\) and \(x+1\), in reverse extraction order, and recovers
the original DOWN input.

#### The West5/East5 branch

Suppose DOWN extracts \(x+1,y+1,z+1\), none from the final position, leaving
\(P':b\).  Its West5 stage is

\[
 P':b:x:y:z.
\]

Write

\[
 P':b:x:y:z
 \xrightarrow{\operatorname{West}_5}
 P':j:k:r:z.
 \tag{37}
\]

DOWN injects \(z+1\) and then \(r+1\).  The surviving prefix anchors place
both before the retained \(j,k\), so the DOWN output is

\[
 Q:j:k.
\]

It has successive extractable occurrences \(r+1,z+1\), and hence is not a
full skeleton.  UP first extracts \(r+1\) and appends \(r\).  Its East3
window is \((j,k,r)\).  Since the right side of (37) lies in the East5
domain,

\[
 k>r+\tau,
\]

so East3 fails.  UP extracts \(z+1\) and reaches

\[
 P':j:k:r:z.
\]

East5, being inverse to West5, returns \(P':b:x:y:z\).  UP finally injects

\[
 z+1,\qquad y+1,\qquad x+1,
\]

which reverses the original three extractions and recovers the starting word.

All possible branches through level 5 have now been paired, proving

\[
 \operatorname{DOWN}\circ\operatorname{UP}=\mathrm{id},
 \qquad
 \operatorname{UP}\circ\operatorname{DOWN}=\mathrm{id}
\]

on the domain under consideration.

## Statistic changes under UP and DOWN

The statistic calculation is uniform and does not require a separate check
for each branch.

The extraction transport identity (6) says that extracting \(e\), deleting
it, and placing \(e-1\) at the right end changes

\[
 (\area,\dinv_\tau)\longmapsto(\area-1,\dinv_\tau+1).
 \tag{38}
\]

Extraction and injection are inverse operations.  Consequently, if \(X:p\)
is a stage word and \(Y\) is obtained by raising \(p\) to \(p+1\) and
injecting it into \(X\), then

\[
 \area(Y)=\area(X:p)+1,
 \qquad
 \dinv_\tau(Y)=\dinv_\tau(X:p)-1.
 \tag{39}
\]

This is also immediate by applying (38) to \(Y\): extracting its newly
injected occurrence recovers \(X:p\).  Thus each raised injection reverses
one extraction transport.

It remains to note that the local East move does not change either statistic.
East3 is the identity.  East5 only rearranges its five entries, so it plainly
preserves area.  Its interactions with every earlier prefix occurrence are
also unchanged, because the five-window has the same multiset before and
after the rearrangement.  Thus only the internal dinv contribution needs to
be checked.  Direct substitution in the two East5 cases gives

\[
 \sum_{i<j}d_\tau(w_i,w_j)
 =\sum_{i<j}d_\tau(w'_i,w'_j),
 \tag{40}
\]

where \(w\) and \(w'\) are the input and output windows.  In case 2a the
only additional observation is that \(\bk_\tau\) either fixes or switches
the middle pair according to the same gap inequality.

Now suppose an UP branch makes \(k\) extractions before its local East move.
By (38), the stage word then has statistics

\[
 (\area(D)-k,\dinv_\tau(D)+k).
\]

The East move leaves these unchanged.  UP then makes \(k+1\) raised
injections.  Applying (39) \(k+1\) times gives

\[
 \area(\operatorname{UP}(D))=\area(D)+1,
 \qquad
 \dinv_\tau(\operatorname{UP}(D))=\dinv_\tau(D)-1,
 \tag{41}
\]

and hence UP preserves defect.  This includes the skeleton branch by taking
\(k=0\).

Since DOWN is the inverse of UP, its statistic change is automatically the
reverse:

\[
 \area(\operatorname{DOWN}(D))=\area(D)-1,
 \qquad
 \dinv_\tau(\operatorname{DOWN}(D))=\dinv_\tau(D)+1.
 \tag{42}
\]

## Plan for the cohesive decomposition proof

The final proof will be written for \(s\ge6\) and will assume the following
three inputs.

1. **Skeleton position.**  Every special skeleton \(S\) in the range under
   consideration satisfies the stronger bound
   \[
     \area(S)\le\defc_\tau(S).
     \tag{43}
   \]
2. **East5 nonfailure.**  Every East5 stage arising from a strict-lower-half
   path of defect at most \(\tau(s-2)-1\) succeeds.
3. **West5 nonfailure.**  Every West5 stage arising from a weak-lower-half
   nonskeleton of defect at most \(\tau(s-2)-1\) succeeds.

The known \(q,t\)-symmetry of the \((\tau s+1,s)\)-Catalan polynomial is also
an ambient assumption.

### Step 1: establish the roots are below the middle

Put

\[
 B=\tau(s-2)-1.
\]

If \(S\) is a special skeleton with defect \(d\le B\), then (43) gives

\[
 2\area(S)+d\le3d\le3B.
\]

For \(s\ge6\),

\[
 M_s-3B
 =\tau\frac{(s-3)(s-4)}2+3>0.
\]

Hence

\[
 2\area(S)+d<M_s,
\]

so every root is in fact strictly below the middle of its defect layer.  The
exceptional skeleton and its global partner have defect \(\tau(s-2)=B+1\),
so within this range every full skeleton is special.

### Step 2: prove UP is total below the middle

Let \(D\) have defect \(d\le B\) and area at most \(L_d-1\).

- If \(D\) is full, UP Lemma 1 makes its raised-terminal injection valid.
- Otherwise UP Lemma 2 supplies a nonfinal first extraction.
- If East3 succeeds, the level-3 branch is defined.
- If East3 fails, UP Lemma 3 supplies the required second extraction outside
  the final two positions.
- The assumed East5 nonfailure theorem then makes the level-5 branch succeed.

The local anchor/normalization check makes the resulting word a normalized
Dyck word, and (41) gives the statistic change.

### Step 3: prove DOWN is total on lower-half nonskeletons

Let \(D\) have defect \(d\le B\), area at most \(L_d\), and suppose it is
not a special skeleton.

- The first extraction exists by nonfullness.
- DOWN Lemma 1 identifies exactly when the skeleton branch applies.
- If it does not apply, DOWN Lemma 2 supplies the second extraction.
- If West3 succeeds, the level-3 branch is defined.
- If West3 fails, DOWN Lemma 3 supplies a nonfinal third extraction.
- The assumed West5 nonfailure theorem makes the level-5 branch succeed.

The local validity check and (42) show that DOWN returns a normalized word of
the same defect and one smaller area.

### Step 4: quote branchwise invertibility

Use the six calculations in the invertibility section:

\[
 \operatorname{DOWN}\circ\operatorname{UP}=\mathrm{id},
 \qquad
 \operatorname{UP}\circ\operatorname{DOWN}=\mathrm{id}
\]

wherever the respective maps are defined.  Thus UP is injective, DOWN gives
the unique predecessor of every lower-half nonskeleton, and no UP string can
merge with another.

### Step 5: obtain the lower-half string decomposition

Fix a defect \(d\le B\).  Starting from any path in the weak lower half,
iterate DOWN until it is undefined.  Area drops by one at every step, so the
process terminates.  By Step 3 it can terminate only at a full, hence special,
skeleton.  Invertibility makes both this root and the entire descent unique.

Conversely, start at a special skeleton \(S\) of defect \(d\) and iterate UP
while the area is at most \(L_d-1\).  Step 2 and (41) give exactly one path at
each area

\[
 \area(S),\area(S)+1,\ldots,L_d.
\]

The lower half of the defect-\(d\) layer is therefore the disjoint union of
these rooted strings.

### Step 6: use symmetry and evaluate the strings

Let

\[
 N=M_s-d.
\]

Along the string rooted at \(S\), the path of area \(j\) has dinv \(N-j\).
Thus its lower-half contribution is

\[
 \sum_{j=\area(S)}^{\lfloor N/2\rfloor}q^{N-j}t^j.
\]

The assumed \(q,t\)-symmetry supplies the reflected upper half.  Since

\[
 \dinv_\tau(S)=N-\area(S),
\]

the complete contribution of the string is

\[
 \sum_{j=\area(S)}^{\dinv_\tau(S)}q^{N-j}t^j
 =
 \frac{
 q^{\dinv_\tau(S)+1}t^{\area(S)}
 -q^{\area(S)}t^{\dinv_\tau(S)+1}
 }{q-t}.
 \tag{44}
\]

Summing (44) over all special skeletons with defect at most \(B\) proves the
desired symmetric string formula.

## Structural summary

The six lemmas use only five reusable mechanisms:

1. record chains pay the negative part of every lambda increment;
2. a missing extraction propagates a failed splice and produces a rapid
   record chain;
3. extraction followed by appending the lowered value transports
   \((\area,\dinv)\) by \((-1,+1)\);
4. a second initial zero creates a spare \(\tau\)-unit at every obstructed
   boundary stage;
5. rapid chains have sparse dinv interactions and large area.

UP Lemma 1 and the \(s=6\) part of UP Lemma 3 are the only genuinely separate
boundary computations.  All other cases are direct applications of these
five principles.
