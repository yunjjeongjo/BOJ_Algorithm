from sys import stdin
from collections import deque

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    visited = [[float('inf')] * w for _ in range(h)]  # 배열 최댓값으로 초기화
    visited[start_x][start_y] = -1
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        if (x, y) == (end_x, end_y):
            return visited[end_x][end_y]

        # 4방향으로 각각 직진
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if not (0 <= nx < h and 0 <= ny < w):  # 격자 벗어나거나
                    break
                if a[nx][ny] == "*":  # 벽 만나면 break
                    break
                if visited[nx][ny] < visited[x][y] + 1:  # 이동할 위치에 있는 거울이 현재까지 사용한 거울+1보다 작으면 갱신 X
                    break
                queue.append((nx, ny))  # 새 위치 이동
                visited[nx][ny] = visited[x][y] + 1
                # 직진
                nx += dx[i]
                ny += dy[i]


# main
w, h = map(int, input().split())
a, target = [], []
start_x, start_y, end_x, end_y = 0, 0, 0, 0
for i in range(h):
    a.append(list(input().strip()))
    for j in range(w):
        if a[i][j] == "C":
            target.append((i, j))
(start_x, start_y), (end_x, end_y) = target
print(bfs())
