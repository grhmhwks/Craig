"""Section 3 row insertion algorithms.

The draft's "dual Dyck" rows are finite non-negative integer sequences whose
consecutive entries differ by at least +2.  The empty sequence is accepted:
the Section 3 rowsert definition explicitly allows empty input rows, and the
local gap condition is vacuous for length 0 and length 1.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal, Sequence


CaseName = Literal["case0", "case1", "case2", "case3"]


@dataclass(frozen=True)
class Chain:
    """A contiguous maximal +2-chain, using zero-based half-open indices."""

    start: int
    stop: int
    values: tuple[int, ...]

    @property
    def length(self) -> int:
        return self.stop - self.start


@dataclass(frozen=True)
class RowsertStep:
    case: CaseName
    f_chunk: tuple[int, ...]
    r_chunk: tuple[int, ...]
    index: int | None
    r_chain: Chain | None = None
    f_chain: Chain | None = None


@dataclass(frozen=True)
class WorsertStep:
    case: CaseName
    e_chunk: tuple[int, ...]
    r_chunk: tuple[int, ...]
    index: int | None
    r_chain: Chain | None = None
    e_chain: Chain | None = None


def is_dual_dyck(seq: Sequence[int]) -> bool:
    """Return whether ``seq`` satisfies the dual-Dyck step-gap condition."""

    return all(value >= 0 for value in seq) and all(
        seq[index + 1] >= seq[index] + 2 for index in range(len(seq) - 1)
    )


def _require_position(seq: Sequence[int], index: int) -> None:
    if not 0 <= index < len(seq):
        raise IndexError(f"position {index} is outside sequence of length {len(seq)}")


def maximal_plus2_chain_starting_at(seq: Sequence[int], index: int) -> Chain:
    """Return the maximal +2-chain starting at ``index``."""

    _require_position(seq, index)
    stop = index + 1
    while stop < len(seq) and seq[stop] == seq[stop - 1] + 2:
        stop += 1
    return Chain(index, stop, tuple(seq[index:stop]))


def maximal_plus2_chain_ending_at(seq: Sequence[int], index: int) -> Chain:
    """Return the maximal +2-chain ending at ``index``."""

    _require_position(seq, index)
    start = index
    while start > 0 and seq[start - 1] == seq[start] - 2:
        start -= 1
    return Chain(start, index + 1, tuple(seq[start : index + 1]))


def rowsert(
    r0: Sequence[int], f0: Sequence[int], *, trace: list[RowsertStep] | None = None
) -> tuple[list[int], list[int]]:
    """Apply the draft's row insertion operation.

    Inputs are copied on entry, so caller-owned lists are never mutated.  The
    returned pair is ``(E, R)``.
    """

    if not is_dual_dyck(r0):
        raise ValueError("r0 must be a dual Dyck sequence")
    if not is_dual_dyck(f0):
        raise ValueError("f0 must be a dual Dyck sequence")

    e: list[int] = []
    r = list(r0)
    f = list(f0)

    while f:
        first = f[0]
        index = next((idx for idx, value in enumerate(r) if first <= value + 1), None)

        if index is None:
            chunk = (first,)
            del f[:1]
            r.extend(chunk)
            if trace is not None:
                trace.append(RowsertStep("case0", chunk, (), None))
            continue

        if first <= r[index]:
            f_chunk = (first,)
            r_chunk = (r[index],)
            del f[:1]
            r[index] = first
            e.extend(r_chunk)
            if trace is not None:
                trace.append(RowsertStep("case1", f_chunk, r_chunk, index))
            continue

        r_chain = maximal_plus2_chain_starting_at(r, index)
        f_chain = maximal_plus2_chain_starting_at(f, 0)

        if r_chain.length <= f_chain.length:
            length = r_chain.length
            f_chunk = tuple(f[:length])
            r_chunk = tuple(r[index : index + length])
            del f[:length]
            r[index : index + length] = f_chunk
            e.extend(r_chunk)
            if trace is not None:
                trace.append(
                    RowsertStep("case2", f_chunk, r_chunk, index, r_chain, f_chain)
                )
        else:
            length = f_chain.length
            f_chunk = tuple(f[:length])
            del f[:length]
            e.extend(f_chunk)
            if trace is not None:
                trace.append(
                    RowsertStep("case3", f_chunk, (), index, r_chain, f_chain)
                )

    return e, r


def worsert(
    e0: Sequence[int], r0: Sequence[int], *, trace: list[WorsertStep] | None = None
) -> tuple[list[int], list[int]]:
    """Apply the corrected reverse row insertion operation.

    Inputs are copied on entry, so caller-owned lists are never mutated.  The
    returned pair is ``(R, F)``.  Case 0 follows the author clarification for
    CA-0001: the removed final element of ``E`` is prepended to ``R``, not
    ``F``.
    """

    if not is_dual_dyck(e0):
        raise ValueError("e0 must be a dual Dyck sequence")
    if not is_dual_dyck(r0):
        raise ValueError("r0 must be a dual Dyck sequence")

    e = list(e0)
    r = list(r0)
    f: list[int] = []

    while e:
        last = e[-1]
        index = next(
            (idx for idx in range(len(r) - 1, -1, -1) if last >= r[idx] - 1),
            None,
        )

        if index is None:
            chunk = (last,)
            del e[-1:]
            r[0:0] = chunk
            if trace is not None:
                trace.append(WorsertStep("case0", chunk, (), None))
            continue

        if last >= r[index]:
            e_chunk = (last,)
            r_chunk = (r[index],)
            del e[-1:]
            r[index] = last
            f[0:0] = r_chunk
            if trace is not None:
                trace.append(WorsertStep("case1", e_chunk, r_chunk, index))
            continue

        r_chain = maximal_plus2_chain_ending_at(r, index)
        e_chain = maximal_plus2_chain_ending_at(e, len(e) - 1)

        if r_chain.length <= e_chain.length:
            length = r_chain.length
            start = index - length + 1
            e_chunk = tuple(e[-length:])
            r_chunk = tuple(r[start : index + 1])
            del e[-length:]
            r[start : index + 1] = e_chunk
            f[0:0] = r_chunk
            if trace is not None:
                trace.append(
                    WorsertStep("case2", e_chunk, r_chunk, index, r_chain, e_chain)
                )
        else:
            length = e_chain.length
            e_chunk = tuple(e[-length:])
            del e[-length:]
            f[0:0] = e_chunk
            if trace is not None:
                trace.append(
                    WorsertStep("case3", e_chunk, (), index, r_chain, e_chain)
                )

    return r, f


def di_statistic(seq: Iterable[int]) -> int:
    """Count ordered pairs ``i < j`` with ``seq[i] = seq[j] + 1``."""

    values = list(seq)
    total = 0
    for left in range(len(values)):
        for right in range(left + 1, len(values)):
            if values[left] == values[right] + 1:
                total += 1
    return total
