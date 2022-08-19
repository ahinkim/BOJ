import sys
import heapq
def dijkstra():
    q = []
    distance[start] = 0 
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
# 도시의 개수
N = int(input())
# 버스의 개수
M = int(input())
graph = [[] for _ in range(N + 1)]
INF = int(1e9)
distance = [INF] * (N + 1)

for _ in range(M):
    # 출발지, 도착지, 버스 비용
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
# 출발점, 도착점
start, end = map(int, input().split())
dijkstra()
print(distance[end])