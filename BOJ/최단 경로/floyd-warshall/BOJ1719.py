import sys
input = lambda : sys.stdin.readline().rstrip()
# 집하장의 개수 n, 집하장 간의 경로의 개수 m
n, m = map(int, input().split())
INF = int(1e9)
adj = [[INF] * (n + 1) for _ in range(n + 1)]
# 거쳐야 하는 집하장의 정보
info = [[-1] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a][b] = c
    adj[b][a] = c
    info[a][b] = b
    info[b][a] = a
for i in range(1, n + 1):
    adj[i][i] = 0
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if adj[a][k] + adj[k][b] < adj[a][b]:
                adj[a][b] = adj[a][k] + adj[k][b]
                info[a][b] = info[a][k]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            print("-", end = ' ')
        else:
            print(info[a][b], end = ' ')
    print()