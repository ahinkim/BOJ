import sys
from collections import deque
def bfs(v):
    # 해킹할 수 있는 컴퓨터의 개수
    cnt = 0
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        cnt += 1
        for i in adj[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return cnt

input = lambda : sys.stdin.readline().rstrip()

# 컴퓨터의 개수 N, 신뢰하는 관계 수 M
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj[B].append(A)

visited = [False] * (N+1)
com = [0] * (N+1)
for i in range(1, N+1):
    visited = [False] * (N+1)
    cnt = bfs(i)
    com[i] = cnt

max_v = max(com)
for i in range(1, N+1):
    if com[i] == max_v:
        print(i, end=' ')