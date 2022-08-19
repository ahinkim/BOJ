from collections import deque
def solution(places):
    def bfs(k, x, y):
        res = 1
        q = deque([(x, y, 0)])
        visited[x][y] = True

        while q:
            x, y, d = q.popleft()
            if d >= 2:
                break
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                    continue
                if not visited[nx][ny]:
                    if places[k][nx][ny] == 'P':
                        res = 0
                        break
                    if places[k][nx][ny] == 'X':
                        continue
                    visited[nx][ny] = True
                    q.append((nx, ny, d+1))
        return res

    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for k in range(5):
        ans = 1
        for i in range(5):
            for j in range(5):
                visited = [[False] * 5 for _ in range(5)]
                if places[k][i][j] == 'P' and bfs(k, i, j) == 0:
                    ans = 0
        answer.append(ans)
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])