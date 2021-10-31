from collections import deque

n, m = map(int, input().split())

a = [[] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    line = input()

    for j in range(m):
        a[i].append(line[j])


def bfs(x, y):
    visited = [[0 for _ in range(m)] for __ in range(n)]
    queue = deque()
    queue.append([x, y])
    cnt = 0
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append([nx, ny])
                    cnt = max(cnt, visited[nx][ny])

    return cnt-1


result = -1

for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
