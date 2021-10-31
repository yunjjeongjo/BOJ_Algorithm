def func():
    stack = []
    for i in line:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
                return 0
            elif stack[-1] == '[':
                return 0
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack:
                return 0
            elif stack[-1] == '(':
                return 0
            elif stack[-1] == '[':
                stack.pop()
    if not stack:
        return 1
    else:
        return 0


while True:
    line = input()

    if line == '.':
        break
    else:
        if func():
            print('yes')
        else:
            print('no')
