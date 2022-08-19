import sys
def dfs(x, y, dx, dy, depth):
    global now
    if x < 0 or y < 0 or x >= n or y >= n:
        return depth
    if graph[x][y] != now:
        return depth
    nx = x + dx
    ny = y + dy
    return dfs(nx, ny, dx, dy, depth + 1)

input = lambda : sys.stdin.readline()
n = 19
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 오른쪽 상단 대각선, 오른쪽, 오른쪽 하단 대각선, 아래 (왼쪽에서 시작하는 방향)
dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

check = False
for x in range(n):
    for y in range(n):
        if graph[x][y] != 0:
            now = graph[x][y]
            for i in range(4):
                # 이 전 방향이 현재랑 같은 색깔의 바둑돌이면 이미 확인했으니 또 확인할 필요 없다.
                if 0 <= x - dx[i] < n and 0 <= y - dy[i] <= n:
                    if graph[x - dx[i]][y - dy[i]] == now:
                        continue
                if dfs(x, y, dx[i], dy[i], 0) == 5:
                    print(now)
                    print(x + 1, y + 1)
                    check = True
if not check:
    print(0)