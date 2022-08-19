import sys
from collections import deque
def bfs():
    res = -1
    # 현재 위치, 버튼의 수
    q = deque([(S, 0)])
    while q:
        y, cnt = q.popleft()
        if y == G:
            res = cnt
            break
        for i in range(2):
            ny = y + dy[i]
            if ny < 1 or ny > F:
                continue
            if not visited[ny]:
                visited[ny] = True
                q.append((ny, cnt + 1))
    return res

input = lambda : sys.stdin.readline().rstrip()
# 총 층수 F, 강호의 위치 S, 스타트 링크 G, 위로 가는 층수 U, 아래로 가는 층수 D
F, S, G, U, D = map(int, input().split())
visited = [False] * (F+1)
dy = [U, -D]

ans = bfs()
if ans == -1:
    print("use the stairs")
else:
    print(ans)