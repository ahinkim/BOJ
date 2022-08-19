import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
dp = [0] * (n + 1)
dp[0:3] = [1, 2, 7]

total = 0
for i in range(3, n + 1):
    total += dp[i - 3]
    dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3 + total * 2) % 1000000007

print(dp[n])