n = int(input())
a = [int(input()) for _ in range(n)]
result = []
stack = []
cnt = 0
flag = True
for i in a:
    while cnt < i:
        cnt += 1
        stack.append(cnt)
        result.append("+")
    if stack[-1] == i:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break
if not flag:
    print("NO")
else:
    for i in result:
        print(i)
