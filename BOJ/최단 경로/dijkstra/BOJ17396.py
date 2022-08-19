import sys
import heapq
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start)) 
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            # 적의 시야에 보이는 곳이면 갈 수 없다.
            if outlook[i[0]] == 1:
                continue
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

input = lambda : sys.stdin.readline().rstrip()
# 분기점의 수 N, 분기점들을 잇는 길의 수 M
N, M = map(int, input().split())
# 각 분기점이 적의 시야에 보이는지를 의미하는 N개의 정수
outlook = list(map(int, input().split()))
# N-1번째 분기점은 상대 시야에 보이면서 갈 수 있는 곳
outlook[N-1] = 0
# 인접 리스트
adj = [[] for _ in range(N)]
# a번째 분기점과 b번째 분기점 사이를 지나는데 t만큼의 시간이 걸리는 것
for _ in range(M):
    a, b, t = map(int, input().split())
    adj[a].append((b, t))
    adj[b].append((a, t))

INF = int(1e11)
distance = [INF] * N    
dijkstra(0)
# 넥서스까지 갈 수 없으면 -1을 출력
if distance[N-1] == INF:
    print(-1)
else:
    print(distance[N-1])