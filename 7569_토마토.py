from collections import deque

m, n, h = map(int, input().split())

tomato = [[[] for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        line = list(map(int, input().split()))
        for k in range(m):
            tomato[i][j].append(line[k])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if tomato[nx][ny][nz] == 0:
                    tomato[nx][ny][nz] = tomato[x][y][z] + 1
                    queue.append([nx, ny, nz])


for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k])

bfs()

flag = 1
result = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                flag = 0
            result = max(result, tomato[i][j][k])

if flag == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)
