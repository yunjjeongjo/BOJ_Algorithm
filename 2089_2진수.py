n = int(input())

result = ''


def func(a, b):
    global result
    if a != 0:
        if a % 2 == 0:
            result = '0' + result
            func(a // b, b)
        else:
            result = '1' + result
            func(a // b + 1, b)
    else:
        result = '0' + result


func(n, -2)

print(int(result))
