import sys
from collections import deque
def bfs(start, end):
    global route
    # 시작 지접, 거리, 경로
    q = deque([(start, 0, [start])])
    visited[start] = True
    while q:
        now, d, r  = q.popleft()
        if now == end:
            route = r
            return d
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append((i, d + 1, r + [i]))
    return 0
input = lambda : sys.stdin.readline().rstrip()
# 정점의 개수 n, 두 정점 사이를 잇는 도로의 개수 m
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 사전순으로 정렬
for i in range(1, n + 1):
    graph[i].sort()
start, end = map(int, input().split())

visited = [False] * (n + 1)
# start ~ end 경로
route = []
res = 0
res += bfs(start, end)
visited = [False] * (n + 1)
for x in route[1:]:
    visited[x] = True
res += bfs(end, start)
print(res)