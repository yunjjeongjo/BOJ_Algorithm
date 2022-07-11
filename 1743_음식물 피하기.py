from collections import deque

n, m, k = map(int, input().split())
path = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(k):
    x, y = map(int, input().split())
    path[x - 1][y - 1] = 1

queue = deque()


def bfs(x, y):
    global cnt
    queue.append([x, y])
    visited[x][y] = 1
    cnt += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and path[nx][ny] == 1:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += 1


result = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if path[i][j] == 1:
            bfs(i, j)
            result = max(result, cnt)
            cnt = 0

print(result)
