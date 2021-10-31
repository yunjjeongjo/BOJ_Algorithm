n = int(input())
a = list(map(int, input().split()))
d = [1000 * 10000 for i in range(n + 1)]

d[0] = 0

for i in range(1, n + 1):
    for j in range(i):
        d[i] = min(d[i], a[j] + d[i - j - 1])

print(d[n])
