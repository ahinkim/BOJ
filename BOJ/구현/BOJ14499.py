import sys
# 시작위치, 명령리스트
def play(dice, x, y):
    # 항상 1이 앞면이고 6이 뒷면이다.
    for order in orders:
        order -= 1
        nx = x + dx[order]
        ny = y + dy[order]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        x, y = nx, ny
        # 동쪽
        if order == 0:
            dice[4], dice[1], dice[3], dice[6] = dice[6], dice[4], dice[1], dice[3]
        # 서쪽
        elif order == 1:
            dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4] 
        # 북쪽
        elif order == 2:
            dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
        # 남쪽
        else:
            dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5],
        # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
        if graph[x][y] == 0:
            graph[x][y] = dice[6]
        # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며 칸에 쓰여 있는 수는 0이 된다.
        else:
            dice[6] = graph[x][y]
            graph[x][y] = 0
        print(dice[1])

input = lambda : sys.stdin.readline().rstrip()
# 지도의 크기 NM, 주사위를 놓은 곳의 좌표 xy, 명령의 개수 K
N, M, x, y, K = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 이동하는 명령
orders = list(map(int, input().split()))
# 주사위 면
dice = [0] * 7
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dx = [0, 0, -1, 1] 
dy = [1, -1, 0, 0]

play(dice, x, y)
