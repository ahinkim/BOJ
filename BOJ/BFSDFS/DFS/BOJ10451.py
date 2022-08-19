import sys
# 파이썬에서 이거 꼭 쓰는 것 잊지 말기
sys.setrecursionlimit(10**6)
def dfs(graph, x, visited):
  global cycle
  # 이미 방문한 적 있었으면 넘어가기
  if visited[x] == True:
    return 
  visited[x] = True
  
  for i in graph[x]:
    if not visited[i]:
      dfs(graph, i, visited)
    else:
      cycle += 1
      
# 테스트 케이스의 크기
T = int(input())

for _ in range(T):
  # 순열의 크기
  N = int(input())
  data1 = list(map(int, input().split()))
  data2 = sorted(data1)#data1.sort()했다가 틀렸다. 반환해주질 않으니 이렇게 하면 안된다.

  graph = [[] for _ in range(N + 1)]
  for i in range(N):
    graph[data1[i]].append(data2[i])
  visited = [False] * (N + 1)
  cycle = 0

  for i in range(1, N + 1):
    dfs(graph, i, visited)  
  print(cycle)