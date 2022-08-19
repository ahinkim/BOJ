import sys
from collections import deque
def threeColorBfs(x, y):
    flag = graph[x][y]
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i] 
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny] and graph[nx][ny] == flag:
                visited[nx][ny] = True
                q.append((nx, ny))

def twoColorBfs(x, y):
    flag1 = graph[x][y]
    if flag1 == 'R':
        flag2 = 'G'
    elif flag1 == 'G':
        flag2 = 'R'
    else:
        flag2 = flag1

    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i] 
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny] and (graph[nx][ny] == flag1 or graph[nx][ny] == flag2):
                visited[nx][ny] = True
                q.append((nx, ny))

input = lambda : sys.stdin.readline().rstrip()
N = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = []
visited = [[False] * N for _ in range(N)]

for _ in range(N):
    graph.append(list(input()))

# 적록색약이 아닌 사람이 봤을 때의 구역 개수 구하기
area1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            threeColorBfs(i, j)
            area1 += 1

# 적록색약인 사람이 봤을 때의 구역 개수 구하기
visited = [[False] * N for _ in range(N)]
area2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            twoColorBfs(i, j)
            area2 += 1

print(area1, area2)