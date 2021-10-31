n = int(input())
a = list(map(int, input().split()))
d = [1 for i in range(n)]
result = []

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

max_val = max(d)
for i in range(len(d) - 1, -1, -1):
    if d[i] == max_val:
        result.append(a[i])
        max_val -= 1

print(max(d))
result.reverse()
for i in result:
    print(i, end=" ")
