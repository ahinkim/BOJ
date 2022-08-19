import sys
input = sys.stdin.readline
# 지역의 개수 n, 수색범위 m, 길의 개수 r
n, m, r = map(int, input().rstrip().split())
items = [0]
items.extend(list(map(int, input().rstrip().split())))

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
  a, b, l = map(int, input().rstrip().split())
  graph[a][b] = l
  graph[b][a] = l

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# k 나오고 a b 나와야 하는데 a, k, b해서 틀렸다. 순서만 바뀌어도 거리가 달라지니 조심하자.
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

total = 0
for a in range(1, n + 1):
  cnt = 0
  for b in range(1, n + 1):
    if graph[a][b] <= m:
      cnt += items[b]
  total = max(total, cnt)
print(total)