import sys
sys.setrecursionlimit(10**6)
# divide and conquer
def dc(st_row, st_col, N):
  global cnt0, cnt1
  if N == 0:
    return
  color = graph[st_row][st_col]   
  for i in range(st_row, st_row + N):
    for j in range(st_col, st_col + N):
      if graph[i][j] != color:
        N //= 2
        dc(st_row, st_col, N)
        dc(st_row, st_col + N, N)
        dc(st_row + N, st_col, N)
        dc(st_row + N, st_col + N, N)
        return  
  if color:
    cnt1 += 1
  else:
    cnt0 += 1

N = int(input())
graph = []
# 하얀색, 파란색
cnt0, cnt1 = 0, 0
for _ in range(N):
  graph.append(list(map(int, input().split())))

dc(0, 0, N)
print(cnt0, cnt1, sep = "\n")