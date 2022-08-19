import sys
import heapq
def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    cnt = 0
    while q:
        dist, now = heapq.heappop(q)
        if now == start:
            cnt += 1
        # 사이클이 있는 경우
        if cnt == 2:
            return dist
        if dist < distance[now]:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if start == i[0] or cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # 사이클이 없는 경우
    return -1

input = lambda: sys.stdin.readline().rstrip()
v, e = map(int, input().split())
adj = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

INF = int(1e9)
res = INF
for i in range(1, v + 1):
    distance = [INF] * (v + 1)
    cost = dijkstra(i, distance)
    if cost == -1:
        continue
    res = min(res, cost)

if res == INF:
    print(-1)
else:
    print(res)