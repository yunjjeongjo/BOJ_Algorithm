s = list(input())
flag = False
word = ''
result = ''

for i in s:
    if not flag: #괄호 안이 아님
        if i == '<':
            flag = True
            word += i
        elif i == ' ':
            word += i
            result += word
            word = ''
        else:
            word = i + word
    else: #괄호 안
        word += i
        if i == '>':
            flag = False
            result += word
            word = ''

print(result + word)
