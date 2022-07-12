from collections import deque

n, m = map(int, input().split())
visited = [[False] * n for _ in range(m)]
map = [[] for _ in range(m)]
for i in range(m):
    line = list(input())
    for j in line:
        map[i].append(j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result_w = 0
result_b = 0


def bfs(x, y):
    if not visited[x][y]:
        global result_w, result_b
        w_b = map[x][y]
        cnt = 1
        queue = deque()
        queue.append([x, y])
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[nx][ny] and map[x][y] == map[nx][ny]:
                        queue.append([nx, ny])
                        visited[nx][ny] = True
                        cnt += 1
        if w_b == 'W':
            result_w += cnt * cnt
        else:
            result_b += cnt * cnt


for i in range(m):
    for j in range(n):
        bfs(i, j)

print(result_w, result_b)
