import sys
input = lambda : sys.stdin.readline().rstrip()
# 대학교 건물의 수 n, 길의 수 m
n, m = map(int, input().split())
INF = sys.maxsize
adj = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 0:
        adj[u][v] = 0
        adj[v][u] = 1
    if b == 1:
        adj[u][v] = 0
        adj[v][u] = 0

for i in range(1, n+1):
    adj[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])

# 질문의 수 k
k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    print(adj[s][e])   