import sys
from collections import deque
# 덩어리 방문 처리
def bfs(count, visited, x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵을 벗어났을 때
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 바다일 때
            if graph[nx][ny] == 0 and not visited[nx][ny]:  
                count[x][y] += 1
                continue
            # 방문한 적이 없다면
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

input = lambda : sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            # 녹여야할 빙산 찾기
            if not visited[i][j] and graph[i][j] > 0:
                bfs(count, visited, i, j)
                cnt += 1
    # 빙산 녹이기
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    # 덩어리가 두 개 이상일 때
    if cnt >= 2:
        print(time)
        break
    # 덩어리가 없을 때 (덩어리가 2개 이상으로 분류되지 않았을 때)
    if cnt == 0:
        print(0)
        break
    time += 1