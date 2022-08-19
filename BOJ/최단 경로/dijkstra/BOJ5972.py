import sys
import heapq
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

input = lambda : sys.stdin.readline().rstrip()
# 헛간의 개수, 양방향 길의 개수
N, M = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


dijkstra(1)
print(distance[N])