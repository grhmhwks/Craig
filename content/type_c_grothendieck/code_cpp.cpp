// Peakset-refined type C Grothendieck finite checker.
// Compile (default: W_6, generators 0,...,5):
//   g++ -O3 -march=native -DNDEBUG -std=c++20 -pthread type_c_peakset_check.cpp -o type_c_peakset_check
// Run:
//   ./type_c_peakset_check 15 4
// Override the rank at compile time with -DTYPE_C_RANK=<rank>.

#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <limits>
#include <memory>
#include <numeric>
#include <stdexcept>
#include <thread>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#ifndef TYPE_C_RANK
#define TYPE_C_RANK 6
#endif

using Clock = std::chrono::steady_clock;
using U64 = std::uint64_t;
using U32 = std::uint32_t;
using I64 = std::int64_t;

static constexpr int RANK = TYPE_C_RANK;
static constexpr int LARGEST = RANK - 1;
static constexpr int ALPH = RANK;
static constexpr int PID_BITS = 20;
static constexpr U32 PID_MASK = (U32(1) << PID_BITS) - 1;
static constexpr U64 EMPTY = ~U64{0};
static_assert(RANK >= 1 && RANK <= 7, "This packed implementation supports W_1 through W_7.");

static inline double seconds(Clock::time_point a, Clock::time_point b) {
    return std::chrono::duration<double>(b - a).count();
}

static inline U64 mix64(U64 x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

static inline std::size_t reduce64(U64 h, std::size_t n) {
    return std::size_t((__uint128_t(h) * n) >> 64);
}

// Compact open-addressing map: uint64 key -> uint32 count.
class Flat32 {
    std::unique_ptr<U64[]> keys_;
    std::unique_ptr<U32[]> vals_;
    std::size_t cap_ = 0, size_ = 0, limit_ = 0;
    static constexpr double LOAD = 0.84;

    void allocate(std::size_t cap) {
        cap = std::max<std::size_t>(cap, 8);
        keys_ = std::make_unique<U64[]>(cap);
        vals_ = std::make_unique<U32[]>(cap);
        std::fill_n(keys_.get(), cap, EMPTY);
        cap_ = cap;
        size_ = 0;
        limit_ = std::size_t(cap * LOAD);
    }

    void add_nogrow(U64 key, U32 value) {
        std::size_t i = reduce64(mix64(key), cap_);
        for (;;) {
            U64 old = keys_[i];
            if (old == EMPTY) {
                keys_[i] = key;
                vals_[i] = value;
                ++size_;
                return;
            }
            if (old == key) {
                U64 sum = U64(vals_[i]) + value;
                if (sum > std::numeric_limits<U32>::max()) {
                    throw std::overflow_error("32-bit dynamic-state count overflow");
                }
                vals_[i] = U32(sum);
                return;
            }
            if (++i == cap_) i = 0;
        }
    }

    void rehash(std::size_t newcap) {
        auto old_keys = std::move(keys_);
        auto old_vals = std::move(vals_);
        std::size_t old_cap = cap_;
        allocate(newcap);
        for (std::size_t i = 0; i < old_cap; ++i) {
            if (old_keys[i] != EMPTY) add_nogrow(old_keys[i], old_vals[i]);
        }
    }

public:
    Flat32() = default;
    explicit Flat32(std::size_t expected) { reserve(expected); }
    Flat32(Flat32&&) = default;
    Flat32& operator=(Flat32&&) = default;
    Flat32(const Flat32&) = delete;
    Flat32& operator=(const Flat32&) = delete;

    void reserve(std::size_t expected) {
        std::size_t needed = std::size_t(double(expected) / LOAD) + 8;
        if (needed > cap_) rehash(needed);
    }

    void add(U64 key, U32 value) {
        if (!cap_) allocate(8);
        if (size_ + 1 > limit_) rehash(std::size_t(cap_ * 1.5) + 16);
        add_nogrow(key, value);
    }

    template<class F>
    void each(F&& f) const {
        for (std::size_t i = 0; i < cap_; ++i) {
            if (keys_[i] != EMPTY) f(keys_[i], vals_[i]);
        }
    }

    std::size_t size() const { return size_; }
    void reset() { keys_.reset(); vals_.reset(); cap_ = size_ = limit_ = 0; }
};

// Compact difference map: uint64 key -> signed 64-bit count.
class FlatI64 {
    std::unique_ptr<U64[]> keys_;
    std::unique_ptr<I64[]> vals_;
    std::size_t cap_ = 0, size_ = 0, limit_ = 0;
    static constexpr double LOAD = 0.84;

    void allocate(std::size_t cap) {
        cap = std::max<std::size_t>(cap, 8);
        keys_ = std::make_unique<U64[]>(cap);
        vals_ = std::make_unique<I64[]>(cap);
        std::fill_n(keys_.get(), cap, EMPTY);
        cap_ = cap;
        size_ = 0;
        limit_ = std::size_t(cap * LOAD);
    }

    void add_nogrow(U64 key, I64 value) {
        std::size_t i = reduce64(mix64(key), cap_);
        for (;;) {
            U64 old = keys_[i];
            if (old == EMPTY) {
                keys_[i] = key;
                vals_[i] = value;
                ++size_;
                return;
            }
            if (old == key) {
                vals_[i] += value;
                return;
            }
            if (++i == cap_) i = 0;
        }
    }

    void rehash(std::size_t newcap) {
        auto old_keys = std::move(keys_);
        auto old_vals = std::move(vals_);
        std::size_t old_cap = cap_;
        allocate(newcap);
        for (std::size_t i = 0; i < old_cap; ++i) {
            if (old_keys[i] != EMPTY) add_nogrow(old_keys[i], old_vals[i]);
        }
    }

public:
    FlatI64() = default;
    explicit FlatI64(std::size_t expected) { reserve(expected); }
    FlatI64(FlatI64&&) = default;
    FlatI64& operator=(FlatI64&&) = default;
    FlatI64(const FlatI64&) = delete;
    FlatI64& operator=(const FlatI64&) = delete;

    void reserve(std::size_t expected) {
        std::size_t needed = std::size_t(double(expected) / LOAD) + 8;
        if (needed > cap_) rehash(needed);
    }

    void add(U64 key, I64 value) {
        if (!cap_) allocate(8);
        if (size_ + 1 > limit_) rehash(std::size_t(cap_ * 1.5) + 16);
        add_nogrow(key, value);
    }

    I64 get(U64 key) const {
        if (!cap_) return 0;
        std::size_t i = reduce64(mix64(key), cap_);
        for (;;) {
            U64 old = keys_[i];
            if (old == EMPTY) return 0;
            if (old == key) return vals_[i];
            if (++i == cap_) i = 0;
        }
    }

    std::pair<std::size_t,U64> mismatch_summary() const {
        std::size_t bad = 0;
        U64 max_abs = 0;
        for (std::size_t i = 0; i < cap_; ++i) if (keys_[i] != EMPTY && vals_[i] != 0) {
            ++bad;
            U64 a = vals_[i] < 0 ? U64(-vals_[i]) : U64(vals_[i]);
            max_abs = std::max(max_abs, a);
        }
        return {bad, max_abs};
    }

    std::size_t size() const { return size_; }
};

struct Dense32 {
    std::vector<U64> keys;
    std::vector<U32> vals;
    std::size_t size() const { return keys.size(); }
    template<class F> void each(F&& f) const {
        for (std::size_t i = 0; i < keys.size(); ++i) f(keys[i], vals[i]);
    }
    void release() {
        std::vector<U64>().swap(keys);
        std::vector<U32>().swap(vals);
    }
};

static Dense32 densify(Flat32& map) {
    Dense32 out;
    out.keys.reserve(map.size());
    out.vals.reserve(map.size());
    map.each([&](U64 key, U32 value) {
        out.keys.push_back(key);
        out.vals.push_back(value);
    });
    map.reset();
    return out;
}

struct PermData {
    std::vector<std::array<U32, ALPH>> transition;
};

static int encode_perm(const std::array<std::int8_t,RANK>& p) {
    constexpr int base = 2 * RANK + 1;
    int code = 0;
    for (int i = 0; i < RANK; ++i) code = code * base + (int(p[i]) + RANK);
    return code;
}

static PermData build_permutations() {
    std::vector<std::array<std::int8_t,RANK>> perms;
    std::size_t factorial = 1;
    for (int i = 2; i <= RANK; ++i) factorial *= i;
    perms.reserve(factorial * (std::size_t(1) << RANK));

    std::unordered_map<int,U32> id;
    id.reserve(perms.capacity() * 5 / 4);
    std::array<int,RANK> values{};
    std::iota(values.begin(), values.end(), 1);
    do {
        for (int signs = 0; signs < (1 << RANK); ++signs) {
            std::array<std::int8_t,RANK> p{};
            for (int i = 0; i < RANK; ++i) p[i] = (signs & (1 << i)) ? -values[i] : values[i];
            U32 new_id = U32(perms.size());
            id.emplace(encode_perm(p), new_id);
            perms.push_back(p);
        }
    } while (std::next_permutation(values.begin(), values.end()));

    if (perms.size() >= (std::size_t(1) << PID_BITS)) {
        throw std::runtime_error("permutation id no longer fits packed state");
    }

    PermData data;
    data.transition.resize(perms.size());
    for (U32 pid = 0; pid < perms.size(); ++pid) {
        for (int generator = 0; generator < ALPH; ++generator) {
            auto q = perms[pid];
            if (generator == 0) {
                if (q[0] > 0) q[0] = -q[0];
            } else if (q[generator - 1] < q[generator]) {
                std::swap(q[generator - 1], q[generator]);
            }
            data.transition[pid][generator] = id.at(encode_perm(q));
        }
    }
    return data;
}

static inline U64 word_key(U32 pid, U32 peakmask) {
    return U64(pid) | (U64(peakmask) << PID_BITS);
}
static inline U32 word_pid(U64 key) { return U32(key) & PID_MASK; }
static inline U32 word_peakmask(U64 key) { return U32(key >> PID_BITS); }

struct VecHash {
    std::size_t operator()(const std::vector<int>& v) const noexcept {
        U64 h = 1469598103934665603ULL;
        for (int x : v) { h ^= U64(x + 17); h *= 1099511628211ULL; }
        return std::size_t(h);
    }
};

static bool column_compatible(const std::vector<int>& bottom0, const std::vector<int>& top0) {
    auto bottom = bottom0;
    auto top = top0;
    if (bottom.empty()) return true;
    if (top.size() <= bottom.size()) return false;

    int bmin = *std::min_element(bottom.begin(), bottom.end());
    int bindex = 0;
    for (int i = 0; i < int(bottom.size()); ++i) if (bottom[i] == bmin) bindex = i;
    for (int i = 0; i <= bindex; ++i) bottom[i] = -bottom[i];

    int tmin = *std::min_element(top.begin(), top.end());
    int tindex = 0;
    for (int i = 0; i < int(top.size()); ++i) if (top[i] == tmin) tindex = i;
    for (int i = 0; i < tindex; ++i) top[i] = -top[i];

    if (std::abs(bottom.back()) >= std::abs(top[0])) return false;
    if (std::abs(bottom[0]) >= std::abs(top[0])) return false;

    for (int i = 0; i < int(bottom.size()); ++i) {
        if (top[i + 1] > bottom[i]) {
            for (int j = i + 1; j < int(bottom.size()); ++j) {
                if (bottom[i] < bottom[j] && bottom[j] < top[i + 1]) return false;
                if (bottom[i] < -bottom[j] && -bottom[j] < top[i + 1]) return false;
                if (bottom[j] == top[i + 1] || bottom[j] == -top[i + 1]) return false;
            }
            for (int k = 0; k <= i; ++k) {
                if (bottom[i] < top[k] && top[k] < top[i + 1]) return false;
                if (bottom[i] < -top[k] && -top[k] < top[i + 1]) return false;
                if (top[k] == -top[i + 1] || top[k] == top[i + 1]) return false;
            }
        }
    }
    return true;
}

struct RowData {
    std::vector<std::vector<int>> rows;
    std::vector<std::vector<int>> by_length;
    std::vector<std::vector<int>> compatible_above;
};

static RowData build_rows() {
    std::unordered_set<std::vector<int>,VecHash> unique_rows;
    for (int minimum = 0; minimum <= LARGEST; ++minimum) {
        int remaining = LARGEST - minimum;
        for (int left_mask = 0; left_mask < (1 << remaining); ++left_mask) {
            for (int right_mask = 0; right_mask < (1 << remaining); ++right_mask) {
                std::vector<int> row;
                for (int j = remaining - 1; j >= 0; --j) if (left_mask & (1 << j)) row.push_back(minimum + 1 + j);
                row.push_back(minimum);
                for (int j = 0; j < remaining; ++j) if (right_mask & (1 << j)) row.push_back(minimum + 1 + j);
                unique_rows.insert(std::move(row));
            }
        }
    }

    RowData data;
    data.rows.assign(unique_rows.begin(), unique_rows.end());
    std::sort(data.rows.begin(), data.rows.end(), [](const auto& a, const auto& b) {
        return a.size() == b.size() ? a < b : a.size() < b.size();
    });

    int max_length = 0;
    for (const auto& row : data.rows) max_length = std::max(max_length, int(row.size()));
    data.by_length.resize(max_length + 1);
    for (int id = 0; id < int(data.rows.size()); ++id) data.by_length[data.rows[id].size()].push_back(id);

    data.compatible_above.resize(data.rows.size());
    for (int bottom = 0; bottom < int(data.rows.size()); ++bottom) {
        for (int top = 0; top < int(data.rows.size()); ++top) {
            if (data.rows[top].size() > data.rows[bottom].size() &&
                column_compatible(data.rows[bottom], data.rows[top])) {
                data.compatible_above[bottom].push_back(top);
            }
        }
    }
    return data;
}

static std::vector<std::vector<int>> strict_shapes_upto(int maximum_size, int maximum_part) {
    std::vector<std::vector<int>> out;
    std::vector<int> prefix;
    std::function<void(int,int)> rec = [&](int remaining, int cap) {
        if (!prefix.empty()) out.push_back(prefix);
        for (int part = std::min(remaining, cap); part >= 1; --part) {
            prefix.push_back(part);
            rec(remaining - part, part - 1);
            prefix.pop_back();
        }
    };
    rec(maximum_size, maximum_part);
    return out;
}

static U64 encode_shape(const std::vector<int>& shape) {
    U64 code = shape.size();
    int shift = 4;
    for (int part : shape) { code |= U64(part) << shift; shift += 4; }
    return code;
}

static U64 encode_shape(const std::array<std::uint8_t,16>& shape, int rows) {
    U64 code = rows;
    int shift = 4;
    for (int i = 0; i < rows; ++i) { code |= U64(shape[i]) << shift; shift += 4; }
    return code;
}

static inline U32 apply_row(U32 pid, const std::vector<int>& row, const PermData& permutations) {
    for (int generator : row) pid = permutations.transition[pid][generator];
    return pid;
}

using PidCount = std::pair<U32,U64>;

struct TableauData {
    std::vector<std::vector<int>> shapes;
    std::vector<std::vector<PidCount>> by_shape;
    std::unordered_map<U64,int> shape_index;
    U64 total_tableaux = 0;
    std::size_t total_bins = 0;
};

static TableauData build_hecke_tableaux(const PermData& permutations, const RowData& rows, int maximum_degree) {
    TableauData out;
    out.shapes = strict_shapes_upto(maximum_degree, int(rows.by_length.size()) - 1);
    out.by_shape.resize(out.shapes.size());
    out.shape_index.reserve(out.shapes.size() * 2);

    for (int shape_id = 0; shape_id < int(out.shapes.size()); ++shape_id) {
        const auto& shape = out.shapes[shape_id];
        out.shape_index.emplace(encode_shape(shape), shape_id);

        Flat32 states;
        int bottom_length = shape.back();
        states.reserve(rows.by_length[bottom_length].size() * 2 + 8);
        for (int bottom : rows.by_length[bottom_length]) {
            U32 pid = apply_row(0, rows.rows[bottom], permutations);
            states.add(U64(pid) | (U64(bottom) << PID_BITS), 1);
        }

        for (auto it = shape.rbegin() + 1; it != shape.rend(); ++it) {
            int top_length = *it;
            Flat32 next;
            next.reserve(states.size() * 2 + 8);
            states.each([&](U64 packed, U32 multiplicity) {
                U32 pid = U32(packed) & PID_MASK;
                int bottom = int(packed >> PID_BITS);
                for (int top : rows.compatible_above[bottom]) {
                    if (int(rows.rows[top].size()) != top_length) continue;
                    U32 next_pid = apply_row(pid, rows.rows[top], permutations);
                    next.add(U64(next_pid) | (U64(top) << PID_BITS), multiplicity);
                }
            });
            states = std::move(next);
        }

        std::unordered_map<U32,U64> pid_counts;
        pid_counts.reserve(states.size() + 8);
        states.each([&](U64 packed, U32 multiplicity) {
            U32 pid = U32(packed) & PID_MASK;
            pid_counts[pid] += multiplicity;
            out.total_tableaux += multiplicity;
        });

        auto& vector = out.by_shape[shape_id];
        vector.reserve(pid_counts.size());
        for (auto [pid,count] : pid_counts) vector.emplace_back(pid,count);
        std::sort(vector.begin(), vector.end());
        out.total_bins += vector.size();
    }
    return out;
}

struct QState {
    std::array<std::uint8_t,16> shape{};
    std::uint8_t rows = 0;
    std::int8_t previous2_row = -1, previous2_col = -1;
    std::int8_t previous_row = -1, previous_col = -1;
    std::uint16_t peaks = 0;

    bool operator==(const QState& other) const {
        return shape == other.shape && rows == other.rows &&
               previous2_row == other.previous2_row && previous2_col == other.previous2_col &&
               previous_row == other.previous_row && previous_col == other.previous_col &&
               peaks == other.peaks;
    }
};

struct QStateHash {
    std::size_t operator()(const QState& state) const noexcept {
        U64 h = state.peaks |
                (U64(state.rows) << 16) |
                (U64(std::uint8_t(state.previous_row + 1)) << 20) |
                (U64(std::uint8_t(state.previous_col + 1)) << 25) |
                (U64(std::uint8_t(state.previous2_row + 1)) << 30) |
                (U64(std::uint8_t(state.previous2_col + 1)) << 35);
        for (int i = 0; i < state.rows; ++i) h = (h ^ state.shape[i]) * 0x9e3779b97f4a7c15ULL;
        return std::size_t(h ^ (h >> 32));
    }
};

using MaskCount = std::pair<std::uint16_t,U64>;

struct RecordingData {
    // by_shape[shape_id][degree] = (peak mask, multiplicity)
    std::vector<std::vector<std::vector<MaskCount>>> by_shape;
    U64 total_tableaux = 1; // include the empty tableau in the summary
    std::size_t total_bins = 0;
};

static RecordingData build_recording_tableaux(const TableauData& hecke, int maximum_degree) {
    RecordingData out;
    out.by_shape.resize(hecke.shapes.size(), std::vector<std::vector<MaskCount>>(maximum_degree + 1));

    std::unordered_map<QState,U64,QStateHash> states, next;
    QState empty;
    states.emplace(empty, 1);

    // Temporary exact counts indexed by (shape id, degree, peak mask).
    std::vector<std::vector<std::unordered_map<std::uint16_t,U64>>> counts(
        hecke.shapes.size(), std::vector<std::unordered_map<std::uint16_t,U64>>(maximum_degree + 1));

    for (int entry = 0; entry < maximum_degree; ++entry) {
        next.clear();
        next.reserve(states.size() * 3 + 8);

        for (const auto& [state,multiplicity] : states) {
            auto add = [&](QState new_state, int new_row, int new_col) {
                if (entry >= 2 && state.previous2_col < state.previous_col && state.previous_row < new_row) {
                    new_state.peaks |= std::uint16_t(1u << (entry - 1));
                }
                new_state.previous2_row = state.previous_row;
                new_state.previous2_col = state.previous_col;
                new_state.previous_row = new_row;
                new_state.previous_col = new_col;
                next[new_state] += multiplicity;
            };

            for (int row = 0; row < state.rows; ++row) {
                int last_col = int(state.shape[row]) - 1 + row;

                // Put the new label into the existing last box.  Consecutive
                // labels are forbidden in the same box.
                if (!(state.previous_row == row && state.previous_col == last_col) &&
                    (row == state.rows - 1 || state.shape[row] > 1 + state.shape[row + 1])) {
                    add(state, row, last_col);
                }

                // Append a new shifted box to this row.
                if (row == 0 || 1 + int(state.shape[row]) < int(state.shape[row - 1])) {
                    QState new_state = state;
                    ++new_state.shape[row];
                    add(new_state, row, int(new_state.shape[row]) - 1 + row);
                }
            }

            // Add a new bottom shifted row.
            if (state.rows == 0 || state.shape[state.rows - 1] > 1) {
                QState new_state = state;
                int row = new_state.rows++;
                new_state.shape[row] = 1;
                add(new_state, row, row);
            }
        }

        states.swap(next);
        int degree = entry + 1;
        for (const auto& [state,multiplicity] : states) {
            U64 code = encode_shape(state.shape, state.rows);
            auto found = hecke.shape_index.find(code);
            if (found == hecke.shape_index.end()) continue;
            counts[found->second][degree][state.peaks] += multiplicity;
            out.total_tableaux += multiplicity;
        }
    }

    for (int shape = 0; shape < int(counts.size()); ++shape) {
        for (int degree = 1; degree <= maximum_degree; ++degree) {
            auto& target = out.by_shape[shape][degree];
            target.reserve(counts[shape][degree].size());
            for (auto [mask,count] : counts[shape][degree]) target.emplace_back(mask,count);
            std::sort(target.begin(), target.end());
            out.total_bins += target.size();
        }
    }
    return out;
}

struct CompareSummary {
    std::size_t bins = 0;
    std::size_t mismatches = 0;
    U64 max_difference = 0;
    U64 pair_operations = 0;
};

static CompareSummary compare_degree(
    int degree,
    const std::array<Dense32,2*ALPH>& word_states,
    const TableauData& hecke,
    const RecordingData& recording,
    int thread_count)
{
    std::size_t state_count = 0;
    for (const auto& category : word_states) state_count += category.size();

    // Aggregate the small set of local word categories once.  The resulting
    // table is read-only during the peakset comparison and is safe to share.
    FlatI64 word_bins(std::max<std::size_t>(64, state_count * 42 / 100));
    for (const auto& category : word_states) {
        category.each([&](U64 key, U32 multiplicity) {
            word_bins.add(key, I64(multiplicity));
        });
    }

    int mask_limit = 1 << std::max(1, degree - 1);
    std::vector<std::vector<std::pair<int,U64>>> shapes_by_peak(mask_limit);
    for (int shape = 0; shape < int(hecke.shapes.size()); ++shape) {
        for (const auto& [mask,q_count] : recording.by_shape[shape][degree]) {
            shapes_by_peak[mask].push_back({shape,q_count});
        }
    }

    std::size_t permutation_count = 1;
    for (int i = 2; i <= RANK; ++i) permutation_count *= std::size_t(i);
    permutation_count <<= RANK;

    struct LocalSummary {
        std::size_t bins = 0;
        std::size_t mismatches = 0;
        U64 max_difference = 0;
        U64 pair_operations = 0;
    };

    int workers = std::max(1, std::min(thread_count, 2 * ALPH));
    std::vector<LocalSummary> local(workers);
    std::atomic<int> mask_task{0};

    auto work = [&](int worker_id) {
        std::vector<U64> pair_count(permutation_count, 0);
        std::vector<U32> touched;
        touched.reserve(permutation_count / 2);
        auto& summary = local[worker_id];

        for (;;) {
            int mask = mask_task.fetch_add(1, std::memory_order_relaxed);
            if (mask >= int(shapes_by_peak.size())) break;
            if (shapes_by_peak[mask].empty()) continue;

            touched.clear();
            for (const auto& [shape,q_count] : shapes_by_peak[mask]) {
                const auto& t = hecke.by_shape[shape];
                summary.pair_operations += U64(t.size());
                for (const auto& [pid,t_count] : t) {
                    __uint128_t product = __uint128_t(t_count) * q_count;
                    if (product > std::numeric_limits<U64>::max()) {
                        throw std::overflow_error("pair count exceeds 64-bit range");
                    }
                    if (pair_count[pid] == 0) touched.push_back(pid);
                    if (__uint128_t(pair_count[pid]) + product > std::numeric_limits<U64>::max()) {
                        throw std::overflow_error("pair-bin count exceeds 64-bit range");
                    }
                    pair_count[pid] += U64(product);
                }
            }

            for (U32 pid : touched) {
                U64 expected = pair_count[pid];
                I64 actual_signed = word_bins.get(word_key(pid,U32(mask)));
                U64 actual = actual_signed < 0 ? 0 : U64(actual_signed);
                ++summary.bins;
                if (actual != expected) {
                    ++summary.mismatches;
                    U64 diff = actual > expected ? actual - expected : expected - actual;
                    summary.max_difference = std::max(summary.max_difference,diff);
                }
                pair_count[pid] = 0;
            }
        }
    };

    if (workers == 1) {
        work(0);
    } else {
        std::vector<std::thread> pool;
        pool.reserve(workers);
        for (int i = 0; i < workers; ++i) pool.emplace_back(work,i);
        for (auto& worker : pool) worker.join();
    }

    CompareSummary summary;
    for (const auto& part : local) {
        summary.bins += part.bins;
        summary.mismatches += part.mismatches;
        summary.max_difference = std::max(summary.max_difference,part.max_difference);
        summary.pair_operations += part.pair_operations;
    }

    // Pair bins are distinct across peaksets.  Matching every pair bin plus
    // equality of support sizes rules out any extra word-side bin.
    if (summary.bins != word_bins.size()) {
        std::size_t delta = summary.bins > word_bins.size()
            ? summary.bins - word_bins.size() : word_bins.size() - summary.bins;
        summary.mismatches += delta;
    }
    return summary;
}

static std::array<Dense32,2*ALPH> next_word_degree(
    const std::array<Dense32,2*ALPH>& states,
    const PermData& permutations,
    int new_degree,
    int thread_count)
{
    std::array<Dense32,2*ALPH> dense;

    auto build_category = [&](int category) {
        int new_last = category / 2;
        int new_rise = category & 1;
        std::size_t source_states = 0;
        for (int old_last = 0; old_last < ALPH; ++old_last) {
            if (old_last != new_last && (old_last < new_last) == bool(new_rise)) {
                source_states += states[2 * old_last].size() + states[2 * old_last + 1].size();
            }
        }
        if (!source_states) return;

        double unique_fraction =
            new_degree <= 6 ? 1.00 :
            new_degree <= 9 ? 0.65 :
            new_degree <= 14 ? 0.47 : 0.52;
        Flat32 destination;
        destination.reserve(std::max<std::size_t>(8, std::size_t(source_states * unique_fraction) + 8));

        U32 peak_bit = U32(1) << (new_degree - 2);
        for (int old_last = 0; old_last < ALPH; ++old_last) {
            if (old_last == new_last || (old_last < new_last) != bool(new_rise)) continue;
            for (int old_rise = 0; old_rise < 2; ++old_rise) {
                bool creates_peak = old_rise && old_last > new_last;
                states[2 * old_last + old_rise].each([&](U64 packed, U32 count) {
                    U32 pid = word_pid(packed);
                    U32 mask = word_peakmask(packed);
                    if (creates_peak) mask |= peak_bit;
                    destination.add(word_key(permutations.transition[pid][new_last], mask), count);
                });
            }
        }
        dense[category] = densify(destination);
    };

    if (thread_count <= 1) {
        for (int category = 0; category < 2 * ALPH; ++category) build_category(category);
    } else {
        std::atomic<int> task{0};
        int workers = std::min(thread_count, 2 * ALPH);
        std::vector<std::thread> pool;
        pool.reserve(workers);
        for (int i = 0; i < workers; ++i) {
            pool.emplace_back([&] {
                for (;;) {
                    int category = task.fetch_add(1);
                    if (category >= 2 * ALPH) return;
                    build_category(category);
                }
            });
        }
        for (auto& worker : pool) worker.join();
    }
    return dense;
}

int main(int argc, char** argv) {
    try {
        int maximum_degree = argc > 1 ? std::atoi(argv[1]) : 15;
        int threads = argc > 2 ? std::atoi(argv[2]) : 4;
        if (maximum_degree < 1 || maximum_degree > 15) {
            std::cerr << "maximum degree must be between 1 and 15\n";
            return 2;
        }
        if (threads < 1) threads = 1;

        auto start = Clock::now();
        auto permutations = build_permutations();
        auto after_permutations = Clock::now();
        auto rows = build_rows();
        auto after_rows = Clock::now();
        auto hecke = build_hecke_tableaux(permutations, rows, maximum_degree);
        auto after_hecke = Clock::now();
        auto recording = build_recording_tableaux(hecke, maximum_degree);
        auto after_recording = Clock::now();

        std::array<Dense32,2*ALPH> word_states;
        for (int generator = 0; generator < ALPH; ++generator) {
            word_states[2 * generator].keys.push_back(word_key(permutations.transition[0][generator], 0));
            word_states[2 * generator].vals.push_back(1);
        }

        U64 all_words = 0;
        std::size_t all_bins = 0;
        std::size_t all_mismatches = 0;
        U64 maximum_difference = 0;
        U64 pair_operations = 0;
        double transition_seconds = 0.0;
        double comparison_seconds = 0.0;

        std::cout << "type C peakset check: W_" << RANK
                  << ", degrees <= " << maximum_degree
                  << ", transition threads=" << threads << "\n";
        std::cout << "permutations=" << permutations.transition.size()
                  << " hook_rows=" << rows.rows.size()
                  << " strict_shapes=" << hecke.shapes.size()
                  << " hecke_tableaux=" << hecke.total_tableaux
                  << " hecke_shape_bins=" << hecke.total_bins
                  << " recording_tableaux=" << recording.total_tableaux
                  << " recording_bins=" << recording.total_bins << "\n";

        for (int degree = 1; degree <= maximum_degree; ++degree) {
            U64 level_words = 0;
            std::size_t level_states = 0;
            for (const auto& category : word_states) {
                level_states += category.size();
                category.each([&](U64, U32 count) { level_words += count; });
            }
            U64 expected_words = U64(ALPH);
            for (int i = 1; i < degree; ++i) expected_words *= U64(ALPH - 1);
            if (level_words != expected_words) throw std::runtime_error("word-count smoke check failed");
            all_words += level_words;

            auto compare_start = Clock::now();
            auto summary = compare_degree(degree, word_states, hecke, recording, threads);
            auto compare_stop = Clock::now();
            comparison_seconds += seconds(compare_start, compare_stop);
            all_bins += summary.bins;
            all_mismatches += summary.mismatches;
            maximum_difference = std::max(maximum_difference, summary.max_difference);
            pair_operations += summary.pair_operations;

            std::cout << "degree=" << degree
                      << " states=" << level_states
                      << " words=" << level_words
                      << " bins=" << summary.bins
                      << " pair_products=" << summary.pair_operations
                      << " mismatches=" << summary.mismatches
                      << " compare_seconds=" << seconds(compare_start, compare_stop)
                      << "\n" << std::flush;

            if (degree < maximum_degree) {
                auto transition_start = Clock::now();
                auto next = next_word_degree(word_states, permutations, degree + 1, threads);
                for (auto& category : word_states) category.release();
                word_states = std::move(next);
                auto transition_stop = Clock::now();
                transition_seconds += seconds(transition_start, transition_stop);
            }
        }

        auto finish = Clock::now();
        std::cout << "total_words=" << all_words
                  << " total_bins=" << all_bins
                  << " pair_products=" << pair_operations
                  << " mismatches=" << all_mismatches
                  << " max_difference=" << maximum_difference << "\n";
        std::cout << "timings_seconds: permutations=" << seconds(start, after_permutations)
                  << " rows=" << seconds(after_permutations, after_rows)
                  << " hecke_tableaux=" << seconds(after_rows, after_hecke)
                  << " recording_tableaux=" << seconds(after_hecke, after_recording)
                  << " word_transitions=" << transition_seconds
                  << " comparisons=" << comparison_seconds
                  << " total=" << seconds(start, finish) << "\n";
        std::cout << "status: " << (all_mismatches ? "FAIL" : "PASS") << "\n";
        return all_mismatches ? 1 : 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << "\n";
        return 2;
    }
}
