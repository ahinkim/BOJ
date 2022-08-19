import sys
input = lambda : sys.stdin.readline().rstrip()
# 회원의 수
N = int(input())
INF = int(1e9)
adj = [[INF] * (N + 1) for _ in range(N + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    adj[a][b] = 1
    adj[b][a] = 1

for i in range(1, N + 1):
    adj[i][i] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])
    
scores = []
for i in range(1, N + 1):
    # 친구사이의 거리 중 최대값
    scores.append((max(adj[i][1:])))

res = []
min_score = min(scores)
for i in range(N):
    # 친구사이의 거리가 가장 작은 회원 추가
    if scores[i] == min_score:
        res.append(i+1)

print(min_score, len(res))
print(*res)