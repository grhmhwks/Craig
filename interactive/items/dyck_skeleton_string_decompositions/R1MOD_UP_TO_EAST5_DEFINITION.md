# r == 1 mod s Up Map Through East5

Source of record:

```text
Combinatorics/items/dyck_skeleton_string_decompositions/code/check_r1mod_skeleton_strings.py
```

This is the current item-level implementation of the conjectural
`r = tau*s + 1` skeleton-string up map through the East5 branch.  It is not a
proved theorem in the repository.  The implementation deliberately stops when
the next branch would require an East7 move:

```python
UNSUPPORTED_LEVEL_7 = "unsupported_level_7"
```

So "defined up to East5" means:

- full-skeleton and special-skeleton branches are implemented;
- the first local branch uses `east3`;
- the second local branch uses `east5`;
- if neither branch applies after two extractions, `up_step` returns failure
  with reason `unsupported_level_7`.

## Local Data

Words are normalized `tau`-affine Dyck words.  The helper `bk2` is the
`tau`-version of the adjacent two-entry swap used inside the East5 case.

```python
Word = tuple[int, ...]


@dataclass(frozen=True)
class LocalResult:
    success: bool
    output: Word | None
    case: str
    reason: str | None = None


@dataclass(frozen=True)
class StepResult:
    success: bool
    output: Word | None
    direction: str
    branch: str
    level: int | None
    reason: str | None = None
    window: Word | None = None
    local_case: str | None = None


def bk2(a: int, b: int, tau: int) -> tuple[int, int]:
    return (b, a) if a > b + tau else (a, b)
```

## Extraction And Injection Helpers

The up map repeatedly extracts the leftmost currently extractable entry, lowers
each extracted entry by `1`, applies a local East move to the final window, and
then injects the raised output entries back from right to left.

```python
@lru_cache(maxsize=None)
def remove_at(word: Word, position: int) -> Word:
    values = tuple(word)
    return values[:position] + values[position + 1 :]


@lru_cache(maxsize=None)
def find_extractable(word: Word, tau: int, *, include_final: bool = True) -> int | None:
    values = tuple(word)
    if not is_normalized(values, tau):
        raise ValueError(f"not normalized: {values}")
    return find_extractable_normalized(values, tau, include_final=include_final)


def find_extractable_normalized(values: Word, tau: int, *, include_final: bool = True) -> int | None:
    max_value = tau * (len(values) - 1)
    prior_counts = [0] * (max_value + 1)
    for index, value in enumerate(values):
        if value == 0:
            prior_counts[0] += 1
            continue
        if not include_final and index == len(values) - 1:
            prior_counts[value] += 1
            continue
        lower = max(0, value - tau)
        prior_count = 0
        for prior in range(lower, value):
            prior_count += prior_counts[prior]
        if prior_count != 1:
            prior_counts[value] += 1
            continue
        if 0 < index and index + 1 < len(values) and values[index + 1] > values[index - 1] + tau:
            prior_counts[value] += 1
            continue
        return index
    return None


def rational_inject_normalized(values: Word, entry: int, tau: int) -> Word:
    lower = max(0, entry - tau)
    anchor = next((index for index, value in enumerate(values) if lower <= value <= entry - 1), None)
    if anchor is None:
        raise ValueError(f"no injection anchor for {entry} in {values}")
    return values[: anchor + 1] + (entry,) + values[anchor + 1 :]


@lru_cache(maxsize=None)
def inject_right_to_left(base: Word, entries: Word, tau: int) -> Word:
    out = tuple(base)
    for entry in reversed(tuple(entries)):
        out = rational_inject_normalized(out, entry, tau)
    return out
```

## East3

For a 3-window `(a,c,d)`, East3 succeeds exactly when `c <= d + tau`.  In the
current rational implementation, successful East3 is the identity on the local
window.

```python
@lru_cache(maxsize=None)
def east3(window: Word, tau: int) -> LocalResult:
    values = tuple(window)
    if len(values) != 3:
        raise ValueError("East3 needs a 3-window")
    _, c, d = values
    if c <= d + tau:
        return LocalResult(True, values, "east3_identity")
    return LocalResult(False, None, "east3_fail", "c >> d")
```

## East5

For a 5-window `(a,b,c,d,e)`, East5 is only considered when the centered East3
on `(b,c,d)` fails.  Then the implementation has two cases.

Case 2b:

```text
b <= d + tau and b <= e + tau
```

with output:

```text
(a,d,c,b,e)
```

Case 2a:

```text
b > d + tau, (b',c') = bk2(b,c), and c' <= e + tau
```

with output:

```text
(a,d,b',c',e)
```

The exact implementation is:

```python
@lru_cache(maxsize=None)
def east5(window: Word, tau: int) -> LocalResult:
    values = tuple(window)
    if len(values) != 5:
        raise ValueError("East5 needs a 5-window")
    a, b, c, d, e = values
    if east3((b, c, d), tau).success:
        return LocalResult(False, None, "east5_outside_domain", "East3 would pass")
    if b <= d + tau:
        if b <= e + tau:
            return LocalResult(True, (a, d, c, b, e), "east5_case2b")
        return LocalResult(False, None, "east5_case2b_fail", "b >> e")
    b_prime, c_prime = bk2(b, c, tau)
    if c_prime <= e + tau:
        return LocalResult(True, (a, d, b_prime, c_prime, e), "east5_case2a")
    return LocalResult(False, None, "east5_case2a_fail", "c' >> e")
```

## Up Step Through East5

The current up map is `up_step(word,tau)`.  Its branches are:

1. Special input:
   `(0,...,0,tau)` maps to the excluded full skeleton
   `(0,0,1,0,...,0,tau)` when `s >= 4`.
2. Full skeleton:
   inject the final entry plus `1` into the prefix.
3. East3 local branch:
   extract once, append `e1-1`, apply `east3` to the last three entries, then
   inject the final two local output entries raised by `1`.
4. East5 local branch:
   extract twice, append `(e1-1,e2-1)`, apply `east5` to the last five entries,
   then keep the first two local output entries in the base and inject the
   final three local output entries raised by `1`.
5. If East5 does not apply, return `unsupported_level_7`.

Exact implementation:

```python
@lru_cache(maxsize=None)
def up_step(word: Word, tau: int) -> StepResult:
    values = tuple(word)
    s = len(values)
    if not is_normalized(values, tau):
        return StepResult(False, None, "up", "failed", None, f"not normalized: {values}")
    try:
        if s >= 4 and values == special_input(s, tau):
            return checked_step("up", values, excluded_full_skeleton(s, tau), tau, branch="special", level=3)
        if is_full_skeleton_normalized(values, tau):
            result = rational_inject_normalized(values[:-1], values[-1] + 1, tau)
            return checked_step("up", values, result, tau, branch="full_skeleton", level=3)
        j1 = find_extractable(values, tau)
        if j1 is None:
            return StepResult(False, None, "up", "failed", None, f"no first extractable in {values}")
        e1 = values[j1]
        c1 = remove_at(values, j1)
        sigma1 = c1 + (e1 - 1,)
        attempt3 = east3(sigma1[-3:], tau)
        if attempt3.success:
            if j1 >= s - 2:
                return StepResult(False, None, "up", "failed", None, f"East3 position bound failed: j1={j1}")
            assert attempt3.output is not None
            result = inject_right_to_left(sigma1[:-2], (attempt3.output[-2] + 1, attempt3.output[-1] + 1), tau)
            return checked_step("up", values, result, tau, branch="local", level=3, window=sigma1[-3:], local_case=attempt3.case)
        j2 = find_extractable(c1, tau)
        if j2 is None:
            return StepResult(False, None, "up", "failed", None, f"no second extractable in {c1}")
        e2 = c1[j2]
        c2 = remove_at(c1, j2)
        sigma2 = c2 + (e1 - 1, e2 - 1)
        attempt5 = east5(sigma2[-5:], tau)
        if attempt5.success:
            if j1 >= s - 3:
                return StepResult(False, None, "up", "failed", None, f"East5 position bound failed: j1={j1}")
            if j2 > len(c1) - 3:
                return StepResult(False, None, "up", "failed", None, f"East5 position bound failed: j2={j2}")
            assert attempt5.output is not None
            base = sigma2[:-5] + attempt5.output[:2]
            result = inject_right_to_left(base, tuple(value + 1 for value in attempt5.output[2:]), tau)
            return checked_step("up", values, result, tau, branch="local", level=5, window=sigma2[-5:], local_case=attempt5.case)
        return StepResult(False, None, "up", "failed", None, UNSUPPORTED_LEVEL_7)
    except (IndexError, ValueError) as exc:
        return StepResult(False, None, "up", "failed", None, str(exc))
```

## Status

This file records the definition implemented in the repo.  The surrounding item
marks the `r = tau*s + 1` skeleton-string map as conjectural/computational.
The implementation checks that a successful step preserves defect, increases
area by `1`, decreases dinv by `1`, and produces a normalized word.  No general
proof of the East3/East5 rational map is recorded here.
