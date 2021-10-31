n = int(input())

d = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    d[i] = i
    for j in range(1, i):
        if j * j > i:
            break
        if d[i] > d[i - j * j] + 1:
            d[i] = d[i - j * j] + 1

print(d[n])
