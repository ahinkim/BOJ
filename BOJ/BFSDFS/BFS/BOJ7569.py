import sys
from collections import deque
def bfs(x, y, h):
    d = -1
    while q:
        # 높이, 행, 열, 날짜
        h, x, y, d = q.popleft()
        # 상하좌우
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            # 범위를 벗어날 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 익지 않은 토마토일 떄
            if graph[h][nx][ny] == 0:
                # 토마토 익히기
                graph[h][nx][ny] = 1
                q.append((h, nx, ny, d + 1))
        # 앞뒤
        for i in range(2):
            nh = h + dh[i]
            if nh < 0 or nh >= H:
                continue
            if graph[nh][x][y] == 0:
                graph[nh][x][y] = 1
                q.append((nh, x, y, d + 1))
    return d

input = lambda : sys.stdin.readline().rstrip()
# 가로칸 M, 세로칸 N, 쌓아올려지는 상자의 수 H
M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]
q = deque()
for i in range(H):
    for j in range(N):
        _input = list(map(int, input().split()))
        for k in range(M):
            # 토마토가 익었을 때 
            if _input[k] == 1:
                q.append((i, j, k, 0))
        graph[i].append(_input)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dh = [1, -1]

ans = bfs(0, 0, 0)
check = True

# 토마토가 모두 익었는 지 확인
for i in range(H):
    for j in range(N):
        for k in range(M):
            # 익지 않은 토마토가 있을 떄
            if graph[i][j][k] == 0:
                ans = -1
                break
print(ans)