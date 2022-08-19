from collections import deque
def bfs(graph, visited, x, y):
    if visited[x][y] == True:
        return False
    q = deque([(x, y)])
    visited[x][y] = True
    total = 0
    cnt = 0
    res = []
    while q:
        x, y = q.popleft()
        res.append((x, y))
        total += graph[x][y]
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == True:
                continue
            if not (L <= abs(graph[x][y] - graph[nx][ny]) <= R):
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
    v = total // cnt
    for x, y in res:
        graph[x][y] = v
    # 인구 이동이 일어났다면
    if cnt > 1:
        return True
    return False

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0
while True:
    visited = [[False] * N for _ in range(N)]
    check = False
    for i in range(N):
        for j in range(N):
            if bfs(graph, visited, i, j):
                check = True
                # ans += 1을 여기다가 구현해서 계속 값이 틀렸었다.
    if check == False:
        break
    ans += 1
print(ans)          