n = int(input())

a = [[] for _ in range(n)]

for i in range(n):
    line = list(input())

    for j in line:
        a[i].append(j)

for i in range(n):
    result = 0
    for j in a[i]:
        if j == '(':
            result += 1
        else:
            result -= 1
        if result < 0:
            print('NO')
            break
    if result > 0:
        print('NO')
    elif result == 0:
        print('YES')
