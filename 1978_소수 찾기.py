n = int(input())
a = list(map(int, input().split()))

cnt = 0


def prime(num):
    if num == 1:
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True


for i in a:
    if prime(i):
        cnt += 1
print(cnt)
