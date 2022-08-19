import sys
from collections import deque
def side_check(x, y):
    visited[x][y] = True
    q = deque([(x, y)])
    # 위치 저장
    locations = []
    locations.append((x, y))
    out_side = False
    while q:
        x, y = q.popleft()
        for i in range(6):
            if x % 2 == 0:
                nx, ny = x + dx[i], y + dy[i]
            else:
                nx, ny = x + dx2[i], y + dy2[i]
            # 범위를 벗어난 경우: 외부
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                out_side = True
                continue
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                locations.append((nx, ny))
    # 내부 -1로 값 할당
    if not out_side:
        for x, y in locations:
            graph[x][y] = -1

def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])
    # 벽면의 길이의 합
    total = 0
    while q:
        x, y = q.popleft()
        for i in range(6):
            if x % 2 == 0:
                nx, ny = x + dx[i], y + dy[i]
            else:
                nx, ny = x + dx2[i], y + dy2[i]
            # 범위를 벗어날 경우(벽면) or 건물이 아닌 경우(벽면)
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 0:
                total += 1
            # 건물인 경우
            elif graph[nx][ny] == 1 and not visited[nx][ny]: 
                visited[nx][ny] = True
                q.append((nx, ny))

    return total

input = lambda : sys.stdin.readline().rstrip()
m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
# 짝수 행일 때 좌표 (0, 2, 4, ...)
dx = [-1, 0, 1, 1, 0, -1]
dy = [0, -1, 0, 1, 1, 1] 
# 홀수 행일 때 좌표 (1, 3, 5, ...)
dx2 = [-1, 0, 1, 1, 0, -1]
dy2 = [-1, -1, -1, 0, 1, 0]
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0 and not visited[x][y]:
            # 외부인지 내부인지 검사 내부면 값 -1 할당해서 구분
            side_check(x, y)

visited = [[False] * m for _ in range(n)]

res = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1 and not visited[x][y]:
            # 벽면의 길이의 합 구하기
            res += bfs(x, y)

print(res)