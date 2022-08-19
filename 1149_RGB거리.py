n = int(input())
cost = [[] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in line:
        cost[i].append(j)
for i in range(1, n):
    cost[i][0] = min(cost[i - 1][1], cost[i - 1][2]) + cost[i][0]
    cost[i][1] = min(cost[i - 1][2], cost[i - 1][0]) + cost[i][1]
    cost[i][2] = min(cost[i - 1][1], cost[i - 1][0]) + cost[i][2]

print(min(cost[i][0], cost[i][1], cost[i][2]))
