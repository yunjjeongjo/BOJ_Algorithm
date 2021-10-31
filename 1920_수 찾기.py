import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

a.sort()


def binary(x):
    min_value = 0
    max_value = len(a) - 1
    while min_value <= max_value:
        mid = (min_value + max_value) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            min_value = mid + 1
        else:
            max_value = mid - 1
    return 0


for i in range(m):
    result = binary(b[i])
    print(result)
