from sys import stdin

lines = []
for line in stdin:
    lines.append(line.strip())

BRACKET_TO_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
BRACKET_MAPPING = {"(": ")", "[": "]", "{": "}", "<": ">"}


def is_incomplete(line: str) -> int:
    """Returns number of points needed to complete the line, 0 otherwise."""
    score = 0
    s = []
    for bracket in line:
        if bracket in BRACKET_MAPPING.keys():
            # opening
            s.append(bracket)
        else:
            # closing
            opening = s.pop()
            if BRACKET_MAPPING[opening] != bracket:
                break
    else:
        for opening in reversed(s):
            closing = BRACKET_MAPPING[opening]
            score = score * 5 + BRACKET_TO_POINTS[closing]

    return score


scores = []
for line in lines:
    score = is_incomplete(line)
    if score > 0:
        scores.append(score)

scores.sort()
ans = scores[len(scores) // 2]
print(ans)
