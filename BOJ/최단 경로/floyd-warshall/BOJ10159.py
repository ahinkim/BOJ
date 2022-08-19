import sys
input = lambda : sys.stdin.readline().rstrip()
# 물건의 개수
N = int(input())
# 물건 쌍의 개수
M = int(input())
adj = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    # a>b
    adj[a][b] = 2
    # b<a
    adj[b][a] = 1

for i in range(1, N+1):
    adj[i][i] = 2

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if adj[a][k] == 2 and adj[k][b] == 2:
                adj[a][b] = 2
                adj[b][a] = 1 

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if not adj[i][j]:
            cnt += 1
    print(cnt)