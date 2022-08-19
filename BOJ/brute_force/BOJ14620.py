from itertools import combinations

def solutions(candidate):
  result = 0
  collisions = [[0] * N for _ in range(N)]
  for x, y in candidate:
    check = True
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      # 꽃잎이 화단을 벗어날 때
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        return False, -1
      # 꽃잎이 닿을 때
      if collisions[nx][ny] == 1:
        return False, -1
      # 꽃잎 채워주기
      collisions[nx][ny] = 1
      result += graph[nx][ny]
    result += graph[x][y]
    collisions[x][y] = 1
  return True, result

# 화단의 한 변의 길이
N = int(input())
graph = []
for _ in range(N):
  __input = list(map(int, input().split()))
  graph.append(__input)

candidates = []
for i in range(N):
  for j in range(N):
    candidates.append((i, j))

candidates = list(combinations(candidates, 3))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = int(1e9)
for candidate in candidates:  
  check, total = solutions(candidate)
  if check:
    result = min(result, total)
print(result)