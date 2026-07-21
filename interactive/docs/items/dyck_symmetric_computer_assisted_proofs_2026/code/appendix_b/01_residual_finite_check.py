from collections import Counter
from math import comb

def stop(message):
    raise AssertionError(message)

def is_dyck_sequence(seq):
    return (
        bool(seq)
        and seq[0] == 0
        and all(x >= 0 for x in seq)
        and all(seq[i + 1] <= seq[i] + 1
                for i in range(len(seq) - 1))
    )

def deficit_and_area(seq):
    first_index = {}
    for i, value in enumerate(seq):
        first_index.setdefault(value, i)
    deficit = 0
    for i, left in enumerate(seq):
        for right in seq[i + 1:]:
            if left > right + 1:
                deficit += 1
            elif left < right and first_index[left] != i:
                deficit += 1
    return deficit, sum(seq)

def generate_dyck_sequences(length):
    sequences = []
    def extend(prefix):
        if len(prefix) == length:
            sequences.append(prefix)
            return
        for next_value in range(prefix[-1] + 2):
            extend(prefix + (next_value,))
    extend((0,))
    return sequences

def leftmost_extractable(seq):
    for index, value in enumerate(seq):
        has_parent = sum(x == value - 1 for x in seq[:index]) == 1
        next_ok = index == len(seq) - 1 or seq[index + 1] <= value
        if value > 0 and has_parent and next_ok:
            return index, value
    return None

def remove_index(seq, index):
    return seq[:index] + seq[index + 1:]

def is_full_skeleton(seq):
    return is_dyck_sequence(seq) and leftmost_extractable(seq) is None

def almost_zero_sequence(length):
    return (0,) * (length - 1) + (1,)

def excluded_skeleton(length):
    return (0, 0, 1) + (0,) * (length - 4) + (1,)

def is_special_skeleton(seq):
    return is_full_skeleton(seq) and seq != excluded_skeleton(len(seq))

def inject_after_first_parent(seq, value):
    for index, entry in enumerate(seq):
        if entry == value - 1:
            result = seq[:index + 1] + (value,) + seq[index + 1:]
            if is_dyck_sequence(result):
                return result
            stop(("skeleton injection produced non-Dyck",
                  seq, value, result))
    stop(("skeleton injection failed", seq, value))

def east3_applies(window3):
    _, x0, x1 = window3
    return x0 <= x1 + 1

def west3_applies(window3):
    return east3_applies(tuple(reversed(window3)))

def east5_case2b_applies(window5):
    _, x_minus1, x0, x1, x2 = window5
    return (
        x0 > x1 + 1
        and x_minus1 <= x1 + 1
        and x_minus1 <= x2 + 1
    )

def west5_case2b_applies(window5):
    return east5_case2b_applies(tuple(reversed(window5)))

def check_up_prefix(seq, length, deficit, half_area_limit):
    if seq == almost_zero_sequence(length):
        return "up special"
    if is_full_skeleton(seq):
        result = inject_after_first_parent(seq[:-1], seq[-1] + 1)
        if len(result) != length:
            stop(("up skeleton changed length", seq, result))
        return "up skeleton"
    first = leftmost_extractable(seq)
    if first is None:
        stop(("extraction lemma: up first extraction failed",
              length, deficit, half_area_limit, seq))
    index1, value1 = first
    child1 = remove_index(seq, index1)
    word1 = child1 + (value1 - 1,)
    if east3_applies(word1[-3:]):
        if index1 >= length - 2:
            stop(("position lemma: up/East3 position", seq, index1))
        return "up East3"
    second = leftmost_extractable(child1)
    if second is None:
        stop(("extraction lemma: up second extraction failed",
              length, deficit, half_area_limit, seq, child1))
    index2, value2 = second
    child2 = remove_index(child1, index2)
    word2 = child2 + (value1 - 1, value2 - 1)
    if not (index1 < length - 3 and index2 < len(child1) - 3):
        stop(("position lemma: up/East5 position",
              seq, index1, child1, index2))
    if not east5_case2b_applies(word2[-5:]):
        stop(("seven-window lemma: up would reach East7",
              length, deficit, half_area_limit, seq, word2[-5:]))
    return "up East5 case 2b"

def check_down_prefix(seq, length, deficit, half_area_limit):
    if seq == excluded_skeleton(length):
        return "down special"
    first = leftmost_extractable(seq)
    if first is None:
        stop(("extraction lemma: down first extraction failed",
              length, deficit, half_area_limit, seq))
    index1, value1 = first
    child1 = remove_index(seq, index1)
    skeleton_candidate = child1 + (value1 - 1,)
    if is_full_skeleton(skeleton_candidate):
        if len(skeleton_candidate) != length:
            stop(("down skeleton changed length", seq, skeleton_candidate))
        return "down skeleton"
    second = leftmost_extractable(child1)
    if second is None:
        stop(("extraction lemma: down second extraction failed",
              length, deficit, half_area_limit, seq, child1))
    index2, value2 = second
    child2 = remove_index(child1, index2)
    word2 = child2 + (value1 - 1, value2 - 1)
    if west3_applies(word2[-3:]):
        if not (index1 < length - 1 and index2 < len(child1) - 1):
            stop(("position lemma: down/West3 position",
                  seq, index1, child1, index2))
        return "down West3"
    third = leftmost_extractable(child2)
    if third is None:
        stop(("extraction lemma: down third extraction failed",
              length, deficit, half_area_limit, seq, child2))
    index3, value3 = third
    child3 = remove_index(child2, index3)
    word3 = child3 + (value1 - 1, value2 - 1, value3 - 1)
    if not (
        index1 < length - 2
        and index2 < len(child1) - 2
        and index3 < len(child2) - 2
    ):
        stop(("position lemma: down/West5 position",
              seq, index1, child1, index2, child2, index3))
    if not west5_case2b_applies(word3[-5:]):
        stop(("seven-window lemma: down would reach West7",
              length, deficit, half_area_limit, seq, word3[-5:]))
    return "down West5 case 2b"

def main():
    up_counts = Counter()
    down_counts = Counter()
    by_length = {
        length: {"up": Counter(), "down": Counter()}
        for length in range(4, 8)
    }
    for length in range(4, 8):
        for seq in generate_dyck_sequences(length):
            deficit, area = deficit_and_area(seq)
            if deficit > 2 * length - 8:
                continue
            half_area_limit = (comb(length, 2) - deficit) // 2
            if area <= half_area_limit - 1:
                label = check_up_prefix(
                    seq, length, deficit, half_area_limit)
                up_counts[label] += 1
                by_length[length]["up"][label] += 1
            if area <= half_area_limit and not is_special_skeleton(seq):
                label = check_down_prefix(
                    seq, length, deficit, half_area_limit)
                down_counts[label] += 1
                by_length[length]["down"][label] += 1
    print("EverythingOkay = True")
    print("up counts  ", dict(up_counts))
    print("down counts", dict(down_counts))
    print()
    for length in range(4, 8):
        print(f"n={length}")
        print("  up:  ", dict(by_length[length]["up"]))
        print("  down:", dict(by_length[length]["down"]))
    print()
    print("No East7 or West7 branch was reached for 4 <= n <= 7.")
if __name__ == "__main__":
    main()
