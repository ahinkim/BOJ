import sys
import heapq
def dijkstra(start):
    q = []
    # dist, now, 거쳐간 도시들
    heapq.heappush(q, (0, start, [start]))
    distance[start] = 0
    while q:
        dist, now, visited = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                nx_visited = visited[:] # nx_visited = visited 하면 새로운 리스트가 생성되는 것이 아닌 기존 리스트의 주소를 가리키는 것이기 때문에 이렇게 하면 정답이 제대로 안나온다.
                distance[i[0]] = cost
                nx_visited.append(i[0])
                heapq.heappush(q, (cost, i[0], nx_visited))
                # 최소 비용을 갖는 경로 갱신
                min_visited[i[0]] = nx_visited

input = lambda : sys.stdin.readline().rstrip()
# 도시의 개수 n
n = int(input())
# 버스의 개수 m
m = int(input())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)
# 최소 비용을 갖는 경로
min_visited = [[] for _ in range(n + 1)]
for _ in range(m):
    # 출발 도시, 도착 도시, 비용
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
# 출발 도시 도착 도시
start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
print(len(min_visited[end]))
print(*min_visited[end])