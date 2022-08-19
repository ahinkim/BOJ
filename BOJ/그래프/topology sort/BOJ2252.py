from collections import deque
# 위상 정렬
def topology_sort(degree):
  q = deque()
  for i in range(1, N + 1):
    if degree[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    print(now, end = " ")
    for i in graph[now]:
      degree[i] -= 1 
      if degree[i] == 0:
        q.append(i)

# N 학생 수, M 키를 비교한 횟수
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  degree[B] += 1

topology_sort(degree)