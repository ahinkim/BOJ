# 물품의 수 N, 버틸 수 있는 무게 K
N, K = map(int, input().split())
# 물건의 무게와 가치 리스트
info = [(0, 0)] 
for _ in range(N):
  # 무게 W, 가치 V
  W, V = map(int, input().split())
  info.append((W, V))
# row: 물건, col: 무게
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  for j in range(1, K + 1):
    # 물건의 무게가 물건을 버틸 수 있는 배낭의 무게보다 클 때 
    if info[i][0] > j:
      # 현재까지의 최대값 저장
      dp[i][j] = dp[i - 1][j]
      continue
    # 해당 물건을 담았을 때의 가치와 담지 않았을 때의 가치 중 더 큰 값 저장
    dp[i][j] = max(dp[i - 1][j - info[i][0]] + info[i][1], dp[i - 1][j])

print(dp[N][K])
