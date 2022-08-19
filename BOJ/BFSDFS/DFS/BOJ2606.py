import sys
def dfs(graph, visited, start):
  visited[start] = True
  for i in graph[start]:
    if visited[i] == True:
      continue
    dfs(graph, visited, i) 
  
input = sys.stdin.readline
# 컴퓨터의 수
N = int(input().rstrip())
# 컴퓨터 쌍의 수
M = int(input().rstrip())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
  # 컴퓨터의 번호 쌍
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(graph, visited, 1)

result = 0
for i in range(2, N + 1):
  if visited[i] == True:
    result += 1
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
print(result)