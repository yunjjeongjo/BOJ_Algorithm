from sys import stdin
stack1 = list(stdin.readline().strip())
n = int(input())

stack2 = []

for i in range(n):

    command = list(stdin.readline().strip())

    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(command[2])

stack2 = stack2[::-1]

print("".join(stack1 + stack2))
