import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(2, n + 1, 2):
    dp[i] += dp[i - 2] * 3
    for j in range(4, i + 1, 2):
        dp[i] += dp[i - j] * 2
print(dp[n])