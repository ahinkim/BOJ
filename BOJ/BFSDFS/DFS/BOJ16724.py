# 지도 밖으로 나가는 방향의 입력은 주어지지 않는다 == 싸이클
import sys
def dfs(x, y, visited):
    global cycle 
    if finished[x][y] == 1:
        return
    if visited[x][y] == 1:
        cycle = True
        return
    visited[x][y] = 1
    dx, dy = direction[graph[x][y]]
    dfs(x + dx, y + dy, visited)
    finished[x][y] = 1

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [[] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
finished = [[0] * m for _ in range(n)]
direction = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

for i in range(n):
    data = input()
    for j in range(m):
        graph[i].append(data[j])

res = 0
for i in range(n):
    for j in range(m):
        cycle = False
        if visited[i][j] == 0:
            dfs(i, j, visited)
            if cycle:
                res += 1  
print(res)