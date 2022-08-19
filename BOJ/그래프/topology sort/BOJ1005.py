import sys
from collections import deque
def topology(degree):
  q = deque([])
  result = [0] * (N + 1)
  for i in range(1, N + 1):
    if degree[i] == 0:
      q.append(i)
      result[i] = time[i]
    
  while q:
    now = q.popleft()
    for i in graph[now]:
      degree[i] -= 1
      # 아래 3줄을 if degree[i] == 0 안에 넣어서 틀렸었다. 하나의 선수과목이 끝났을 때 시간 비교를 해야지 진입차수가 0일 때 시간비교를 하면 들어오는 모든 과목의 시간을 비교할 수 없다.
      t = result[now] + time[i]
      if t > result[i]:
        result[i] = t
      if degree[i] == 0:
        q.append(i)
  return result

input = sys.stdin.readline
T = int(input())
# 각 건물당 건설에 걸리는 시간

for _ in range(T):
  # 건물의 개수 N, 건물간의 건설순서 규칙의 총 개수 K
  N, K = map(int, input().split())
  graph = [[] for _ in range(N + 1)]
  degree = [0] * (N + 1)
  time = [0]
  time.extend(list(map(int, input().split())))
  for _ in range(K):
    # 건설순서 X Y
    X, Y = map(int, input().split())
    graph[X].append(Y)
    degree[Y] += 1
  # 건설해야 할 건물의 번호 W
  W = int(input())
  result = topology(degree)
  print(result[W])
