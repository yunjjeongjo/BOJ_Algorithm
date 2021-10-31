from collections import deque

n = int(input())

a = [[] for _ in range(n)]
door = []

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

for i in range(n):
    line = input()
    for j in range(n):
        a[i].append(line[j])

for i in range(n):  # 문 위치 미리 파악
    for j in range(n):
        if a[i][j] == '#':
            door.append([i, j])

queue = deque()
mirror = [[[1e9 for _ in range(4)] for _ in range(n)] for _ in range(n)]  # 최댓값으로 초기화

for i in range(4):
    queue.append([door[0][0], door[0][1], i])
    mirror[door[0][0]][door[0][1]][i] = 0  # 최소 거울 갯수 담는 3차원 배열


def bfs():
    while queue:
        x, y, to = queue.popleft()

        ny = y + dx[to]
        nx = x + dy[to]

        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] != '*':
                if a[nx][ny] == '.' or a[nx][ny] == '#':
                    if mirror[x][y][to] < mirror[nx][ny][to]:
                        mirror[nx][ny][to] = mirror[x][y][to]
                        queue.append([nx, ny, to])
                elif a[nx][ny] == '!':  # 거울 설치 가능한 구역
                    if mirror[x][y][to] < mirror[nx][ny][to]:
                        mirror[nx][ny][to] = mirror[x][y][to]
                        queue.append([nx, ny, to])
                    if to == 0 or to == 1:  # 이전 방향이 상, 하 일 때
                        for j in range(2, 4):  # +90도 , -90도 회전
                            to_mirror = j
                            if mirror[x][y][to] < mirror[nx][ny][to_mirror]:
                                mirror[nx][ny][to_mirror] = mirror[x][y][to] + 1
                                queue.append([nx, ny, to_mirror])
                    elif to == 2 or to == 3:  # 이전 방향이 좌, 우 일 때
                        for j in range(0, 2):  # +90도 , -90도 회전
                            to_mirror = j
                            if mirror[x][y][to] < mirror[nx][ny][to_mirror]:
                                mirror[nx][ny][to_mirror] = mirror[x][y][to] + 1
                                queue.append([nx, ny, to_mirror])


bfs()
print(min(mirror[door[1][0]][door[1][1]]))
