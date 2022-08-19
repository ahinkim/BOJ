import sys
import heapq
def dijkstra():
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if now == t:
            break
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        

input = lambda : sys.stdin.readline().rstrip()
# 정점의 개수 n, 간선 수 m
n, m = map(int, input().split())
INF = sys.maxsize
distance = [INF] * (n+1)
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
s, t = map(int, input().split())

dijkstra()
print(distance[t])