INF = int(1e10)
N = 10
adj = [[INF]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    adj[i][i] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            adj[a][b] = min(adj[a][b], adj[a][k]+adj[k][b])