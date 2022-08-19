import sys
# 폭탄 설치
def install_boom(t):
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '.':
                graph[i][j] = 'O'
                boomtime[i][j] = t+3
def boomdelete():
    t = 2
    for _ in range(t, N+1):
        if t % 2 == 0:
            install_boom(t)
        else:
            for x in range(R):
                for y in range(C):
                    if boomtime[x][y] != t:
                        continue
                    graph[x][y] = '.'

                    for i in range(4):
                        nx, ny = x+dx[i], y+dy[i]
                        if nx < 0 or ny < 0 or nx >= R or ny >= C:
                            continue

                        graph[nx][ny] = '.'

        t+=1
        

input = lambda : sys.stdin.readline().rstrip()
# R*C, N초가 지난 후 격자판 출력
R, C, N = map(int, input().split())
# 격자판
graph = []
# 폭탄이 터지는 시간
boomtime = [[0]*C for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(R):
    data = list(input())
    graph.append(data)
    for j in range(C):
        if data[j] == 'O':
            boomtime[i][j] = 3

boomdelete()
for x in graph:
    print(*x, sep='')