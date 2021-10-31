import sys

n, m, b = map(int, sys.stdin.readline().split())

a = [[] for _ in range(n)]

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        a[i].append(line[j])

min_value = min(min(a))
max_value = max(max(a))

result_time = 1e9

for k in range(min_value, max_value + 1):
    cnt_out = 0
    cnt_in = 0
    for i in range(n):
        for j in range(m):
            flag = a[i][j] - k
            if flag > 0:
                cnt_in += flag
            elif flag < 0:
                cnt_out += -flag
    if b - cnt_out + cnt_in >= 0:
        time = cnt_in * 2 + cnt_out

        if result_time >= time:
            result_time = time
            result_height = k

print(result_time, result_height)
