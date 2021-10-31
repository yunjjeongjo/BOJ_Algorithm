import sys

n = int(sys.stdin.readline())

dp = [-1 for i in range(n + 1)]
if n < 6:
    if n == 3 or n == 5:
        print(1)
    else:
        print(dp[n])
else:

    for i in range(6, n + 1):
        dp[3] = 1
        dp[5] = 1
        if dp[i - 3] == -1 and dp[i - 5] == -1:
            continue
        elif dp[i - 3] == -1:
            dp[i] = dp[i - 5] + 1
        elif dp[i - 5] == -1:
            dp[i] = dp[i - 3] + 1
        else:
            dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)
    print(dp[n])
