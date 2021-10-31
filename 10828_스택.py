import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command = sys.stdin.readline().strip()
    if command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        result = command.split(' ')
        stack.append(int(result[-1]))
