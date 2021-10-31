import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()

print(round(sum(a) / len(a)))
print(a[len(a) // 2])
cnt_a = Counter(a).most_common()
if len(cnt_a) > 1 and cnt_a[0][1] == cnt_a[1][1]:
    print(cnt_a[1][0])
else:
    print(cnt_a[0][0])

print(a[len(a) - 1] - a[0])
