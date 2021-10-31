n, m = map(int, input().split())

a = list(map(int, input().split()))

start = 0
end = max(a)

while start <= end:
    result = 0
    mid = (start + end) // 2

    for i in a:
        if i >= mid:
            result += i - mid
    if result >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
