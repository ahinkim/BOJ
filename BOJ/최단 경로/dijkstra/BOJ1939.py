import sys
import heapq
def dijkstra(distance, start, limit):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            if i[1] < limit:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def binary(start, end):
    while start <= end:
        distance = [INF] * (n + 1)
        mid = (start + end) // 2
        dijkstra(distance, S, mid)
        if distance[E] < INF:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result
# 섬의 개수 n, 다리의 개수 m
input = lambda : sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e20)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
# 공장이 위치해 있는 섬의 번호   
S, E = map(int, input().split())
print(binary(1, 1000000000))