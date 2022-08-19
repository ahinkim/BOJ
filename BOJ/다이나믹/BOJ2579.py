# 계단의 개수
n = int(input())
score = []
dp = [0]*n
for _ in range(n):
    # 각 계단의 점수
    score.append(int(input()))

dp[0] = score[0]
if n > 1:
    dp[1] = score[0]+score[1]
if n > 2:
    dp[2] = max(score[0]+score[2], score[1]+score[2])
for i in range(3, n):
    dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])

print(dp[n-1])