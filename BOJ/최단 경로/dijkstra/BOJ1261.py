import sys
import heapq
# 부숴야 하는 최소 벽의 개수 구하기
def crush_wall():
    q = []
    # 부순 벽의 개수 w, 위치 x, y
    heapq.heappush(q, (0, 0, 0))
    while q:
        w, x, y = heapq.heappop(q)
        if x == N-1 and y == M-1:
            return w
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 미로 밖으로 이동한 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 방문한 적이 없는 경우
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == '1':
                    heapq.heappush(q, (w+1, nx, ny))
                else:
                    heapq.heappush(q, (w, nx, ny))
    return 0

input = lambda : sys.stdin.readline().rstrip()
M, N = map(int, input().split())
graph = [list(input()) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(crush_wall())