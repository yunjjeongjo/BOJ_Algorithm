from collections import deque

n, k = map(int, input().split())

queue = deque()
result = []

for i in range(n):
    queue.append(i + 1)

while queue:

    for i in range(k - 1):
        value = queue.popleft()
        queue.append(value)
    value_result = queue.popleft()
    result.append(value_result)
print("<", end='')
for i in range(n - 1):
    print(result[i], end=', ')
print(result[-1], end='')
print(">")
