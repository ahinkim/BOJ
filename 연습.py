import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop()
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = i[0] + dist
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


INF = int(1e10)
N = 10
adj = [[] for _ in range(N+1)]
distance = [INF]*(N+1)