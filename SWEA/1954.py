T = int(input())
for k in range(T):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    # 오, 아래, 왼, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 0, -1
    num = 1
    i = 0
    while True:
        nx = x + dx[i % 4]
        ny = y + dy[i % 4]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            x, y = nx, ny
            graph[x][y] = num
            if num == n**2:
                break
            num += 1
        else:
            nx, ny = x, y
            i += 1
    print(f'#{k+1}')
    for x in graph:
        print(*x, sep=' ')