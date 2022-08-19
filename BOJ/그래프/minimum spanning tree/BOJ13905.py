import sys
from collections import deque
sys.setrecursionlimit(10**6)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# 목표 위치까지 들고 갈 수 있는 무게 구하기
def bfs(v):
    res = 0
    INF = sys.maxsize
    q = deque([(v, INF)])
    visited[v] = True
    while q:
        now, cost = q.popleft()
        if now == e:
            res = cost
            break
        for i in adj[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                q.append((i[0], min(cost, i[1])))
    return res

input = lambda : sys.stdin.readline().rstrip()
# 섬에 존재하는 집의 수 N, 다리의 수 M
N, M = map(int, input().split())
# 숭이의 출발 위치 s, 혜빈이의 위치 e
s, e = map(int, input().split())

edges = []
parent = [i for i in range(N+1)]
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 다리의 정보
for _ in range(M):
    h1, h2, k = map(int, input().split())
    edges.append((k, h1, h2))
edges.sort(reverse = True)

# 무게 제한이 높은 다리 순서로 모든 집을 연결한다.
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        adj[a].append((b, cost))
        adj[b].append((a, cost))
print(bfs(s))