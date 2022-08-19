import sys
def solutions(x, y, result):
  likes[result] = likes.get(result, 0) + 1 
  if len(result) == 5:
    return
  # 상하좌우나 대각선 방향의 칸으로 한 칸씩 이동
  for i in range(8):
    nx, ny = (x + dx[i]) % N, (y + dy[i]) % M
    solutions(nx, ny, result + graph[nx][ny])

input = sys.stdin.readline
# 격자의 크기 N, M, 신이 좋아하는 문자열의 개수 K
N, M, K = map(int, input().split())
graph = []
for i in range(N):
  graph.append(list(input())) 
  
likes = {}
dx = [1, -1, 0, 0, -1, -1, 1, 1] # 상 하 좌 우 대각선
dy = [0, 0, 1, -1, -1, 1, -1, 1]

for i in range(N):
  for j in range(M):
    solutions(i, j, graph[i][j])
    
# K개의 줄에 걸쳐서 신이 좋아하는 문자열
for _ in range(K):
  like = input().rstrip()
  print(likes.get(like, 0))