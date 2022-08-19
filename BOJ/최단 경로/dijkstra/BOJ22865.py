import sys
import heapq
def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

input = lambda : sys.stdin.readline().rstrip()
# 자취할 땅 후보의 개수 N
N = int(input())
# 친구 A, B, C가 사는 위치
A, B, C = map(int, input().split())
# 도로의 개수 M
M = int(input())
adj = [[] for _ in range(N+1)]
INF = int(1e10)
distance_a = [INF] * (N+1)
distance_b = [INF] * (N+1)
distance_c = [INF] * (N+1)

for _ in range(M):
    D, E, L = map(int, input().split())
    adj[D].append((E, L))
    adj[E].append((D, L))

dijkstra(A, distance_a)
dijkstra(B, distance_b)
dijkstra(C, distance_c)

min_v = INF
max_v = 0
res = 0
for i in range(1, N+1):
    min_v = min(distance_a[i], distance_b[i], distance_c[i])
    if max_v < min_v:
        max_v = min_v
        res = i

print(res)