from collections import deque
def bfs(graph, x, y):
    # 1: 벽을 1개 부셨다. 0: 부시지 x 
    q = deque([(0, 1, x, y)])
    visited[0][x][y] = True
    while q:
        f, d, x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[f][nx][ny]:
                # 벽 부수고 이동
                if f == 0 and graph[nx][ny] == 1:
                    q.append((1, d + 1, nx, ny))
                    visited[f][nx][ny] = True
                # 벽 안부수고 이동
                elif graph[nx][ny] == 0:
                    q.append((f, d + 1, nx, ny))
                    visited[f][nx][ny] = True

n, m = map(int, input().split())
# input().split()하면 안된다. 문제 잘 보고 풀자.
graph = [list(map(int, input())) for _ in range(n)]
# 3차원 배열: 벽을 부시지 않은 경우 0, 벽은 부순 경우 1
visited = [[[False] * m for _ in range(n)] for _ in range(2)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
res = bfs(graph, 0, 0)
if res == None:
    print(-1)
elif res == 0:
    print(0)
else:
    print(res)