import sys
from collections import deque
def bfs():
    global q
    d = 0 
    while q:
        # 토마토 위치 x, y 날짜 d
        x, y, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵을 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 원래 익었던 토마토거나 방문한적이 있는 경우 or 비어있는 상자인 경우
            if graph[nx][ny] == 1 or graph[nx][ny] == -1:
                continue
            graph[nx][ny] = 1
            q.append((nx, ny, d + 1))
    return d

input = lambda : sys.stdin.readline().rstrip()
M, N = map(int, input().split())
graph = []
q = deque()
for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(M):
        if data[j] == 1:
            q.append((i, j, 0))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
res = bfs()
for i in range(N):
    for j in range(M):
        # 익지 않은 토마토가 있을 때
        if graph[i][j] == 0:
            res = -1
            break
print(res)