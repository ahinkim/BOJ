import sys
def search_mines(x, y):
    res = 0
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if ans[nx][ny] =='*':
            res += 1
    return res

input = lambda : sys.stdin.readline().rstrip()
n = int(input())
ans = [list(input()) for _ in range(n)]
graph = [list(input()) for _ in range(n)]
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

check = False
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'x':
            if ans[i][j] == '*':
                check = True
            else:
                ans[i][j] = search_mines(i, j)

for i in range(n):
    for j in range(n):
        if ans[i][j] == '*' and not check:
            print('.', end ='')
        else:
            print(ans[i][j], end = '')
    print()