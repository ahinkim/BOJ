def solution(graph, routes, N):
  # 맨 밑부터 맨 위로 왼쪽방향부터 오른쪽방향으로 올라가며 현재 위치에서 종점으로 갈 수 있는 경로의 수를 저장
  for x in range(N - 1, -1, -1):
    for y in range(N - 1, -1, -1):
      if x == N - 1 and y == N - 1:
        routes[N - 1][N - 1] = 1
        continue
			# 현재 위치에서 점프할 수 있는 거리
      k = graph[x][y]
			# 이전에 계산된 dp값 활용
      if x + k < N:
        routes[x][y] += routes[x + k][y]
      if y + k < N:
        routes[x][y] += routes[x][y + k]


N = int(input())
graph = []
routes = [[0] * N for _ in range(N)]
for _ in range(N):
  graph.append(list(map(int, input().split())))

solution(graph, routes, N)
print(routes[0][0])