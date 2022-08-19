from collections import deque
def bfs(start):
  # 시작 위치와 시작 시간 저장
  q = deque([(start, 0)])
  # 수빈이가 동생을 찾는 방법의 수
  cnt = 0
  # 수빈이가 동생을 찾는 가장 빠른 시간
  min_time = -1
  while q:
    # 위치, 시간
    loc, t = q.popleft()
    # 가장 빠른 시간을 찾았고 그 시간을 지났다면 break
    if min_time != -1 and min_time != t:
      break
    if loc == K:
      min_time = t
      cnt += 1 

    for x in [loc - 1, loc + 1, loc * 2]:
      # visited에 저장된 시간보다 큰 시간은 항상 종점에 늦게 도착하기 때문에 방문하지 않는다.
      if 0 <= x <= MAX and visited[x] > t:
        q.append((x, t + 1))
        visited[x] = t + 1

  return min_time, cnt

# 시작점 N, 종점 K
N, K = map(int, input().split())
# 방문했던 최소 시간 저장하는 테이블
visited = [int(1e9)] * 100001
MAX = 100000
print(*bfs(N), sep = "\n")