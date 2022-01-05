from collections import defaultdict
from functools import reduce
from sys import stdin
from typing import Dict, List


entries = []
for line in stdin:
    patterns, output = line.strip().split(" | ")
    entries.append((patterns.split(), output.split()))

# digit: number of segments & letters
# 0: 6 {abcefg}
# 1: 2 {cf}
# 2: 5 {acdeg}
# 3: 5 {acdfg}
# 4: 4 {bcdf}
# 5: 5 {abdfg}
# 6: 6 {abdefg}
# 7: 3 {acf}
# 8: 7 {abcdefg}
# 9: 6 {abcdfg}

# (Henrikh)
# Known segments: {}
# 1) 7{acf} - 1{cf} = {a}
# Known segments: {a}
# 2) 2{acdeg} & 3{acdfg} & 5{abdfg} & 4{bcdf} = {d}
# Known segments: {a, d}
# 3) 4{bcdf} - 1{cf} - {d} = {b}
# Known segments: {a, b, d}
# 4) 2{acdeg} & 3{acdfg} & 5{abdfg} = {adg} - {a} - {d} = {g}
# Known segments: {a, b, d, g}
# 5) 0{abcdefg} & 6{abdefg} & 9{abcdfg} = {abdfg} - {a} - {b} - {d} - {g} = {f}
# Known segments: {a, b, d, f, g}
# 6) 1{cf} - {f} = {c}
# Known segments: {a, b, c, d, f, g}
# 7) 8{abcdefg} - {a} - {b} - {c} - {d} - {f} - {g} = {e}
# Known segments: {a, b, c, d, e, f, g}

# (Karen)
# Known segments: {}
# 1) 7{acf} - 1{cf} = {a}
# Known segments: {a}
# 2) 2{acdeg} + 3{acdfg} + 5{abdfg} = {aaabccdddeffggg} in 4{bcdf} -> {b} else {e}
# Known segments: {a, b, e}
# 3) 4{bcdf} - 1{cf} - {b} = {d}
# Known segments: {a, b, d, e}
# 4) 0{abcdefg} + 6{abdefg} + 9{abcdfg} = {aaabbbccddeefffggg} - {d}* - {e}* = {c}
# Known segments: {a, b, c, d, e}
# 5) 1{cf} - {c} = {f}
# Known segments: {a, b, c, d, e, f}
# 5) 8{abcdefg} - {a} - {b} - {c} - {d} - {e} - {f} = {g}


def decode(patterns: List[str]) -> Dict[str, str]:
    mapping = dict()
    memo = defaultdict(list)
    for pattern in patterns:
        memo[len(pattern)].append(set(pattern))

    # 1 has 2 segments
    one = memo[2][0]
    # 4 has 4 segments
    four = memo[4][0]
    # 7 has 3 segments
    seven = memo[3][0]
    # 8 has 7 segments
    eight = memo[7][0]
    # 2, 3, 5 have 5 segments
    two_three_five = memo[5]
    # 0, 6, 9 has 6 segments
    zero_six_nine = memo[6]

    # 1) 7{acf} - 1{cf} = {a}
    a = seven.difference(one)
    mapping["a"] = next(iter(a))

    # 2) 2{acdeg} & 3{acdfg} & 5{abdfg} & 4{bcdf} = {d}
    d = reduce(lambda a, b: a.intersection(b), [*two_three_five, four])
    mapping["d"] = next(iter(d))

    # 3) 4{bcdf} - 1{cf} - {d} = {b}
    b = four.difference(one).difference(d)
    mapping["b"] = next(iter(b))

    # 4) 2{acdeg} & 3{acdfg} & 5{abdfg} - {a} - {d} = {g}
    g = (
        reduce(lambda a, b: a.intersection(b), two_three_five)
        .difference(a)
        .difference(d)
    )
    mapping["g"] = next(iter(g))

    # 5) 0{abcdefg} & 6{abdefg} & 9{abcdfg} - {a} - {b} - {d} - {g} = {f}
    f = (
        reduce(lambda a, b: a.intersection(b), zero_six_nine)
        .difference(a)
        .difference(b)
        .difference(d)
        .difference(g)
    )
    mapping["f"] = next(iter(f))

    # 6) 1{cf} - {f} = {c}
    c = one.difference(f)
    mapping["c"] = next(iter(c))

    # 7) 8{abcdefg} - {a} - {b} - {c} - {d} - {f} - {g} = {e}
    e = (
        eight.difference(a)
        .difference(b)
        .difference(c)
        .difference(d)
        .difference(f)
        .difference(g)
    )
    mapping["e"] = next(iter(e))

    return mapping


SEGMENT_TO_DIGIT = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

ans = 0
for patterns, output in entries:
    mapping = decode(patterns)
    num = 0
    for value in output:
        table = {ord(v): ord(k) for k, v in mapping.items()}
        translated = value.translate(table)
        segment = "".join(sorted(translated))
        num = num * 10 + SEGMENT_TO_DIGIT[segment]

    ans += num

print(ans)
