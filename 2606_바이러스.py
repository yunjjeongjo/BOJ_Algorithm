n = int(input())
m = int(input())
a = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

result = 0


def dfs(a, visited, v):
    global result
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            dfs(a, visited, i)
            result += 1


dfs(a, visited, 1)
print(result)
