from collections import deque

r, c = map(int, input().split())

a = [[] for _ in range(r)]
cnt = [[0 for i in range(c)] for i in range(r)]  # 이동 시간 기록

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    line = input()
    for j in range(c):
        a[i].append(line[j])

queue = deque()

for i in range(r):
    for j in range(c):
        if a[i][j] == '*':
            queue.append([i, j])  # 물 처음 차있는 위치 좌표
        elif a[i][j] == 'S':
            start_x, start_y = i, j  # 고슴도치 처음 위치 좌표
        elif a[i][j] == 'D':
            target_x, target_y = i, j  # 목적지 좌표
queue.append([start_x, start_y])

flag = 0  # 비버의 굴 만나면 while문 탈출하기 위한 flag


def bfs():
    global flag
    while queue:
        x, y = queue.popleft()
        if flag == 1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if a[x][y] == '*' and a[nx][ny] == '.':  # 물이 고슴도치보다 먼저 이동해야함
                    a[nx][ny] = '*'
                    queue.append([nx, ny])
                if a[x][y] == 'S':  # 고슴도치 이동
                    if a[nx][ny] == '.':  # 이동 할 수 있는 지역일때
                        a[nx][ny] = 'S'
                        cnt[nx][ny] = cnt[x][y] + 1
                        queue.append([nx, ny])
                    if a[nx][ny] == 'D':  # 비버의 굴 만났을때
                        flag = 1
                        cnt[nx][ny] = cnt[x][y] + 1
                        break


bfs()

if cnt[target_x][target_y] == 0:  # 비버의 굴에 도달하지 못했음
    print('KAKTUS')
else:
    print(cnt[target_x][target_y])  # 비버의 굴까지 얼마나 걸렸는지
