H, W = map(int, input().split())
blocks = list(map(int, input().split()))
graph = [[0] * W for _ in range(H)]
for i in range(W):
  for j in range(H - 1, H - 1 - blocks[i], -1):
    graph[j][i] = 1
total = 0
for i in range(H - 1, -1, -1):
  cnt = 0
  left = False
  right = False
  for j in range(W):
    if graph[i][j] == 1:
      if left == False:
        left = True
      else:
        total += cnt
        cnt = 0
    elif left == True:
      cnt += 1
    
print(total)