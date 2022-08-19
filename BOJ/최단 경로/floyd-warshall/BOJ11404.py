n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
# 버스 정보
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]\

# 시작 도시와 도착 도시가 같은 경우는 없다.
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j:
      graph[i][j] = 0

for _ in range(m):
  # 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c
  a, b, c = map(int, input().split()) 
  # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다. (최솟값 저장) 
  if graph[a][b] > c:
    graph[a][b] = c

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
  for j in range(1, n + 1):
    # 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
    if graph[i][j] == INF:
      print(0, end = " ")
    else:
      print(graph[i][j], end = " ")
  print()

