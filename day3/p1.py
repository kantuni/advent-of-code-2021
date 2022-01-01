from collections import defaultdict
from sys import stdin

memo = defaultdict(int)
for line in stdin:
    for i, c in enumerate(line.strip()):
        memo[i] += 1 if c == "1" else -1

gamma = ""
epsilon = ""

for value in memo.values():
    gamma += "1" if value > 0 else "0"
    epsilon += "0" if value > 0 else "1"

ans = int(gamma, 2) * int(epsilon, 2)
print(ans)
