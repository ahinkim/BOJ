from collections import deque
def bfs(x, y):
    q =deque([(x, y, 1, str(graph[x][y]))])
    res = []
    while q:
        x, y, d, nums = q.popleft()
        if d >= 7:
            res.append(nums)
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= 4 or ny >=4:
                continue
            q.append((nx, ny, d+1, nums + str(graph[nx][ny])))
    return res

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
T = int(input())
for k in range(T):
    graph = []
    res = []
    for _ in range(4):
        graph.append(list(map(int, input().split())))
    for i in range(4):
        for j in range(4):
            res.extend(bfs(i, j))

    cnt = len(set(res))
    print(f'#{k+1} {cnt}')