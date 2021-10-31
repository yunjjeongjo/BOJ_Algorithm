import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

box = [list(input()) for i in range(n)]
result = 0


def rows():
    global result
    for i in range(n):
        cnt = 1
        for j in range(0, n - 1):
            if box[i][j] == box[i][j + 1]:
                cnt += 1
            else:
                if result < cnt:
                    result = cnt
                cnt = 1
        if result < cnt:
            result = cnt


def columns():
    global result
    for i in range(n):
        cnt = 1
        for j in range(0, n - 1):
            if box[j][i] == box[j + 1][i]:
                cnt += 1
            else:
                if result < cnt:
                    result = cnt
                cnt = 1
        if result < cnt:
            result = cnt


for i in range(n):
    for j in range(0, n - 1):
        box[i][j], box[i][j + 1] = box[i][j + 1], box[i][j]
        rows()
        columns()
        box[i][j + 1], box[i][j] = box[i][j], box[i][j + 1]

for i in range(n):
    for j in range(0, n - 1):
        box[j][i], box[j + 1][i] = box[j + 1][i], box[j][i]
        rows()
        columns()
        box[j + 1][i], box[j][i] = box[j][i], box[j + 1][i]

print(result)
