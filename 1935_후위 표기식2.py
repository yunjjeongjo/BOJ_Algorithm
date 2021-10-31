n = int(input())
s = list(input())
a = []
stack = []
for i in range(n):
    a.append(input())

for i in s:
    if 65 <= ord(i) <= 90:
        stack.append(int(a[ord(i) - 65]))
    else:
        s2 = stack.pop()
        s1 = stack.pop()

        if i == '+':
            stack.append(s1 + s2)
        elif i == '-':
            stack.append(s1 - s2)
        elif i == '*':
            stack.append(s1 * s2)
        elif i == '/':
            stack.append(s1 / s2)

print("%0.2f" % stack[0])
