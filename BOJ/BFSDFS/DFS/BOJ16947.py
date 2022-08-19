# 지금까지 했던 게 한방향 그래프여서 dfs로 풀 수 있었나..
import sys
from collections import deque
sys.setrecursionlimit(10**7)
def dfs(v, prev, route):
    global res_route
    if finished[v]:
        return
    # 사이클일 때
    if visited[v]:
        # 이 부분 안쓰면 사이클 이외에도 사이클까지 가는 길까지 다 저장한다. 예외처리 잘 해주자.
        idx = route.index(v)
        res_route = route[idx:]
        return
    visited[v] = True
    route.append(v)
    for i in graph[v]:
        # 직전 방문지가 아닐 때
        if prev != i:
            new = route[:]
            dfs(i, v, new) # 처음에 new로 할당안해주고 그냥 route그대로 넘겨서 값이 틀렸었다.
    finished[v] = True

def bfs(v):
    q = deque([(v, 0)])
    visited[v] = True
    while q:
        v, d = q.popleft()
        if cycle[v]:
            return d
        for i in graph[v]:
            if not visited[i]: # not visited[v]라고 해서 값이 틀렸었다. 
                q.append((i, d + 1))
                visited[i] = True

input = lambda : sys.stdin.readline().rstrip()
n = int(input())
visited = [False] * (n + 1)
finished = [False] * (n + 1)
# 순환선에 속해 있는 역들
cycle = [False] * (n + 1)
# 순환선 사이의 거리
distance = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 사이클 찾기
res_route = []
dfs(1, -1, [])
for x in res_route:
    cycle[x] = True

# 순환선 사이의 최소 거리 구하기
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if not cycle[i]:
        distance[i] = bfs(i)

print(*distance[1:])