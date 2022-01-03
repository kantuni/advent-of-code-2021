xs = list(map(int, input().split(",")))
low = min(xs)
high = max(xs)


def calculate_cost(p):
    cost = 0
    for x in xs:
        diff = abs(x - p)
        cost += diff * (diff + 1) // 2
    return cost

ans = float("inf")
for x in range(low, high + 1):
    cost = calculate_cost(x)
    ans = min(ans, cost)

print(ans)
