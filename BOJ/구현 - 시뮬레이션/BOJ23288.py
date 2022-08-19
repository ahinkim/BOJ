import sys
from collections import deque

# 주사위 이동
def move(dice, direction):
    # 1 = 주사위의 앞면, 6 = 주사위의 뒷면
    # 동쪽 이동
    if direction == 0:
        dice[4], dice[1], dice[3], dice[6] = dice[6], dice[4], dice[1], dice[3]
    # 남쪽 이동
    elif direction == 1:
        dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]
    # 서쪽 이동
    elif direction == 2:
        dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
    # 북쪽 이동
    else:
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
# 동서남북으로 이동할 수 있는 칸 중 B와 같은 정수인 칸들의 개수 세는 함수
def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False] * m for _ in range(n)]
    B = graph[x][y]
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == B:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return cnt

def solution(x, y, d):
    # 이동 횟수
    cnt = 0
    res = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        # 칸이 있다면 주사위의 아랫면에 있는 정수와 칸에 있는 정수를 비교
        if 0 <= nx < n and 0 <= ny < m:
            move(dice, d)
            # 90도 시계방향으로 회전
            if dice[6] > graph[nx][ny]:
                d = (d + 1) % 4
            elif dice[6] < graph[nx][ny]:
                d = (d - 1) % 4
            x, y = nx, ny 
            # 이동했을 때 점수 구하기
            res += graph[x][y] * bfs(x, y)
            cnt += 1
        # 이동방향에 칸이 없을 때 반대방향으로 주사위 이동
        else:
            d = (d - 2) % 4    
        if cnt == k:
            break 
    return res
input = lambda : sys.stdin.readline().rstrip()
# 세로 크기 n, 가로 크기 m, 이동하는 횟수 k
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [0, 1, 2, 3, 4, 5, 6]
# 처음 주사위 이동 방향 동쪽
print(solution(0, 0, 0))