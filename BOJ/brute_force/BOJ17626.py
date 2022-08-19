from math import sqrt
n = int(input())
array = [i**2 for i in range(1, int(sqrt(n)) + 1)]
INF = int(1e9)
dp = [INF] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(len(array)):
        if i < array[j]:
            break
        dp[i] = min(dp[i], dp[i - array[j]] + 1)

print(dp[n])