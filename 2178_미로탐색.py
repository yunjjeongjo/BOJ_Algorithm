from collections import deque

n, m = map(int, input().split())
map = [[] for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    line = input()
    for j in range(m):
        map[i].append(int(line[j]))


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and map[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])


bfs(0, 0)

print(visited[n - 1][m - 1] + 1)
