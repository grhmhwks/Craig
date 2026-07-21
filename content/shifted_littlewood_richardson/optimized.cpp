/*
Optimized exhaustive checks for the shifted Q/R and P tableau conjectures.

MATHEMATICAL SCOPE
------------------
For a charged bound N, the Q/R mode checks every proper skew shifted shape
lambda/mu with |lambda| <= N and every actual-entry degree

    |lambda/mu| <= n <= N - |mu|,

by comparing the counts of standard shifted set-valued tableaux with no
consecutive labels in one box, refined by (n, peak set), against the same
coefficient-weighted counts for straight shapes.  The coefficients are the
lattice highest-weight R-tableaux.  Inflation and budding make these exactly
the finite equalities required by the Q conjecture in that range.

The P mode checks the analogous coefficient-weighted identity after converting
each standard-tableau record

    (n, P-peak set, same-box consecutive-pair set, diagonal-label set)

into dominant-monomial coefficients.  Every partition of n is included when
--num-vars >= n.  Hence --num-vars N checks every dominant monomial in the
charged range.  The coefficients are the lattice highest-weight P-tableaux
with all entries in present diagonal boxes primed.

EXACTNESS OF THE OPTIMIZATIONS
------------------------------
* State compression merges only states with identical data needed by all
  future insertions and by the final statistic.
* A skew tableau is obtained uniquely by deleting a canonical initial segment;
  batching merely distributes these linear counts among independent seed
  states and adds them afterward.
* In Q/R coefficient enumeration, strict target weights are exhaustive by the
  strict-dominance argument.  The reverse target scan enforces exactly the
  backward lattice scan, the forward lattice scan, and the first-occurrence
  priming condition; it is a pruning/reformulation, not a weaker test.
* In P mode the signature-to-monomial transform is linear, so transforming
  each batch before summing is exact.
* Count additions and products are overflow-checked by default.  Define
  FAST_UNCHECKED_COUNTS only to remove those guards for benchmarking.

BUILD
-----
Requires a C++20 compiler, OpenMP, and the header-only Boost.Unordered flat map.
A typical build is

    g++ -O3 -march=native -DNDEBUG -std=c++20 -fopenmp \
        optimized.cpp -o optimized

RECREATING THE COMPLETED CHECKS
-------------------------------
The source chooses the historical batch sizes automatically at these bounds;
they can also be overridden with QR_BATCH_SIZE and P_BATCH_SIZE.

    QR_BATCH_SIZE=500000 ./optimized --mode qr --max-entries 21 --progress
    P_BATCH_SIZE=1000    ./optimized --mode p  --max-entries 17 \
                                      --num-vars 17 --progress

or, with separate bounds in one invocation,

    QR_BATCH_SIZE=500000 P_BATCH_SIZE=1000 \
    ./optimized --mode both --qr-bound 21 --p-bound 17 --num-vars 17 --progress

Set OMP_NUM_THREADS to the desired number of OpenMP threads.  Batch sizes trade
memory against speed but do not alter the mathematical result.

RECORDED RESULTS IN THE EXECUTION ENVIRONMENT
---------------------------------------------
Q/R, charged bound 21:
  PASS; 446 straight shapes; 33,053 proper skew shapes;
  331,727 shape-degree comparisons; 8:38.87 wall time;
  1,665,668 KiB peak RSS (about 1.59 GiB).

P, charged bound 17 and monomial length 17:
  PASS; 206 straight shapes; 8,330 proper skew shapes;
  69,703 shape-degree comparisons; 14:29.16 wall time;
  2,877,544 KiB peak RSS (about 2.74 GiB).

Timings are machine- and thread-count-dependent.  The mathematical output is
independent of iteration order, batching, and thread count.

A separate coefficient-only audit over the same shape ranges found maximum
individual coefficients 245 (Q/R) and 224 (P), and maximum sums of coefficients
for one skew shape 2,004 (Q/R) and 1,094 (P).  There is also an a priori bound
on the standard generation: after m labels, a strict shape has at most
floor((sqrt(8m+1)-1)/2) rows and therefore at most twice that number plus one
legal next positions.  Multiplying these bounds through degree 21 gives fewer
than 2.83e17 top-degree paths, and charging every canonical deletion gives
fewer than 6.19e18 total skew records.  With the P marking factor at most 2^17,
the comparison counters are likewise below 2^64.  Thus the completed
historical runs did not rely on unsigned wraparound.  The present source also
aborts on any overflow.
*/

#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include <boost/unordered/unordered_flat_map.hpp>

using u64 = std::uint64_t;
using u32 = std::uint32_t;
using u16 = std::uint16_t;
using u8 = std::uint8_t;
using Shape = u64;
using Mask = u64;
template<class K, class V, class H>
using FastMap = boost::unordered_flat_map<K, V, H>;

namespace {

constexpr unsigned PART_BITS = 6;
constexpr u64 PART_MASK = (u64{1} << PART_BITS) - 1;
constexpr u16 NO_POS = std::numeric_limits<u16>::max();

struct SplitMixHash {
    static u64 mix(u64 x) noexcept {
        x += 0x9e3779b97f4a7c15ULL;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
        return x ^ (x >> 31);
    }
    std::size_t operator()(u64 x) const noexcept {
        static const u64 salt =
            static_cast<u64>(std::chrono::steady_clock::now().time_since_epoch().count());
        return static_cast<std::size_t>(mix(x + salt));
    }
};

inline void hash_combine(u64& seed, u64 value) noexcept {
    seed ^= SplitMixHash::mix(value + 0x9e3779b97f4a7c15ULL + (seed << 6) + (seed >> 2));
}

inline unsigned shape_part(Shape s, unsigned row) noexcept {
    return static_cast<unsigned>((s >> (PART_BITS * row)) & PART_MASK);
}

inline unsigned shape_length(Shape s) noexcept {
    unsigned len = 0;
    while (shape_part(s, len) != 0) ++len;
    return len;
}

inline unsigned shape_size(Shape s) noexcept {
    unsigned total = 0;
    while (s) {
        total += static_cast<unsigned>(s & PART_MASK);
        s >>= PART_BITS;
    }
    return total;
}

inline Shape shape_add_box(Shape s, unsigned row) noexcept {
    return s + (u64{1} << (PART_BITS * row));
}

inline u16 make_pos(unsigned row, unsigned col) noexcept {
    return static_cast<u16>((row << 8) | col);
}
inline unsigned pos_row(u16 p) noexcept { return p >> 8; }
inline unsigned pos_col(u16 p) noexcept { return p & 0xffu; }
inline bool is_diagonal(u16 p) noexcept { return pos_row(p) == pos_col(p); }

bool is_strict_shape(Shape s) noexcept {
    unsigned prev = 64;
    for (unsigned r = 0;; ++r) {
        unsigned p = shape_part(s, r);
        if (!p) break;
        if (p >= prev) return false;
        prev = p;
    }
    return true;
}

Shape canonical_prefix(Shape canonical, unsigned boxes) noexcept {
    Shape result = 0;
    unsigned remaining = boxes;
    for (unsigned r = 0; remaining && shape_part(canonical, r); ++r) {
        unsigned take = std::min(shape_part(canonical, r), remaining);
        result |= static_cast<Shape>(take) << (PART_BITS * r);
        remaining -= take;
    }
    return result;
}

Shape truncate_canonical(Shape canonical, u16 occupied) noexcept {
    const unsigned target_row = pos_row(occupied);
    const unsigned target_col = pos_col(occupied);
    unsigned before = 0;
    for (unsigned r = 0; shape_part(canonical, r); ++r) {
        const unsigned len = shape_part(canonical, r);
        if (r == target_row && target_col >= r && target_col < r + len) {
            before += target_col - r;
            return canonical_prefix(canonical, before);
        }
        before += len;
    }
    return canonical;
}

inline Mask lower_bits(unsigned n) noexcept {
    if (n == 0) return 0;
    if (n >= 64) return ~Mask{0};
    return (Mask{1} << n) - 1;
}

inline Mask shift_mask(Mask mask, unsigned removed, unsigned minimum_index) noexcept {
    Mask shifted = mask >> removed;
    return shifted & ~lower_bits(minimum_index);
}

struct ShapeInfo {
    unsigned len = 0;
    unsigned size = 0;
    std::vector<unsigned> terminal_rows;
    std::vector<u16> terminal_positions;
    std::vector<unsigned> addable_rows;
    std::vector<Shape> added_shapes;
    std::vector<u16> added_positions;
};

class ShapeCache {
    std::unordered_map<Shape, ShapeInfo, SplitMixHash> cache_;
public:
    const ShapeInfo& get(Shape s) {
        auto found = cache_.find(s);
        if (found != cache_.end()) return found->second;
        ShapeInfo info;
        info.len = shape_length(s);
        info.size = shape_size(s);
        for (unsigned r = 0; r < info.len; ++r) {
            const unsigned p = shape_part(s, r);
            if (r + 1 == info.len || p >= shape_part(s, r + 1) + 2) {
                info.terminal_rows.push_back(r);
                info.terminal_positions.push_back(make_pos(r, r + p - 1));
            }
            if (r == 0 || shape_part(s, r - 1) >= p + 2) {
                info.addable_rows.push_back(r);
                info.added_shapes.push_back(shape_add_box(s, r));
                info.added_positions.push_back(make_pos(r, r + p));
            }
        }
        if (info.len == 0 || shape_part(s, info.len - 1) >= 2) {
            const unsigned r = info.len;
            info.addable_rows.push_back(r);
            info.added_shapes.push_back(shape_add_box(s, r));
            info.added_positions.push_back(make_pos(r, r));
        }
        return cache_.emplace(s, std::move(info)).first->second;
    }
};

struct ShapePair {
    Shape outer = 0;
    Shape inner = 0;
    bool operator==(const ShapePair&) const = default;
};
struct ShapePairHash {
    std::size_t operator()(const ShapePair& x) const noexcept {
        u64 h = SplitMixHash::mix(x.outer);
        hash_combine(h, x.inner);
        return static_cast<std::size_t>(h);
    }
};

using Count = u64;

[[noreturn]] inline void count_overflow() noexcept {
    std::fputs("fatal: 64-bit tableau counter overflow\n", stderr);
    std::abort();
}

inline void add_count(Count& target, Count value) noexcept {
#ifndef FAST_UNCHECKED_COUNTS
    if (value > std::numeric_limits<Count>::max() - target) count_overflow();
#endif
    target += value;
}

inline void add_product(Count& target, Count a, Count b) noexcept {
#ifndef FAST_UNCHECKED_COUNTS
    if (a != 0 && b > std::numeric_limits<Count>::max() / a) count_overflow();
#endif
    add_count(target, a * b);
}

using MaskCounter = FastMap<Mask, Count, SplitMixHash>;
using QRDegrees = std::vector<MaskCounter>;
using QRStraight = FastMap<Shape, QRDegrees, SplitMixHash>;
using QRSkew = FastMap<ShapePair, QRDegrees, ShapePairHash>;

struct PSig {
    Mask peaks = 0;
    Mask same = 0;
    Mask diag = 0;
    bool operator==(const PSig&) const = default;
};
struct PSigHash {
    std::size_t operator()(const PSig& x) const noexcept {
        u64 h = SplitMixHash::mix(x.peaks);
        hash_combine(h, x.same);
        hash_combine(h, x.diag);
        return static_cast<std::size_t>(h);
    }
};
using PSigCounter = FastMap<PSig, Count, PSigHash>;
using PDegrees = std::vector<PSigCounter>;
using PStraight = FastMap<Shape, PDegrees, SplitMixHash>;
using PSkew = FastMap<ShapePair, PDegrees, ShapePairHash>;



// -----------------------------------------------------------------------------
// Standard-tableau generation
// -----------------------------------------------------------------------------

struct QRState {
    Shape shape = 0;
    Shape canonical = 0;
    u16 prevprev = NO_POS;
    u16 prev = NO_POS;
    Mask peaks = 0;
    bool operator==(const QRState&) const = default;
};
struct QRStateHash {
    std::size_t operator()(const QRState& x) const noexcept {
        u64 h = SplitMixHash::mix(x.shape);
        hash_combine(h, x.canonical);
        hash_combine(h, static_cast<u64>(x.prevprev) << 16 | x.prev);
        hash_combine(h, x.peaks);
        return static_cast<std::size_t>(h);
    }
};

struct PState {
    Shape shape = 0;
    Shape canonical = 0;
    u16 prevprev = NO_POS;
    u16 prev = NO_POS;
    Mask peaks = 0;
    Mask same = 0;
    Mask diag = 0;
    bool operator==(const PState&) const = default;
};
struct PStateHash {
    std::size_t operator()(const PState& x) const noexcept {
        u64 h = SplitMixHash::mix(x.shape);
        hash_combine(h, x.canonical);
        hash_combine(h, static_cast<u64>(x.prevprev) << 16 | x.prev);
        hash_combine(h, x.peaks);
        hash_combine(h, x.same);
        hash_combine(h, x.diag);
        return static_cast<std::size_t>(h);
    }
};

inline bool canonical_can_extend(Shape shape, unsigned row) noexcept {
    unsigned len = shape_length(shape);
    return row == len || (len != 0 && row + 1 == len);
}

inline Mask qr_peak_update(Mask mask, u16 pp, u16 p, u16 q, unsigned label) noexcept {
    if (label >= 3 && pos_col(pp) < pos_col(p) && pos_row(q) > pos_row(p)) {
        mask |= Mask{1} << (label - 1);
    }
    return mask;
}

inline Mask p_peak_update(Mask mask, u16 pp, u16 p, u16 q, unsigned label) noexcept {
    if (label < 3) return mask;
    const bool left = pp == p || (pp != p && pos_row(p) <= pos_row(pp));
    const bool right = p == q || pos_row(q) > pos_row(p);
    if (left && right) mask |= Mask{1} << (label - 1);
    return mask;
}

template<class Map, class Key>
auto& ensure_degrees(Map& map, const Key& key, unsigned n) {
    auto [it, inserted] = map.try_emplace(key);
    if (inserted) it->second.resize(n + 1);
    return it->second;
}


using QRStateMap = FastMap<QRState, Count, QRStateHash>;

void qr_generation_step(unsigned label, unsigned n, QRStateMap& states, QRStateMap& next,
                        QRStraight& straight, QRSkew& skew, ShapeCache& shapes) {
    next.clear();
    next.reserve(states.size() * 3 + 32);
    for (const auto& [state, multiplicity] : states) {
        const ShapeInfo& info = shapes.get(state.shape);
        for (std::size_t k = 0; k < info.terminal_rows.size(); ++k) {
            const u16 pos = info.terminal_positions[k];
            if (pos == state.prev) continue;
            QRState q;
            q.shape = state.shape;
            q.canonical = truncate_canonical(state.canonical, pos);
            q.prevprev = state.prev;
            q.prev = pos;
            q.peaks = qr_peak_update(state.peaks, state.prevprev, state.prev, pos, label);
            add_count(next[q], multiplicity);
        }
        for (std::size_t k = 0; k < info.addable_rows.size(); ++k) {
            const unsigned row = info.addable_rows[k];
            const Shape new_shape = info.added_shapes[k];
            const u16 pos = info.added_positions[k];
            QRState q;
            q.shape = new_shape;
            q.canonical = state.canonical;
            if (shape_size(state.canonical) == label - 1 && canonical_can_extend(state.shape, row)) {
                q.canonical = new_shape;
            }
            q.prevprev = state.prev;
            q.prev = pos;
            q.peaks = qr_peak_update(state.peaks, state.prevprev, state.prev, pos, label);
            add_count(next[q], multiplicity);
        }
    }
    states.swap(next);
    for (const auto& [state, multiplicity] : states) {
        auto& sd = ensure_degrees(straight, state.shape, n);
        add_count(sd[label][state.peaks], multiplicity);
        const unsigned mmax = shape_size(state.canonical);
        for (unsigned missing = 1; missing <= mmax; ++missing) {
            const unsigned actual = label - missing;
            if (!actual) continue;
            const Shape inner = canonical_prefix(state.canonical, missing);
            auto& kd = ensure_degrees(skew, ShapePair{state.shape, inner}, n);
            const Mask peaks = shift_mask(state.peaks, missing, 2);
            add_count(kd[actual][peaks], multiplicity);
        }
    }
}


void qr_record_state(const QRState& state, Count multiplicity, unsigned label, unsigned n,
                     QRStraight& straight, QRSkew& skew) {
    auto& sd = ensure_degrees(straight, state.shape, n);
    add_count(sd[label][state.peaks], multiplicity);
    const unsigned mmax = shape_size(state.canonical);
    for (unsigned missing = 1; missing <= mmax; ++missing) {
        const unsigned actual = label - missing;
        if (!actual) continue;
        const Shape inner = canonical_prefix(state.canonical, missing);
        auto& kd = ensure_degrees(skew, ShapePair{state.shape, inner}, n);
        const Mask peaks = shift_mask(state.peaks, missing, 2);
        add_count(kd[actual][peaks], multiplicity);
    }
}

std::pair<Count,std::size_t> qr_generation_final(unsigned label, unsigned n,
                        const QRStateMap& states, QRStraight& straight, QRSkew& skew,
                        ShapeCache& shapes) {
    Count tableaux = 0;
    std::size_t records = 0;
    for (const auto& [state, multiplicity] : states) {
        const ShapeInfo& info = shapes.get(state.shape);
        for (std::size_t k = 0; k < info.terminal_rows.size(); ++k) {
            const u16 pos = info.terminal_positions[k];
            if (pos == state.prev) continue;
            QRState q;
            q.shape = state.shape;
            q.canonical = truncate_canonical(state.canonical, pos);
            q.prevprev = state.prev;
            q.prev = pos;
            q.peaks = qr_peak_update(state.peaks, state.prevprev, state.prev, pos, label);
            qr_record_state(q, multiplicity, label, n, straight, skew);
            add_count(tableaux, multiplicity);
            ++records;
        }
        for (std::size_t k = 0; k < info.addable_rows.size(); ++k) {
            const unsigned row = info.addable_rows[k];
            const Shape new_shape = info.added_shapes[k];
            const u16 pos = info.added_positions[k];
            QRState q;
            q.shape = new_shape;
            q.canonical = state.canonical;
            if (shape_size(state.canonical) == label - 1 && canonical_can_extend(state.shape, row))
                q.canonical = new_shape;
            q.prevprev = state.prev;
            q.prev = pos;
            q.peaks = qr_peak_update(state.peaks, state.prevprev, state.prev, pos, label);
            qr_record_state(q, multiplicity, label, n, straight, skew);
            add_count(tableaux, multiplicity);
            ++records;
        }
    }
    return {tableaux, records};
}

void merge_qr_straight(QRStraight& dest, const QRStraight& src, unsigned n) {
    for (const auto& [shape, degrees] : src) {
        auto& out = ensure_degrees(dest, shape, n);
        for (unsigned d = 1; d < degrees.size(); ++d)
            for (const auto& [mask, count] : degrees[d]) add_count(out[d][mask], count);
    }
}
void merge_qr_skew(QRSkew& dest, const QRSkew& src, unsigned n) {
    for (const auto& [shape, degrees] : src) {
        auto& out = ensure_degrees(dest, shape, n);
        for (unsigned d = 1; d < degrees.size(); ++d)
            for (const auto& [mask, count] : degrees[d]) add_count(out[d][mask], count);
    }
}

struct QRBatchedGeneration {
    QRStraight straight;
    QRSkew skew;
    Count top_tableaux = 0;
    std::size_t top_state_records = 0;
    unsigned split = 0;
    std::size_t batches = 0;
};

QRBatchedGeneration generate_qr_batched(unsigned n, bool progress) {
    QRBatchedGeneration result;
    result.split = std::min(n, 19u);
    ShapeCache shapes;
    QRStateMap states, next;
    states.reserve(4096);
    states.emplace(QRState{}, 1);

    for (unsigned label = 1; label <= result.split; ++label) {
        qr_generation_step(label, n, states, next, result.straight, result.skew, shapes);
        if (progress) {
            Count total = 0;
            for (const auto& [_, count] : states) add_count(total, count);
            std::cerr << "[Q/R] generated n=" << label << ": " << total
                      << " tableaux, " << states.size() << " states, "
                      << result.skew.size() << " skew shapes\n";
        }
    }

    if (n == result.split) {
        result.batches = 1;
        result.top_state_records = states.size();
        for (const auto& [_, count] : states) add_count(result.top_tableaux, count);
        return result;
    }

    std::vector<std::pair<QRState, Count>> seeds;
    seeds.reserve(states.size());
    for (const auto& item : states) seeds.push_back(item);
    QRStateMap{}.swap(states);
    QRStateMap{}.swap(next);

    std::size_t batch_size = (n >= 21 ? 500000 : 50000);
    if (const char* env = std::getenv("QR_BATCH_SIZE")) {
        const unsigned long long parsed = std::strtoull(env, nullptr, 10);
        if (parsed) batch_size = static_cast<std::size_t>(parsed);
    }
    result.batches = (seeds.size() + batch_size - 1) / batch_size;

    for (std::size_t begin = 0, batch = 0; begin < seeds.size(); begin += batch_size, ++batch) {
        const std::size_t end = std::min(seeds.size(), begin + batch_size);
        QRStateMap batch_states, batch_next;
        batch_states.reserve((end - begin) * 2 + 32);
        for (std::size_t i = begin; i < end; ++i)
            batch_states.emplace(seeds[i].first, seeds[i].second);
        QRStraight local_straight;
        QRSkew local_skew;
        for (unsigned label = result.split + 1; label < n; ++label)
            qr_generation_step(label, n, batch_states, batch_next,
                               local_straight, local_skew, shapes);
        const auto [batch_tableaux, batch_records] =
            qr_generation_final(n, n, batch_states, local_straight, local_skew, shapes);
        if (batch_records > std::numeric_limits<std::size_t>::max() - result.top_state_records)
            throw std::runtime_error("top-state record counter overflow");
        result.top_state_records += batch_records;
        add_count(result.top_tableaux, batch_tableaux);
        merge_qr_straight(result.straight, local_straight, n);
        merge_qr_skew(result.skew, local_skew, n);
        if (progress) {
            std::cerr << "[Q/R] completed batch " << (batch + 1) << '/' << result.batches
                      << " (" << (end - begin) << " seed states, "
                      << batch_records << " final transition records)\n";
        }
    }
    return result;
}


// -----------------------------------------------------------------------------
// Highest-weight coefficients
// -----------------------------------------------------------------------------

struct Cell {
    u16 symbols = 0; // bit e-1 means encoded symbol e is present
    u8 minimum = 0;
    u8 maximum = 0;
};
struct RowChoice {
    std::vector<Cell> cells;
    std::vector<u8> reading;
};

struct RowKey {
    u8 length = 0;
    u8 maximum_value = 0;
    u8 max_entries = 0;
    bool diagonal_primed = false;
    bool operator==(const RowKey&) const = default;
};
struct RowKeyHash {
    std::size_t operator()(const RowKey& k) const noexcept {
        return (k.length << 17) ^ (k.maximum_value << 9) ^
               (k.max_entries << 1) ^ k.diagonal_primed;
    }
};

class RowCache {
    std::unordered_map<RowKey, std::vector<RowChoice>, RowKeyHash> cache_;

    static Cell make_cell(u16 subset) {
        Cell c;
        c.symbols = subset;
        c.minimum = static_cast<u8>(std::countr_zero(static_cast<unsigned>(subset)) + 1);
        c.maximum = static_cast<u8>(std::bit_width(static_cast<unsigned>(subset)));
        return c;
    }

    static std::vector<u8> cell_reading(u16 subset, unsigned m) {
        std::vector<u8> out;
        for (unsigned value = 1; value <= m; ++value) {
            unsigned e = 2 * value;
            if (subset & (u16{1} << (e - 1))) out.push_back(static_cast<u8>(e));
        }
        for (unsigned value = m; value >= 1; --value) {
            unsigned e = 2 * value - 1;
            if (subset & (u16{1} << (e - 1))) out.push_back(static_cast<u8>(e));
            if (value == 1) break;
        }
        return out;
    }

    static void generate_rec(unsigned target_len, unsigned m, bool diag,
                             unsigned max_entries, unsigned entry_count,
                             std::vector<Cell>& cells, std::vector<RowChoice>& out) {
        if (cells.size() == target_len) {
            RowChoice row;
            row.cells = cells;
            for (const Cell& c : cells) {
                auto piece = cell_reading(c.symbols, m);
                row.reading.insert(row.reading.end(), piece.begin(), piece.end());
            }
            out.push_back(std::move(row));
            return;
        }
        const unsigned max_symbol = 2 * m;
        unsigned start = 1;
        if (!cells.empty()) {
            start = cells.back().maximum;
            if (start & 1u) ++start; // primed values cannot repeat in a row
        }
        if (start > max_symbol) return;
        u16 available = 0;
        for (unsigned e = start; e <= max_symbol; ++e) available |= u16{1} << (e - 1);
        for (u16 subset = available; subset; subset = (subset - 1) & available) {
            if (diag && cells.empty()) {
                bool has_unprimed = false;
                for (unsigned e = 2; e <= max_symbol; e += 2) {
                    if (subset & (u16{1} << (e - 1))) { has_unprimed = true; break; }
                }
                if (has_unprimed) continue;
            }
            const unsigned added = std::popcount(static_cast<unsigned>(subset));
            const unsigned next_count = entry_count + added;
            const unsigned remaining_cells = target_len - (cells.size() + 1);
            if (next_count + remaining_cells > max_entries) continue;
            cells.push_back(make_cell(subset));
            generate_rec(target_len, m, diag, max_entries, next_count, cells, out);
            cells.pop_back();
        }
    }

public:
    const std::vector<RowChoice>& get(unsigned length, unsigned maximum_value,
                                      bool diagonal_primed, unsigned max_entries) {
        RowKey key{static_cast<u8>(length), static_cast<u8>(maximum_value),
                   static_cast<u8>(max_entries), diagonal_primed};
        auto found = cache_.find(key);
        if (found != cache_.end()) return found->second;
        std::vector<RowChoice> rows;
        std::vector<Cell> cells;
        generate_rec(length, maximum_value, diagonal_primed,
                     max_entries, 0, cells, rows);
        return cache_.emplace(key, std::move(rows)).first->second;
    }
};

bool rows_compatible(const RowChoice& top, unsigned top_skew,
                     const RowChoice& bottom, unsigned bottom_skew) noexcept {
    if (top_skew + top.cells.size() < 1 + bottom_skew + bottom.cells.size()) return false;
    for (unsigned i = 0; i < top.cells.size(); ++i) {
        int bottom_i = static_cast<int>(top_skew + i) - static_cast<int>(bottom_skew + 1);
        if (bottom_i >= 0 && bottom_i < static_cast<int>(bottom.cells.size())) {
            const u8 t = top.cells[i].maximum;
            const u8 b = bottom.cells[bottom_i].minimum;
            if (t > b || (t == b && (t % 2 == 0))) return false;
        }
    }
    return true;
}

bool has_primed_property(const std::vector<u8>& word) noexcept {
    u64 seen = 0;
    for (u8 encoded : word) {
        unsigned value = (encoded + 1) / 2;
        Mask bit = Mask{1} << value;
        if (!(seen & bit)) {
            if ((encoded & 1u) == 0) return false;
            seen |= bit;
        }
    }
    return true;
}

bool has_lattice_property(const std::vector<u8>& word) noexcept {
    if (word.empty()) return true;
    unsigned largest = 0;
    for (u8 e : word) largest = std::max(largest, static_cast<unsigned>((e + 1) / 2));
    std::array<unsigned, 16> counts{};
    for (auto it = word.rbegin(); it != word.rend(); ++it) {
        unsigned e = *it;
        unsigned value = (e + 1) / 2;
        if ((e & 1u) == 0) {
            ++counts[value];
            if (value > 1 && counts[value] > counts[value - 1]) return false;
        } else if (value > 1 && counts[value] == counts[value - 1]) {
            return false;
        }
    }
    for (u8 e : word) {
        unsigned value = (e + 1) / 2;
        if (e & 1u) {
            ++counts[value];
            if (value > 1 && counts[value] > counts[value - 1]) return false;
        } else if (counts[value + 1] == counts[value]) {
            return false;
        }
    }
    return true;
}

Shape word_weight(const std::vector<u8>& word) {
    std::array<unsigned, 10> counts{};
    unsigned largest = 0;
    for (u8 e : word) {
        unsigned value = (e + 1) / 2;
        largest = std::max(largest, value);
        ++counts[value - 1];
    }
    Shape result = 0;
    for (unsigned i = 0; i < largest; ++i) {
        if (counts[i] > PART_MASK) throw std::runtime_error("weight part too large");
        result |= static_cast<Shape>(counts[i]) << (PART_BITS * i);
    }
    return result;
}

using Coefficients = std::vector<std::pair<Shape, Count>>;

struct CoeffKey {
    ShapePair shape;
    bool p = false;
    u8 max_entries = 0;
    bool operator==(const CoeffKey&) const = default;
};
struct CoeffKeyHash {
    std::size_t operator()(const CoeffKey& k) const noexcept {
        u64 h = ShapePairHash{}(k.shape);
        hash_combine(h, k.p);
        hash_combine(h, k.max_entries);
        return static_cast<std::size_t>(h);
    }
};

class CoefficientCache {
    RowCache rows_;
    std::unordered_map<CoeffKey, Coefficients, CoeffKeyHash> cache_;

    static bool extend_backward_lattice(const RowChoice& row,
                                        std::array<unsigned, 16>& counts) noexcept {
        for (auto it = row.reading.rbegin(); it != row.reading.rend(); ++it) {
            const unsigned e = *it;
            const unsigned value = (e + 1) / 2;
            if ((e & 1u) == 0) {
                ++counts[value];
                if (value > 1 && counts[value] > counts[value - 1]) return false;
            } else if (value > 1 && counts[value] == counts[value - 1]) {
                return false;
            }
        }
        return true;
    }

    void enumerate_rec(unsigned row_index,
                       const std::vector<const std::vector<RowChoice>*>& choices,
                       const std::vector<unsigned>& skews,
                       std::vector<const RowChoice*>& selected,
                       const std::array<unsigned, 16>& backward_counts,
                       unsigned entry_count,
                       unsigned max_entries,
                       bool require_primed,
                       std::unordered_map<Shape, Count, SplitMixHash>& counts) {
        if (row_index == choices.size()) {
            std::vector<u8> word;
            std::size_t reserve = 0;
            for (const RowChoice* r : selected) reserve += r->reading.size();
            word.reserve(reserve);
            for (std::size_t r = selected.size(); r-- > 0;) {
                word.insert(word.end(), selected[r]->reading.begin(), selected[r]->reading.end());
            }
            if (require_primed && !has_primed_property(word)) return;
            if (!has_lattice_property(word)) return;
            Shape weight = word_weight(word);
            if (weight && !is_strict_shape(weight)) {
                throw std::runtime_error("non-strict highest weight");
            }
            add_count(counts[weight], 1);
            return;
        }
        for (const RowChoice& candidate : *choices[row_index]) {
            if (row_index && !rows_compatible(*selected.back(), skews[row_index - 1],
                                               candidate, skews[row_index])) {
                continue;
            }
            const unsigned next_entry_count = entry_count + candidate.reading.size();
            if (next_entry_count > max_entries) continue;
            auto next_counts = backward_counts;
            if (!extend_backward_lattice(candidate, next_counts)) continue;
            selected.push_back(&candidate);
            enumerate_rec(row_index + 1, choices, skews, selected, next_counts,
                          next_entry_count, max_entries, require_primed, counts);
            selected.pop_back();
        }
    }

    static void strict_targets_rec(unsigned remaining, unsigned max_part,
                                   unsigned max_length, unsigned depth,
                                   Shape prefix, std::vector<Shape>& out) {
        if (remaining == 0) {
            if (prefix) out.push_back(prefix);
            return;
        }
        if (depth == max_length || max_part == 0) return;
        const unsigned upper = std::min(remaining, max_part);
        for (unsigned part = upper; part >= 1; --part) {
            const Shape next = prefix | (static_cast<Shape>(part) << (PART_BITS * depth));
            strict_targets_rec(remaining - part, part - 1, max_length,
                               depth + 1, next, out);
            if (part == 1) break;
        }
    }

    static std::vector<Shape> strict_targets(unsigned minimum_size,
                                             unsigned maximum_size,
                                             unsigned max_length) {
        std::vector<Shape> out;
        for (unsigned size = minimum_size; size <= maximum_size; ++size)
            strict_targets_rec(size, size, max_length, 0, 0, out);
        return out;
    }

    static bool extend_qr_target(const RowChoice& row, Shape target,
                                 std::array<unsigned, 16>& unprimed,
                                 std::array<unsigned, 16>& prime_after,
                                 std::array<unsigned, 16>& seen) noexcept {
        for (auto it = row.reading.rbegin(); it != row.reading.rend(); ++it) {
            const unsigned e = *it;
            const unsigned value = (e + 1) / 2;
            const unsigned target_value = shape_part(target, value - 1);
            if (++seen[value] > target_value) return false;

            if ((e & 1u) == 0) {
                ++unprimed[value];
                if (value > 1 && unprimed[value] > unprimed[value - 1]) return false;

                // This is the forward-pass tie test at an unprimed value.
                const unsigned current = target_value - prime_after[value];
                const unsigned upper = shape_part(target, value) - prime_after[value + 1];
                if (current == upper) return false;
            } else {
                // This is the backward-pass tie test at a primed value.
                if (value > 1 && unprimed[value] == unprimed[value - 1]) return false;

                // In the forward pass the current prime has just been counted.
                if (value > 1) {
                    const unsigned current = target_value - prime_after[value];
                    const unsigned lower = shape_part(target, value - 2) - prime_after[value - 1];
                    if (current > lower) return false;
                }
                ++prime_after[value];
            }

            // The last occurrence in the reverse scan is the first occurrence
            // in the ordinary reading word, and must be primed.
            if (seen[value] == target_value && (e & 1u) == 0) return false;
        }
        return true;
    }

    void enumerate_qr_target_rec(
            unsigned row_index,
            const std::vector<const std::vector<RowChoice>*>& choices,
            const std::vector<unsigned>& skews,
            const std::vector<unsigned>& remaining_boxes,
            std::vector<const RowChoice*>& selected,
            Shape target, unsigned target_size, unsigned entry_count,
            const std::array<unsigned, 16>& unprimed,
            const std::array<unsigned, 16>& prime_after,
            const std::array<unsigned, 16>& seen,
            Count& count) {
        if (row_index == choices.size()) {
            if (entry_count == target_size) add_count(count, 1);
            return;
        }
        for (const RowChoice& candidate : *choices[row_index]) {
            if (row_index && !rows_compatible(*selected.back(), skews[row_index - 1],
                                               candidate, skews[row_index])) {
                continue;
            }
            const unsigned next_entry_count = entry_count + candidate.reading.size();
            if (next_entry_count > target_size) continue;
            if (next_entry_count + remaining_boxes[row_index + 1] > target_size) continue;
            auto next_unprimed = unprimed;
            auto next_prime_after = prime_after;
            auto next_seen = seen;
            if (!extend_qr_target(candidate, target, next_unprimed,
                                  next_prime_after, next_seen)) continue;
            selected.push_back(&candidate);
            enumerate_qr_target_rec(row_index + 1, choices, skews, remaining_boxes,
                                    selected, target, target_size, next_entry_count,
                                    next_unprimed, next_prime_after, next_seen, count);
            selected.pop_back();
        }
    }

public:
    const Coefficients& get(Shape outer, Shape inner, bool p, unsigned max_entries) {
        CoeffKey key{{outer, inner}, p, static_cast<u8>(max_entries)};
        auto found = cache_.find(key);
        if (found != cache_.end()) return found->second;
        const unsigned len = shape_length(outer);
        std::vector<const std::vector<RowChoice>*> choices;
        std::vector<unsigned> skews;
        choices.reserve(len);
        skews.reserve(len);
        for (unsigned r = 0; r < len; ++r) {
            unsigned in = shape_part(inner, r);
            unsigned out = shape_part(outer, r);
            bool diag = p && in == 0;
            choices.push_back(&rows_.get(out - in, r + 1, diag, max_entries));
            skews.push_back(in);
        }
        Coefficients result;
        if (!p) {
            const unsigned boxes = shape_size(outer) - shape_size(inner);
            std::vector<unsigned> remaining_boxes(len + 1, 0);
            for (unsigned r = len; r-- > 0;)
                remaining_boxes[r] = remaining_boxes[r + 1] +
                                     shape_part(outer, r) - shape_part(inner, r);
            const auto targets = strict_targets(boxes, max_entries, len);
            result.reserve(targets.size());
            for (Shape target : targets) {
                const unsigned target_size = shape_size(target);
                std::vector<const RowChoice*> selected;
                std::array<unsigned, 16> unprimed{};
                std::array<unsigned, 16> prime_after{};
                std::array<unsigned, 16> seen{};
                Count count = 0;
                enumerate_qr_target_rec(0, choices, skews, remaining_boxes,
                                        selected, target, target_size, 0,
                                        unprimed, prime_after, seen, count);
                if (count) result.emplace_back(target, count);
            }
        } else {
            std::unordered_map<Shape, Count, SplitMixHash> counts;
            std::vector<const RowChoice*> selected;
            std::array<unsigned, 16> backward_counts{};
            enumerate_rec(0, choices, skews, selected, backward_counts,
                          0, max_entries, false, counts);
            result.reserve(counts.size());
            for (const auto& pair : counts) result.push_back(pair);
            std::sort(result.begin(), result.end(),
                      [](auto a, auto b) { return a.first < b.first; });
        }
        return cache_.emplace(key, std::move(result)).first->second;
    }
};

// -----------------------------------------------------------------------------
// P dominant-monomial transform
// -----------------------------------------------------------------------------

struct PartitionInfo {
    Shape code = 0;
    Mask boundary = 0;
    Mask ends = 0;
    struct Part { Mask labels = 0; Mask internal_pair_starts = 0; };
    std::vector<Part> parts;
};

class PartitionCache {
    std::map<std::pair<unsigned, unsigned>, std::vector<PartitionInfo>> cache_;

    static void generate_vectors(unsigned remaining, unsigned largest, unsigned max_length,
                                 std::vector<unsigned>& prefix,
                                 std::vector<std::vector<unsigned>>& out) {
        if (remaining == 0) { out.push_back(prefix); return; }
        if (prefix.size() == max_length) return;
        for (unsigned p = std::min(largest, remaining); p >= 1; --p) {
            prefix.push_back(p);
            generate_vectors(remaining - p, p, max_length, prefix, out);
            prefix.pop_back();
            if (p == 1) break;
        }
    }

public:
    const std::vector<PartitionInfo>& get(unsigned n, unsigned max_length) {
        auto key = std::make_pair(n, max_length);
        auto found = cache_.find(key);
        if (found != cache_.end()) return found->second;
        std::vector<std::vector<unsigned>> vectors;
        std::vector<unsigned> prefix;
        generate_vectors(n, n, max_length, prefix, vectors);
        std::vector<PartitionInfo> infos;
        infos.reserve(vectors.size());
        for (const auto& parts : vectors) {
            PartitionInfo info;
            unsigned start = 1;
            for (unsigned i = 0; i < parts.size(); ++i) {
                info.code |= static_cast<Shape>(parts[i]) << (PART_BITS * i);
                unsigned end = start + parts[i] - 1;
                info.boundary |= Mask{1} << start;
                info.boundary |= Mask{1} << end;
                info.ends |= Mask{1} << end;
                Mask labels = (lower_bits(end + 1) ^ lower_bits(start));
                Mask pairs = start < end ? (lower_bits(end) ^ lower_bits(start)) : 0;
                info.parts.push_back({labels, pairs});
                start = end + 1;
            }
            infos.push_back(std::move(info));
        }
        return cache_.emplace(key, std::move(infos)).first->second;
    }
};


class PTransform {
    PartitionCache partitions_;
public:
    std::vector<Count> transform(unsigned n, unsigned max_length,
                                 const PSigCounter& signatures) {
        const auto& parts = partitions_.get(n, max_length);
        std::vector<Count> result(parts.size(), 0);
        for (const auto& [sig, multiplicity] : signatures) {
            const Mask diagonal_double = sig.same & sig.diag;
            for (std::size_t index = 0; index < parts.size(); ++index) {
                const PartitionInfo& partition = parts[index];
                if (sig.peaks & ~partition.boundary) continue;
                if (diagonal_double & ~partition.ends) continue;

                unsigned free_parts = 0;
                for (const auto& part : partition.parts) {
                    if (part.labels & sig.diag) continue;
                    if (part.internal_pair_starts & sig.same) continue;
                    ++free_parts;
                }
                const Count marking_multiplicity = Count{1} << free_parts;
                add_product(result[index], multiplicity, marking_multiplicity);
            }
        }
        return result;
    }

    std::size_t dimension(unsigned n, unsigned max_length) {
        return partitions_.get(n, max_length).size();
    }
};

using MonoDegrees = std::vector<std::vector<Count>>;
using PMonoStraight = FastMap<Shape, MonoDegrees, SplitMixHash>;
using PMonoSkew = FastMap<ShapePair, MonoDegrees, ShapePairHash>;
using PStateMap = FastMap<PState, Count, PStateHash>;

void add_mono_vector(std::vector<Count>& target, const std::vector<Count>& source) {
    if (target.empty()) target.assign(source.size(), 0);
    if (target.size() != source.size()) throw std::runtime_error("monomial dimension mismatch");
    for (std::size_t i = 0; i < source.size(); ++i) add_count(target[i], source[i]);
}

void transform_p_signatures(const PStraight& local_straight, const PSkew& local_skew,
                            PMonoStraight& straight_mono, PMonoSkew& skew_mono,
                            unsigned n, unsigned num_vars,
                            Count& straight_total, Count& skew_total) {
    PTransform transform;
    for (const auto& [shape, degrees] : local_straight) {
        auto& target = ensure_degrees(straight_mono, shape, n);
        for (unsigned d = 1; d < degrees.size(); ++d) {
            if (degrees[d].empty()) continue;
            for (const auto& [_, count] : degrees[d]) add_count(straight_total, count);
            auto mono = transform.transform(d, std::min(num_vars, d), degrees[d]);
            add_mono_vector(target[d], mono);
        }
    }
    for (const auto& [pair, degrees] : local_skew) {
        auto& target = ensure_degrees(skew_mono, pair, n);
        for (unsigned d = 1; d < degrees.size(); ++d) {
            if (degrees[d].empty()) continue;
            for (const auto& [_, count] : degrees[d]) add_count(skew_total, count);
            auto mono = transform.transform(d, std::min(num_vars, d), degrees[d]);
            add_mono_vector(target[d], mono);
        }
    }
}

void p_generation_step(unsigned label, unsigned n,
                       PStateMap& states, PStateMap& next,
                       PStraight& straight, PSkew& skew,
                       ShapeCache& shapes) {
    next.clear();
    next.reserve(states.size() * 3 + 32);
    for (const auto& [state, multiplicity] : states) {
        const ShapeInfo& info = shapes.get(state.shape);
        for (std::size_t k = 0; k < info.terminal_rows.size(); ++k) {
            const u16 pos = info.terminal_positions[k];
            PState q;
            q.shape = state.shape;
            q.canonical = truncate_canonical(state.canonical, pos);
            q.prevprev = state.prev;
            q.prev = pos;
            q.peaks = p_peak_update(state.peaks, state.prevprev, state.prev, pos, label);
            q.same = state.same;
            if (label >= 2 && state.prev == pos) q.same |= Mask{1} << (label - 1);
            q.diag = state.diag;
            if (is_diagonal(pos)) q.diag |= Mask{1} << label;
            add_count(next[q], multiplicity);
        }
        for (std::size_t k = 0; k < info.addable_rows.size(); ++k) {
            const unsigned row = info.addable_rows[k];
            const Shape new_shape = info.added_shapes[k];
            const u16 pos = info.added_positions[k];
            PState q;
            q.shape = new_shape;
            q.canonical = state.canonical;
            if (shape_size(state.canonical) == label - 1 && canonical_can_extend(state.shape, row))
                q.canonical = new_shape;
            q.prevprev = state.prev;
            q.prev = pos;
            q.peaks = p_peak_update(state.peaks, state.prevprev, state.prev, pos, label);
            q.same = state.same;
            if (label >= 2 && state.prev == pos) q.same |= Mask{1} << (label - 1);
            q.diag = state.diag;
            if (is_diagonal(pos)) q.diag |= Mask{1} << label;
            add_count(next[q], multiplicity);
        }
    }
    states.swap(next);

    for (const auto& [state, multiplicity] : states) {
        PSig sig{state.peaks, state.same, state.diag};
        auto& sd = ensure_degrees(straight, state.shape, n);
        add_count(sd[label][sig], multiplicity);
        const unsigned mmax = shape_size(state.canonical);
        for (unsigned missing = 1; missing <= mmax; ++missing) {
            const unsigned actual = label - missing;
            if (!actual) continue;
            const Shape inner = canonical_prefix(state.canonical, missing);
            PSig shifted{
                shift_mask(state.peaks, missing, 2),
                shift_mask(state.same, missing, 1),
                shift_mask(state.diag, missing, 1)
            };
            auto& kd = ensure_degrees(skew, ShapePair{state.shape, inner}, n);
            add_count(kd[actual][shifted], multiplicity);
        }
    }
}


void p_record_state(const PState& state, Count multiplicity, unsigned label, unsigned n,
                    PStraight& straight, PSkew& skew) {
    PSig sig{state.peaks, state.same, state.diag};
    auto& sd = ensure_degrees(straight, state.shape, n);
    add_count(sd[label][sig], multiplicity);
    const unsigned mmax = shape_size(state.canonical);
    for (unsigned missing = 1; missing <= mmax; ++missing) {
        const unsigned actual = label - missing;
        if (!actual) continue;
        const Shape inner = canonical_prefix(state.canonical, missing);
        PSig shifted{
            shift_mask(state.peaks, missing, 2),
            shift_mask(state.same, missing, 1),
            shift_mask(state.diag, missing, 1)
        };
        auto& kd = ensure_degrees(skew, ShapePair{state.shape, inner}, n);
        add_count(kd[actual][shifted], multiplicity);
    }
}

std::pair<Count,std::size_t> p_generation_final(unsigned label, unsigned n,
                        const PStateMap& states, PStraight& straight, PSkew& skew,
                        ShapeCache& shapes) {
    Count tableaux = 0;
    PStateMap outputs;
    outputs.reserve(states.size() * 4 + 32);
    for (const auto& [state, multiplicity] : states) {
        const ShapeInfo& info = shapes.get(state.shape);
        for (std::size_t k = 0; k < info.terminal_rows.size(); ++k) {
            const u16 pos = info.terminal_positions[k];
            PState q;
            q.shape = state.shape;
            q.canonical = truncate_canonical(state.canonical, pos);
            q.prevprev = NO_POS;
            q.prev = NO_POS;
            q.peaks = p_peak_update(state.peaks, state.prevprev, state.prev, pos, label);
            q.same = state.same;
            if (label >= 2 && state.prev == pos) q.same |= Mask{1} << (label - 1);
            q.diag = state.diag;
            if (is_diagonal(pos)) q.diag |= Mask{1} << label;
            add_count(outputs[q], multiplicity);
            add_count(tableaux, multiplicity);
        }
        for (std::size_t k = 0; k < info.addable_rows.size(); ++k) {
            const unsigned row = info.addable_rows[k];
            const Shape new_shape = info.added_shapes[k];
            const u16 pos = info.added_positions[k];
            PState q;
            q.shape = new_shape;
            q.canonical = state.canonical;
            if (shape_size(state.canonical) == label - 1 && canonical_can_extend(state.shape, row))
                q.canonical = new_shape;
            q.prevprev = NO_POS;
            q.prev = NO_POS;
            q.peaks = p_peak_update(state.peaks, state.prevprev, state.prev, pos, label);
            q.same = state.same;
            if (label >= 2 && state.prev == pos) q.same |= Mask{1} << (label - 1);
            q.diag = state.diag;
            if (is_diagonal(pos)) q.diag |= Mask{1} << label;
            add_count(outputs[q], multiplicity);
            add_count(tableaux, multiplicity);
        }
    }
    for (const auto& [state, multiplicity] : outputs)
        p_record_state(state, multiplicity, label, n, straight, skew);
    return {tableaux, outputs.size()};
}

void merge_p_mono_straight(PMonoStraight& dest, const PMonoStraight& src, unsigned n) {
    for (const auto& [shape, degrees] : src) {
        auto& out = ensure_degrees(dest, shape, n);
        for (unsigned d = 1; d < degrees.size(); ++d)
            if (!degrees[d].empty()) add_mono_vector(out[d], degrees[d]);
    }
}
void merge_p_mono_skew(PMonoSkew& dest, const PMonoSkew& src, unsigned n) {
    for (const auto& [shape, degrees] : src) {
        auto& out = ensure_degrees(dest, shape, n);
        for (unsigned d = 1; d < degrees.size(); ++d)
            if (!degrees[d].empty()) add_mono_vector(out[d], degrees[d]);
    }
}

struct PBatchedGeneration {
    PMonoStraight straight;
    PMonoSkew skew;
    Count straight_total = 0;
    Count skew_total = 0;
    Count top_tableaux = 0;
    std::size_t top_state_records = 0;
    unsigned split = 0;
    std::size_t batches = 0;
};

PBatchedGeneration generate_p_batched(unsigned n, unsigned num_vars, bool progress) {
    PBatchedGeneration result;
    result.split = std::min(n, 13u);
    ShapeCache shapes;
    PStateMap states, next;
    states.reserve(65536);
    states.emplace(PState{}, 1);
    PStraight initial_straight;
    PSkew initial_skew;

    for (unsigned label = 1; label <= result.split; ++label) {
        p_generation_step(label, n, states, next, initial_straight, initial_skew, shapes);
        if (progress) {
            Count total = 0;
            for (const auto& [_, count] : states) add_count(total, count);
            std::cerr << "[P] generated n=" << label << ": " << total
                      << " tableaux, " << states.size() << " states, "
                      << initial_skew.size() << " skew shapes\n";
        }
    }

    transform_p_signatures(initial_straight, initial_skew, result.straight, result.skew,
                           n, num_vars, result.straight_total, result.skew_total);
    initial_straight.clear();
    initial_skew.clear();

    if (n == result.split) {
        result.batches = 1;
        result.top_state_records = states.size();
        for (const auto& [_, count] : states) add_count(result.top_tableaux, count);
        return result;
    }

    std::vector<std::pair<PState, Count>> seeds;
    seeds.reserve(states.size());
    for (const auto& item : states) seeds.push_back(item);
    PStateMap{}.swap(states);
    PStateMap{}.swap(next);

    std::size_t batch_size = (n >= 17 ? 1000 : 25000);
    if (const char* env = std::getenv("P_BATCH_SIZE")) {
        const unsigned long long parsed = std::strtoull(env, nullptr, 10);
        if (parsed) batch_size = static_cast<std::size_t>(parsed);
    }
    result.batches = (seeds.size() + batch_size - 1) / batch_size;

    std::vector<Count> batch_top_tableaux(result.batches, 0);
    std::vector<std::size_t> batch_top_records(result.batches, 0);
    std::vector<Count> batch_straight_totals(result.batches, 0);
    std::vector<Count> batch_skew_totals(result.batches, 0);

    #pragma omp parallel for schedule(dynamic,1)
    for (std::int64_t batch = 0; batch < static_cast<std::int64_t>(result.batches); ++batch) {
        const std::size_t begin = static_cast<std::size_t>(batch) * batch_size;
        const std::size_t end = std::min(seeds.size(), begin + batch_size);
        ShapeCache local_shapes;
        PStateMap batch_states, batch_next;
        batch_states.reserve((end - begin) * 2 + 32);
        for (std::size_t i = begin; i < end; ++i)
            batch_states.emplace(seeds[i].first, seeds[i].second);
        PStraight local_straight;
        PSkew local_skew;

        for (unsigned label = result.split + 1; label < n; ++label)
            p_generation_step(label, n, batch_states, batch_next,
                              local_straight, local_skew, local_shapes);
        const auto [batch_tableaux, batch_records] =
            p_generation_final(n, n, batch_states, local_straight, local_skew, local_shapes);
        batch_top_tableaux[batch] = batch_tableaux;
        batch_top_records[batch] = batch_records;

        PMonoStraight local_mono_straight;
        PMonoSkew local_mono_skew;
        Count local_straight_total = 0, local_skew_total = 0;
        transform_p_signatures(local_straight, local_skew,
                               local_mono_straight, local_mono_skew,
                               n, num_vars, local_straight_total, local_skew_total);
        batch_straight_totals[batch] = local_straight_total;
        batch_skew_totals[batch] = local_skew_total;

        #pragma omp critical(p_mono_merge)
        {
            merge_p_mono_straight(result.straight, local_mono_straight, n);
            merge_p_mono_skew(result.skew, local_mono_skew, n);
            if (progress) {
                std::cerr << "[P] completed batch " << (batch + 1) << '/' << result.batches
                          << " (" << (end - begin) << " seed states, "
                          << batch_records << " final transition records)\n";
            }
        }
    }
    for (std::size_t batch = 0; batch < result.batches; ++batch) {
        add_count(result.top_tableaux, batch_top_tableaux[batch]);
        if (batch_top_records[batch] > std::numeric_limits<std::size_t>::max() - result.top_state_records)
            throw std::runtime_error("top-state record counter overflow");
        result.top_state_records += batch_top_records[batch];
        add_count(result.straight_total, batch_straight_totals[batch]);
        add_count(result.skew_total, batch_skew_totals[batch]);
    }
    return result;
}

template<class Counter>
bool counter_equal(const Counter& a, const Counter& b) {
    if (a.size() != b.size()) return false;
    for (const auto& [k, v] : a) {
        auto it = b.find(k);
        if (it == b.end() || it->second != v) return false;
    }
    return true;
}

Count total_qr(const QRStraight& data) {
    Count total = 0;
    for (const auto& [_, degrees] : data)
        for (const auto& counter : degrees)
            for (const auto& [__, count] : counter) add_count(total, count);
    return total;
}
Count total_qr(const QRSkew& data) {
    Count total = 0;
    for (const auto& [_, degrees] : data)
        for (const auto& counter : degrees)
            for (const auto& [__, count] : counter) add_count(total, count);
    return total;
}

struct RunResult { bool pass; double generation; double comparison; };
using Clock = std::chrono::steady_clock;
double seconds(Clock::time_point a, Clock::time_point b) {
    return std::chrono::duration<double>(b - a).count();
}

RunResult run_qr(unsigned n, bool progress, bool stop_first) {
    auto t0 = Clock::now();
    QRBatchedGeneration generated = generate_qr_batched(n, progress);
    auto t1 = Clock::now();
    QRStraight& straight = generated.straight;
    QRSkew& skew = generated.skew;

    std::vector<const QRSkew::value_type*> work;
    work.reserve(skew.size());
    for (const auto& item : skew) work.push_back(&item);
    std::uint64_t comparisons = 0, failures = 0;

    if (stop_first) {
        CoefficientCache coeffs;
        for (const auto* item : work) {
            const auto& pair = item->first;
            const auto& degrees = item->second;
            const unsigned limit = n - shape_size(pair.inner);
            const auto& c = coeffs.get(pair.outer, pair.inner, false, limit);
            for (unsigned actual = 1; actual <= limit; ++actual) {
                ++comparisons;
                static const MaskCounter empty;
                const MaskCounter& left = actual < degrees.size() ? degrees[actual] : empty;
                MaskCounter right;
                for (const auto& [shape, coefficient] : c) {
                    if (shape_size(shape) > actual) continue;
                    auto sit = straight.find(shape);
                    if (sit == straight.end() || actual >= sit->second.size()) continue;
                    for (const auto& [peak, count] : sit->second[actual])
                        add_product(right[peak], coefficient, count);
                }
                if (!counter_equal(left, right)) { ++failures; goto qr_done; }
            }
        }
    } else {
        #pragma omp parallel reduction(+:comparisons,failures)
        {
            CoefficientCache coeffs;
            #pragma omp for schedule(dynamic,1)
            for (std::int64_t wi = 0; wi < static_cast<std::int64_t>(work.size()); ++wi) {
                const auto& pair = work[wi]->first;
                const auto& degrees = work[wi]->second;
                const unsigned limit = n - shape_size(pair.inner);
                const auto& c = coeffs.get(pair.outer, pair.inner, false, limit);
                for (unsigned actual = 1; actual <= limit; ++actual) {
                    ++comparisons;
                    static const MaskCounter empty;
                    const MaskCounter& left = actual < degrees.size() ? degrees[actual] : empty;
                    MaskCounter right;
                    for (const auto& [shape, coefficient] : c) {
                        if (shape_size(shape) > actual) continue;
                        auto sit = straight.find(shape);
                        if (sit == straight.end() || actual >= sit->second.size()) continue;
                        for (const auto& [peak, count] : sit->second[actual])
                            add_product(right[peak], coefficient, count);
                    }
                    if (!counter_equal(left, right)) ++failures;
                }
            }
        }
    }
qr_done:
    auto t2 = Clock::now();
    const bool pass = failures == 0;
    std::cout << "Q/R CHECK\n"
              << "maximum charged entries: " << n << '\n'
              << "straight shapes:          " << straight.size() << '\n'
              << "proper skew shapes:       " << skew.size() << '\n'
              << "straight tableaux:        " << total_qr(straight) << '\n'
              << "derived skew tableaux:    " << total_qr(skew) << '\n'
              << "tableaux at top degree:   " << generated.top_tableaux << '\n'
              << "batched top-state records:" << generated.top_state_records << '\n'
              << "generation split degree:  " << generated.split << '\n'
              << "generation batches:       " << generated.batches << '\n'
              << "shape-degree comparisons: " << comparisons << '\n'
              << std::fixed << std::setprecision(6)
              << "generation runtime:       " << seconds(t0,t1) << " seconds\n"
              << "comparison runtime:       " << seconds(t1,t2) << " seconds\n"
              << "total runtime:            " << seconds(t0,t2) << " seconds\n"
              << "result: " << (pass ? "PASS" : "FAIL") << '\n';
    return {pass, seconds(t0,t1), seconds(t1,t2)};
}

RunResult run_p(unsigned n, unsigned num_vars, bool progress, bool stop_first) {
    auto t0 = Clock::now();
    PBatchedGeneration generated = generate_p_batched(n, num_vars, progress);
    auto t1 = Clock::now();

    std::vector<const PMonoSkew::value_type*> work;
    work.reserve(generated.skew.size());
    for (const auto& item : generated.skew) work.push_back(&item);
    std::vector<std::size_t> dimensions(n + 1, 0);
    PTransform dim_transform;
    for (unsigned d = 1; d <= n; ++d)
        dimensions[d] = dim_transform.dimension(d, std::min(num_vars, d));

    std::uint64_t comparisons = 0, failures = 0;
    if (stop_first) {
        CoefficientCache coeffs;
        for (const auto* item : work) {
            const ShapePair& pair = item->first;
            const MonoDegrees& degrees = item->second;
            const unsigned limit = n - shape_size(pair.inner);
            const auto& c = coeffs.get(pair.outer, pair.inner, true, limit);
            for (unsigned actual = 1; actual <= limit; ++actual) {
                ++comparisons;
                std::vector<Count> left;
                if (actual < degrees.size() && !degrees[actual].empty()) left = degrees[actual];
                else left.assign(dimensions[actual], 0);
                std::vector<Count> right(dimensions[actual], 0);
                for (const auto& [shape, coefficient] : c) {
                    if (shape_size(shape) > actual) continue;
                    auto sit = generated.straight.find(shape);
                    if (sit == generated.straight.end() || actual >= sit->second.size()) continue;
                    const auto& source = sit->second[actual];
                    for (std::size_t j = 0; j < source.size(); ++j)
                        add_product(right[j], coefficient, source[j]);
                }
                if (left != right) { ++failures; goto p_done; }
            }
        }
    } else {
        #pragma omp parallel reduction(+:comparisons,failures)
        {
            CoefficientCache coeffs;
            #pragma omp for schedule(dynamic,1)
            for (std::int64_t wi = 0; wi < static_cast<std::int64_t>(work.size()); ++wi) {
                const ShapePair& pair = work[wi]->first;
                const MonoDegrees& degrees = work[wi]->second;
                const unsigned limit = n - shape_size(pair.inner);
                const auto& c = coeffs.get(pair.outer, pair.inner, true, limit);
                for (unsigned actual = 1; actual <= limit; ++actual) {
                    ++comparisons;
                    std::vector<Count> left;
                    if (actual < degrees.size() && !degrees[actual].empty()) left = degrees[actual];
                    else left.assign(dimensions[actual], 0);
                    std::vector<Count> right(dimensions[actual], 0);
                    for (const auto& [shape, coefficient] : c) {
                        if (shape_size(shape) > actual) continue;
                        auto sit = generated.straight.find(shape);
                        if (sit == generated.straight.end() || actual >= sit->second.size()) continue;
                        const auto& source = sit->second[actual];
                        for (std::size_t j = 0; j < source.size(); ++j)
                            add_product(right[j], coefficient, source[j]);
                    }
                    if (left != right) ++failures;
                }
            }
        }
    }
p_done:
    auto t2 = Clock::now();
    const bool pass = failures == 0;
    std::cout << "P CHECK\n"
              << "maximum charged entries: " << n << '\n'
              << "maximum monomial length:  " << num_vars << '\n'
              << "straight shapes:          " << generated.straight.size() << '\n'
              << "proper skew shapes:       " << generated.skew.size() << '\n'
              << "straight tableaux:        " << generated.straight_total << '\n'
              << "derived skew tableaux:    " << generated.skew_total << '\n'
              << "tableaux at top degree:   " << generated.top_tableaux << '\n'
              << "final transition records:" << generated.top_state_records << '\n'
              << "generation split degree:  " << generated.split << '\n'
              << "generation batches:       " << generated.batches << '\n'
              << "shape-degree comparisons: " << comparisons << '\n'
              << std::fixed << std::setprecision(6)
              << "generation runtime:       " << seconds(t0,t1) << " seconds\n"
              << "comparison runtime:       " << seconds(t1,t2) << " seconds\n"
              << "total runtime:            " << seconds(t0,t2) << " seconds\n"
              << "result: " << (pass ? "PASS" : "FAIL") << '\n';
    return {pass, seconds(t0,t1), seconds(t1,t2)};
}

struct Options {
    std::string mode = "both";
    unsigned max_entries = 15;
    unsigned qr_bound = 0;
    unsigned p_bound = 0;
    unsigned num_vars = 0;
    bool progress = false;
    bool stop_first = false;
};

Options parse(int argc, char** argv) {
    Options o;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        auto need = [&](const char* name) -> std::string {
            if (++i >= argc) throw std::runtime_error(std::string("missing value for ") + name);
            return argv[i];
        };
        if (arg == "--mode") o.mode = need("--mode");
        else if (arg == "--max-entries") o.max_entries = std::stoul(need("--max-entries"));
        else if (arg == "--qr-bound") o.qr_bound = std::stoul(need("--qr-bound"));
        else if (arg == "--p-bound") o.p_bound = std::stoul(need("--p-bound"));
        else if (arg == "--num-vars") o.num_vars = std::stoul(need("--num-vars"));
        else if (arg == "--progress") o.progress = true;
        else if (arg == "--stop-on-first-failure") o.stop_first = true;
        else if (arg == "-h" || arg == "--help") {
            std::cout
                << "Usage: optimized [--mode qr|p|both] [--max-entries N]\n"
                << "                 [--qr-bound N] [--p-bound N] [--num-vars N]\n"
                << "                 [--progress] [--stop-on-first-failure]\n\n"
                << "--max-entries sets both bounds unless a mode-specific bound is given.\n"
                << "For a complete P check, use --num-vars at least --p-bound.\n";
            std::exit(0);
        } else throw std::runtime_error("unknown option: " + arg);
    }
    if (o.mode != "qr" && o.mode != "p" && o.mode != "both")
        throw std::runtime_error("invalid mode");
    if (!o.qr_bound) o.qr_bound = o.max_entries;
    if (!o.p_bound) o.p_bound = o.max_entries;
    auto validate_bound = [](unsigned value, const char* name) {
        if (value < 1 || value > 30)
            throw std::runtime_error(std::string(name) + " must be 1..30");
    };
    validate_bound(o.qr_bound, "qr-bound");
    validate_bound(o.p_bound, "p-bound");
    if (!o.num_vars) o.num_vars = o.p_bound;
    validate_bound(o.num_vars, "num-vars");
    return o;
}

} // namespace

int main(int argc, char** argv) {
    try {
        Options o = parse(argc, argv);
        bool pass = true;
        if (o.mode == "qr" || o.mode == "both") pass &= run_qr(o.qr_bound, o.progress, o.stop_first).pass;
        if (o.mode == "both") std::cout << '\n';
        if (o.mode == "p" || o.mode == "both") pass &= run_p(o.p_bound, o.num_vars, o.progress, o.stop_first).pass;
        return pass ? 0 : 1;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 2;
    }
}
