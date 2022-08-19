import sys
from collections import deque
def bfs(x, y):
    # 위치, 체력, 우산내구도, 거리
    q = deque([(x, y, H, 0, 0)])
    visited[x][y] = H
    while q:
        x, y, h, d, c = q.popleft()
        # 안전지대일 때
        if graph[x][y] == 'E':
            return c
        if h == 0:
            continue
        # 4개의 방향으로 이동
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            # 맵을 벗어날 때
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            nh, nd = h, d
            if graph[nx][ny] == 'U':
                nd = D 
            # 내구도가 있다면
            if nd > 0:
                nd -= 1
            else:
                nh -= 1
            # 이전에 방문했던 체력과 내구도의 총합보다 현재 총합이 더 높다면
            if nh + nd > visited[nx][ny]: 
                q.append((nx, ny, nh, nd, c + 1))
                visited[nx][ny] = nh + nd
    return -1

input = lambda : sys.stdin.readline().rstrip()
# 정사각형 격자의 한변의 길이인 n, 현재 체력 h, 우산의 내구도 d
N, H, D = map(int, input().split())
graph = []
visited = [[-1] * N for _ in range(N)]

start_x = 0
start_y = 0
end_x = 0
end_y = 0
for i in range(N):
    data = list(input())
    graph.append(data)
    for j in range(N):
        if data[j] == 'S':
            start_x = i
            start_y = j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(start_x, start_y))