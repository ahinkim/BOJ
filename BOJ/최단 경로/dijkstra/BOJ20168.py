import sys
import heapq
def dijkstra(distance, amount):
    q = []
    heapq.heappush(q, (A, 0))
    distance[A] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            if i[1] > amount:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
    return distance[B]

def binary(start, end):
    res = -1
    while start <= end:
        distance = [INF]*(N+1)
        mid = (start+end) // 2
        target = dijkstra(distance, mid)
        if target > C:
            start = mid + 1
        else:
            res = mid
            end = mid - 1
    return res

input = lambda : sys.stdin.readline().rstrip()
# 교차로 개수 N, 골목 개수 M, 시작 교차로 번호 A, 도착 교차로 번호 B, 가진 돈 C 
N, M, A, B, C = map(int, input().split())
adj = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(M):
    n1, n2, cost = map(int, input().split())
    adj[n1].append((n2, cost))
    adj[n2].append((n1, cost))
    
print(binary(1, 1000))