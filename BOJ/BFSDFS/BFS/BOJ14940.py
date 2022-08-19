import sys
from collections import deque
def bfs(x, y):
    dist[x][y] = 0
    q = deque([(x, y, 0)])
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = d + 1
                q.append((nx, ny, d + 1))

input = lambda : sys.stdin.readline().rstrip()
# 세로, 가로 크기
n, m = map(int, input().split())
graph = [] 
# 도달할 수 없다면 -1 출력
dist = [[-1]*m for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        # 목표지점
        if data[j] == 2:
            st_x, st_y = i, j
        # 갈 수 없는 땅
        if data[j] == 0:
            dist[i][j] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
bfs(st_x, st_y)
for x in dist:
    print(*x, sep=' ')