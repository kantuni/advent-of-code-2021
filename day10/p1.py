from sys import stdin

lines = []
for line in stdin:
    lines.append(line.strip())

BRACKET_TO_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

BRACKET_MAPPING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

ans = 0
for line in lines:
    s = []
    for bracket in line:
        if bracket in BRACKET_MAPPING.keys():
            # opening
            s.append(bracket)
        else:
            # closing
            opening = s.pop()
            if BRACKET_MAPPING[opening] != bracket:
                ans += BRACKET_TO_POINTS[bracket]
                break

print(ans)
