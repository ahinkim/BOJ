t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, 4):
            if i >= j:
                dp[i] += dp[i - j]
    print(dp[n])