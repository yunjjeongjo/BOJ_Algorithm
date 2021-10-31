k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]

start = 1
end = max(a)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in a:
        result += i // mid
    if result >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
