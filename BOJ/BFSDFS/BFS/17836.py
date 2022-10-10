import sys
from collections import deque
def bfs():
    q = deque([(0, 0, 0, 0)])
    visited[0][0] = True
    while q:
        d, x, y, gram = q.popleft()
        if x == N-1 and y == M-1:
            if d <= T:
                return d
            else:
                return 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # gram을 갖고 있지 않은 경우
            if not gram and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((d+1, nx, ny, 0))
            # gram을 갖고 있는 경우
            elif graph[nx][ny] == 2 or (gram and not visited_wg[nx][ny]):            
                visited_wg[nx][ny] = True
                q.append((d+1, nx, ny, 1))

    return 0
input = lambda : sys.stdin.readline().rstrip()
# 성의 크기 N, M, 제한 시간 T
N, M, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
# visited_with_gram
visited_wg = [[False]*M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = bfs()
if res == 0:
    print("Fail")
else:
    print(res)