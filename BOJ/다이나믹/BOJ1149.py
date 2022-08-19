import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n + 1)]
# i: 집 1 ~ n, j: 빨강, 초록, 파랑
for i in range(1, n + 1):
    for j in range(3):
        min_v = int(1e9)
        for k in range(3):
            if k != j:
                min_v = min(min_v, dp[i - 1][k])
        dp[i][j] = min_v + graph[i - 1][j]
print(min(dp[n]))