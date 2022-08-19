import sys
sys.setrecursionlimit(10**6)
def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for i in adj[v]:
        if not visited[i]:
            dfs(i)

input = lambda : sys.stdin.readline().rstrip()
# 민상이가 작업할 개수 N, 작업 순서 정보의 개수 M
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    # A작업이 끝나야 B작업 가능
    A, B = map(int, input().split())
    # 반대로 저장
    adj[B].append(A)

X = int(input())

cnt = 0
dfs(X)
print(cnt - 1)