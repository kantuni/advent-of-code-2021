from sys import stdin

lines = []
for line in stdin:
    lines.append(line.strip())

BRACKET_TO_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
BRACKET_MAPPING = {"(": ")", "[": "]", "{": "}", "<": ">"}


def is_corrupted(line: str) -> int:
    """Returns number of points for the first corrupted character, 0 otherwise."""
    s = []
    for bracket in line:
        if bracket in BRACKET_MAPPING.keys():
            # opening
            s.append(bracket)
        else:
            # closing
            opening = s.pop()
            if BRACKET_MAPPING[opening] != bracket:
                return BRACKET_TO_POINTS[bracket]
    return 0


ans = 0
for line in lines:
    ans += is_corrupted(line)

print(ans)
