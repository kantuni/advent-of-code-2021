xs = list(map(int, input().split(",")))
low = min(xs)
high = max(xs)


def calculate_cost(p):
    return sum(map(lambda x: abs(x - p), xs))


ans = float("inf")
for x in range(low, high + 1):
    cost = calculate_cost(x)
    ans = min(ans, cost)

print(ans)
