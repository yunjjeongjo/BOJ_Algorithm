from collections import deque

test_case = int(input())

for i in range(test_case):
    flag = True
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    queue = deque(a)
    result_index = m
    result=0

    while flag:
        max_value = max(queue)
        pop_value = queue.popleft()

        if pop_value < max_value: # 출력 안함
            if result_index == 0:
                result_index += n-1
            else:
                result_index -= 1
            queue.append(pop_value)

        else: # 출력함
            if result_index == 0:
                result += 1
                flag=False
            else:
                result += 1
                result_index -= 1
                n -= 1

    print(result)