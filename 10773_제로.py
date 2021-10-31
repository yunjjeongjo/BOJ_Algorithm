import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a:
        stack.append(a)
    else:
        if stack:
            stack.pop()

print(sum(stack))
