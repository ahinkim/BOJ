n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
# 아래, 오, 위, 왼
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y = -1, 0
num = n ** 2
i = 0
result_x = 0
result_y = 0
while True:
  nx = x + dx[i % 4]
  ny = y + dy[i % 4]
  if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
    x, y = nx, ny
    graph[x][y] = num
    if num == k:
      result_x = x + 1
      result_y = y + 1
    if num == 1:
      break
    num -= 1
  else:
    nx, ny = x, y
    i += 1

for x in graph:
  print(*x, sep = " ")
print(result_x, result_y)
