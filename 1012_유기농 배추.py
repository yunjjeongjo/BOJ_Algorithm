from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(y, x):
    queue = deque([])
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if cabbage[ny][nx] == 1:
                    queue.append([ny, nx])
                    cabbage[ny][nx] = 0
    return


for i in range(t):
    m, n, k = map(int, input().split())

    cabbage = [[0] * (m) for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    cnt = 0

    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
