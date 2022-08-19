n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
result = 0

# 그래프를 맨 아래 -1 부터 돌면서 자식들 중 더 큰 값을 자기자신에 저장
for i in range(n - 2, -1, -1): # n - 2, 0, -1 이라고 하면 안된다. 이거는 n - 2부터 0 + 1 까지라는 뜻이기 때문
  for j in range(len(graph[i])):
    graph[i][j] += max(graph[i + 1][j], graph[i + 1][j + 1])

print(graph[0][0])