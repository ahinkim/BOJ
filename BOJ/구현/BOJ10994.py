import sys
def draw(N, idx):
    if N == 1:
        starMap[N-1][N-1] = '*'
        return
    for i in range(idx, N):
        starMap[idx][i] = '*'
        starMap[N-1][i] = '*'
    for i in range(idx, N):
        starMap[i][idx] = '*'
        starMap[i][N-1] = '*'

    draw(N-2, idx+2)

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
# size
N = 4*N-3
starMap = [[' ']*N for _ in range(N)]
draw(N, 0)
for x in starMap:
    print(*x, sep='')