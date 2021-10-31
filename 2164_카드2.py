from collections import deque
n = int(input())

queue = deque()
for i in range(n):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    value = queue.popleft()
    queue.append(value)

print(queue.popleft())

