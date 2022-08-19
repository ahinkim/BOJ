# 벽의 위치 저장해서
# 상하좌우 대각선을 통해 움직인다.
# nx ny가 벽의 위치와 같으면 0
import sys
from collections import deque
def bfs(Map):
    x = n - 1
    y = 0
    q = deque([(x, y)])
    # 벽 이동횟수
    turn = 0
    while q:
        turn += 1
        # 벽이 다 내려갔을 때
        if turn == 9:
            return True
        for _ in range(len(q)):
            x, y = q.popleft()
            # 벽이 캐릭터 있는 칸으로 이동했을 때
            if Map[x][y] == '#':
                continue
            # 캐릭터가 종점에 도착했을 떄
            if x == 0:
                return True
            # 인접한 칸으로 이동
            for i in range(9): 
                nx = x + dx[i]
                ny = y + dy[i]
                # Map을 벗어났을 때
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                # 벽이라면
                if Map[nx][ny] == "#":
                    continue
                q.append((nx, ny))
        # 1초 동안 q에 있는 원소가 모두 이동할 수 있기 때문에 q에 있는 원소가 다 빠지고 벽이 이동해야 한다. 
        Map.pop()
				# append가 아닌 appendleft로 해야 한다.
        Map.appendleft(list('........'))

    return False

input = lambda : sys.stdin.readline().rstrip()
# 문제에 현재 위치에 서 있을 수 있다고 헀으니 0, 0 도 포함시켜야 한다.
dx = [0, 0, 0, 1, -1, 1, 1, -1, -1]
dy = [0, 1, -1, 0, 0, -1, 1, -1, 1]
n = 8
Map = deque()
for i in range(n):
    data = list(input())
    Map.append(data)

if bfs(Map):
    print(1)
else:
    print(0)