import sys
from collections import deque
def bfs(graph, x, y):
    q = deque([(x, y)])
    graph[x][y] = -1 # 처음에 방문처리를 10으로 했다가 벽의 값이 10이 될 때랑 충돌했다. 방문처리를 숫자로 하려면 아예 쓰지 않는 -1 같은 숫자로 하자.
    wall = set()
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵을 벗어나거나 방문한 적이 있을 때
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == -1:
                continue
            # 벽을 마주쳤을 때
            if  graph[nx][ny] > 0:
                wall.add((nx, ny))
                continue
            graph[nx][ny] = -1
            q.append((nx, ny))
    for x, y in wall:
        graph[x][y] += cnt

input = lambda : sys.stdin.readline().rstrip()
n, m = map(int, input().split())
# 문자열로 들어오는 거 input().split()으로 바꾸는 실수 하지 말자.
graph = [list(map(int, input())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(graph, i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] != -1:
            print(graph[i][j] % 10, end = '')
        else:
            print(0, end = '')
    print()