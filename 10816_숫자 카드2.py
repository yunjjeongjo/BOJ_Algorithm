from collections import Counter

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
cnt_a = Counter(a)


def binary_search(n):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if n == a[mid]:
            return 1
        elif n > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in range(m):
    if binary_search(b[i]):
        if b[i] in cnt_a:
            print(cnt_a[b[i]], end=' ')
    else:
        print(0, end=' ')
