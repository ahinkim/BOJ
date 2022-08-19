import sys
def dfs(x, y):
    global depth
    graph[x][y] = -1
    depth += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위 벗어날 경우
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)
input = lambda : sys.stdin.readline().rstrip()
# 지도의 크기
N = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 지도
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            depth = 0
            dfs(i, j)
            ans.append(depth)

ans.sort()
print(len(ans))
print(*ans, sep = '\n')