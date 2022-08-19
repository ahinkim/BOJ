import sys
input = lambda: sys.stdin.readline().rstrip()
v, e = map(int, input().split())
INF = int(1e9)
adj = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a][b] = c

for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])

res = INF
for i in range(1, v + 1):
    res = min(res, adj[i][i])

if res == INF:
    print(-1)
else:
    print(res)