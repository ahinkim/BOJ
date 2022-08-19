from itertools import combinations
from collections import deque
import copy # 리스트 copy하는 방법 잘 알아두자
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)] #상 좌 하 우
# 벽의 개수 3개
# 0은 빈 칸, 1은 벽, 2는 바이러스
n, m = map(int, input().split())
selection = []
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(m):
    selection.append((i, j))

selection = list(combinations(selection, 3))
INF = int(1e9)

def bfs(graph, start):
  q = deque([start])
  infection = 0
  while q:
    x, y = q.popleft()
    for direction in directions:
      nx = x + direction[0]
      ny = y + direction[1]
      # 그래프를 벗어나거나 1(벽), 2(감염병) 만나면 continue
      if nx < 0 or nx >= n or ny < 0 or ny >= m: # n행 m열인데 둘다 n으로 써서 n =4 m = 6일 때 에러났다. 조심하자
        continue
      if graph[nx][ny] == 1 or graph[nx][ny] == 2:
        continue
      # 0이라면
      graph[nx][ny] = 2
      q.append((nx, ny))
      infection += 1
  return infection

# 감염이 적게되는 벽 위치  
min_infection = INF
copygraph = []  
infect_loc = []
for i in range(n):
  for j in range(m):
    # 바이러스 위치 저장
    if graph[i][j] == 2:
      infect_loc.append((i, j))

for w1, w2, w3 in selection:
  copygraph = copy.deepcopy(graph)
  # 벽 위치 3개 중 그 위치에있는 값이 하나라도 0이 아닐 때
  if graph[w1[0]][w1[1]] != 0 or graph[w2[0]][w2[1]] != 0 or graph[w3[0]][w3[1]] != 0:
    continue
  # 벽만들기: 이 부분을 잊었다. 코딩할 때 생각하면서 짜자
  copygraph[w1[0]][w1[1]] = 1
  copygraph[w2[0]][w2[1]] = 1
  copygraph[w3[0]][w3[1]] = 1
  # 3개 다 0일 때
  infection = 0
  for location in infect_loc:
    infection += bfs(copygraph, location)
  # 만약 감염을 더 적게 시켰다면

  if infection < min_infection:
    min_infection = infection
    minw1 = w1
    minw2 = w2
    minw3 = w3     
  
  #그래프 처음으로 초기화 3개 위치  = 0

# 감염이 제일 적게되는 위치 3개에 벽 저장
graph[minw1[0]][minw1[1]] = 1
graph[minw2[0]][minw2[1]] = 1
graph[minw3[0]][minw3[1]] = 1

copygraph = []
copygraph = copy.deepcopy(graph) # 리스트 copy하는 방법 잘 알아두자
for i in range(n):
  for j in range(m):
    # 2라면 BFS 수행
    if graph[i][j] == 2:
      bfs(copygraph, (i, j))

result = 0
for i in range(n):
  for j in range(m):
    if copygraph[i][j] == 0:
      result += 1
print(result)

