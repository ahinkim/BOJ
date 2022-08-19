import sys
from collections import deque
def bfs(x, y):
    d = 0
    q = deque([(0, x, y)])
    visited[x][y] = True
    while q:
        d, x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                continue
            if graph[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((d+1, nx, ny))
    return d

input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = 0
for i in range(N):
    for j in range(M):
        visited = [[False]*M for _ in range(N)]
        if graph[i][j] == 'L':
            d = bfs(i, j)
            res = max(res, d)

print(res)