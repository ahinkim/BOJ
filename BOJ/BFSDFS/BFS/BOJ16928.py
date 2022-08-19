from collections import deque
def bfs():
    res = INF
    q = deque([(1, 0)])
    while q:
        now, dist = q.popleft()
        if now == 100:
            res = min(res, dist)

        if dist < visited[now]:
            visited[now] = dist
            if graph[now] != -1: 
                q.append((graph[now], dist))
            else:
                for i in range(1, 7):
                    if now+i <= 100:
                        q.append((now+i, dist+1))
    return res

INF = int(1e9)
graph = [-1] * 101
visited = [INF] * 101
# 사다리의 수 N, 뱀의 수 M
N, M = map(int, input().split())

# 사다리의 정보
for _ in range(N):
    x, y = map(int, input().split())
    graph[x] = y
# 뱀의 정보
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = v

print(bfs())