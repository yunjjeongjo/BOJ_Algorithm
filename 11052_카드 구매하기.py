n = int(input())
a = list(map(int, input().split()))
d = [0 for i in range(n)]
d[0] = a[0]

for i in range(1, n):
    for j in range(0, n):
        if j == n - 1:
            d[i] = a[j]
        d[i] = a[j] + d[n - 1 - j]

print(max(d))
