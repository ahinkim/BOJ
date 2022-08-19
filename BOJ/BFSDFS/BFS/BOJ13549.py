# 누가 제일 적은 비용으로 도착하냐(최단거리 알고리즘)
# 이 문제는 어떤 거리비용이 들든 누가 먼저 도착지점에 도착하냐(BFS)
from collections import deque
from re import T
def bfs(visited):
    # 수빈이가 있는 위치, 시작 시간
    q = deque([(N, 0)])
    min_value = int(1e9)
    while q:
        x, t = q.popleft()
        if x == K:
            min_value = t
            break
        array = [2 * x, x - 1, x + 1]
        for i in range(3):
            next = array[i]
            if 0 <= next <= max_v and not visited[next]:
                if i == 0:
                    q.appendleft((next, t))
                else:
                    q.append((next, t + 1))
                visited[next] = True
    return min_value
# 수빈이가 있는 위치 N과 동생이 있는 위치 K
N, K = map(int, input().split())
max_v = 100000 
visited = [False] * (max_v + 1)
print(bfs(visited))