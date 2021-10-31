from collections import deque

n, m, v = map(int, input().split())
a = [[0 for i in range(n + 1)] for i in range(n + 1)]

visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1
    a[y][x] = 1


def dfs(a, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if not visited[i] and a[v][i] == 1:
            dfs(a, visited, i)


def bfs(a, visited, v):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(v)
    while queue:
        value = queue.popleft()
        visited[value] = True
        print(value, end=' ')
        for i in range(1, n + 1):
            if not visited[i] and a[value][i] == 1:
                queue.append(i)
                visited[i] = True


dfs(a, visited, v)
print('')
bfs(a, visited, v)
