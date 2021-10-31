n = int(input())
a = [[] for _ in range(n)]
visited = [[0] * n for _ in range(n)]
for i in range(n):
    line = input()
    for j in line:
        a[i].append(int(j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

house = 0  # 단지내 집의 수
cnt = 0  # 총 단지수


def dfs(a, visited, x, y):
    visited[x][y] = 1
    global house

    if a[x][y] == 1:
        house += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and a[x][y] == 1:
                dfs(a, visited, nx, ny)


house_list = []

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and a[i][j] == 1:
            dfs(a, visited, i, j)
            house_list.append(house)
            house = 0
            cnt += 1

print(cnt)
house_list.sort()
for i in house_list:
    print(i)
