# input = sys.stdin.readline 안하면 python3에서 시간초과 난다. 입력값이 많을 때 꼭 해주자.
import sys
from collections import deque
def topology_sort(degree):
  q = deque([])
  result = [0] * (N + 1)
  for i in range(1, N + 1):
    if degree[i] == 0:
      q.append((1, i))
  while q:
    rank, now = q.popleft()
    result[now] = rank
    for i in graph[now]:
      degree[i] -= 1
      if degree[i] == 0:
        q.append((rank + 1, i))
  return result

input = sys.stdin.readline
# 과목의 수 N, 선수 조건의 수 M
N, M = map(int, input().split())

# 진입 차수
degree = [0] * (N + 1)
# 인접 리스트
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  degree[B] += 1

print(*topology_sort(degree)[1:])
  