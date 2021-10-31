from collections import deque

m, n = map(int, input().split())

a = [[] for i in range(n)]
visited = [[0 for i in range(m)] for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        a[i].append(line[j])
queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0:
                    a[nx][ny] = a[x][y] + 1
                    queue.append([nx, ny])


for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            queue.append([i, j])
bfs()

flag = 1
result = -1

for i in a:
    for j in i:
        if j == 0:
            flag = 0
        result = max(result, j)

if flag == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)
