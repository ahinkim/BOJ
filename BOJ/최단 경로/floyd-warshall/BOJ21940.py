import sys
input = lambda : sys.stdin.readline().rstrip()
# 도시의 개수 N, 도로의 개수 M
N, M = map(int, input().split())
INF = int(1e9)
adj = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    adj[A][B] = T

for i in range(1, N+1):
    adj[i][i] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])

# 준형이와 친구들의 총 인원 K
K = int(input())
# 살고 있는 도시 번호
city_nums = list(map(int, input().split())) 

min_v = INF
res = []
for i in range(1, N+1):
    max_v = 0
    for num in city_nums:
        max_v = max(max_v, adj[i][num] + adj[num][i])
    if max_v < min_v:
        min_v = max_v
        res = [i]
    elif max_v == min_v:
        res.append(i)

res.sort()
print(*res, sep=' ')