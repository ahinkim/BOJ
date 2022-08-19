R, C = map(int, input().split())
graph = []
res = [[False] * C for _ in range(R)]
for _ in range(R):
    graph.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# X가 존재하는 지도 맨 끝 위치(왼쪽, 오른쪽, 위, 아래)
left = C-1
right = 0
up = R-1
down = 0
for x in range(R):
    for y in range(C):
        cnt = 0
        if graph[x][y] == 'X':
            for i in range(4):
                nx, ny = x+dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= R or ny >= C or graph[nx][ny] == '.':
                    cnt += 1
            if cnt < 3:
                res[x][y] = True
                left = min(left, y)
                right = max(right, y)
                up = min(up, x)
                down = max(down, x)

for i in range(up, down+1):
    for j in range(left, right+1):
        if res[i][j]:
            print('X', end='')
        else:
            print('.', end='')
    print()