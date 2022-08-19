import sys
import heapq
def dijkstra(start):
    q = []
    # 거리(골목), 노드(교차로), 최대 요금
    heapq.heappush(q, (0, start, 0))
    max_v[start] = 0
    distance[start] = 0
    res = INF
    while q:
        dist, now, now_mv = heapq.heappop(q)
        # 도착교차로에 도착한 최대 요금의 최솟값 찾기
        if now == b:
            res = min(res, now_mv)
        for i in graph[now]:
            cost = dist + i[1]
            nex_mv = now_mv 
            # 최대 요금 갱신
            if i[1] > now_mv:
                nex_mv = i[1]
            # 최대 요금이 더 작다면 해당 노드 갱신
            if (nex_mv < max_v[i[0]] and cost <= c):
                max_v[i[0]] = nex_mv
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0], nex_mv))
            # 거리가 더 짧다면 해당 노드 갱신
            elif cost < distance[i[0]] and cost <= c:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0], nex_mv))
    return res
            
input = lambda : sys.stdin.readline().rstrip()
# 교차로 개수 N, 골목 개수 M, 시작 교차로 번호 A, 도착 교차로 번호 B, 가진 돈 C 
n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
max_v = [INF] * (n + 1) # [[INF] * (n + 1)]하면 안된다.
distance = [INF] * (n + 1) 
for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))
    graph[v2].append((v1, cost))
res = dijkstra(a)
if res == INF:
    print(-1)
else:
    print(res)