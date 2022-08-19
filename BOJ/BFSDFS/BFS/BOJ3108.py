import sys
from collections import deque
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵을 벗어나면
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 인접하지 않다면
            if graph[nx][ny] != 1:
                continue
            # 방문한적이 없다면
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))        

input = lambda : sys.stdin.readline().rstrip()
# 직사각형의 개수 n 
n = int(input())
N = 2001
graph = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
ans = 0
start = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 = (x1 + 500) * 2 
    y1 = (y1 + 500) * 2
    x2 = (x2 + 500) * 2
    y2 = (y2 + 500) * 2
    start.append((y1, x1)) 
    # 직사각형 그리기
    # 가로
    for i in range(x1, x2 + 1): 
        graph[y1][i] = 1 
        graph[y2][i] = 1
    # 세로
    for i in range(y1, y2 + 1): 
        graph[i][x1] = 1
        graph[i][x2] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for x, y in start:
    if not visited[x][y]:
        bfs(x, y)
        ans += 1
# 원점 포함되어 있다면 개수 빼기
if graph[1000][1000] == 1:
    ans -= 1
print(ans)