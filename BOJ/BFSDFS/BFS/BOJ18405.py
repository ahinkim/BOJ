# 아는 문제라고 급하게 접근하지 말고 보통 bfs에서 변형이 돼서 출제를 많이 하니까 신중하게 알고리즘을 생각하고 풀자
from collections import deque
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
s, x, y = map(int, input().split())
# 인덱스에 맞게 위치 변경
x -= 1
y -= 1
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs_all(start, sec):
  q = deque([])
  cnt = len(start)
  for x in start:
    q.append(x[1])
  while q:
    if sec == 0:
      break
    x, y = q.popleft()
    for direction in directions:
      nx = x + direction[0]
      ny = y + direction[1]
      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      if graph[nx][ny] != 0:
        continue
      graph[nx][ny] = graph[x][y]
      q.append((nx, ny))
    cnt -= 1
    if cnt == 0:
      sec -= 1
      cnt = len(q)

# 바이러스 초기 위치들을 기록
start = []
for i in range(N):
  for j in range(N):
    if 1 <= graph[i][j] <= K:
      start.append((graph[i][j], (i, j)))
start.sort()
bfs_all(start, s)

print(graph[x][y])
