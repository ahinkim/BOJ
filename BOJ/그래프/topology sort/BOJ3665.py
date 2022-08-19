from collections import deque
def __init__(graph, degree, n):
  # 등수 별 작년 팀 번호
  team_order = list(map(int, input().split())) 
  for i in range(n):
    graph[team_order[i]].extend(team_order[i + 1:]) 
    for team in team_order[i + 1:]:
      degree[team] += 1

def change_order(graph, degree, a, b):
  if b in graph[a]:
    graph[a].remove(b)
    degree[b] -= 1
    graph[b].append(a)
    degree[a] += 1
  else:
    graph[b].remove(a)
    degree[a] -= 1
    graph[a].append(b)
    degree[b] += 1

def topology(degree, n):
  q = deque([])
  for i in range(1, n + 1):
    if degree[i] == 0:
      q.append(i)
  cnt = 0
  teamorder = ""
  result = ""
  while q:
    cnt += 1
    # 진입차수 0이 두개여서 순위를 알 수 없는 경우 
    if len(q) > 1:
      result = "?"
      break
    now = q.popleft()
    teamorder += str(now) + " "
    for x in graph[now]:
      degree[x] -= 1
      if degree[x] == 0:
        q.append(x)
  # q에서 꺼낸 원소수가 n개보다 적은 경우 == 싸이클(데이터에 일관성이 없는 경우)
  if result == "" and cnt < n:
    result = "IMPOSSIBLE"
  elif cnt == n:
    result = teamorder
  return result

testcnt = int(input())
for _ in range(testcnt):
  # 팀의 수
  n = int(input()) 
  graph = [[] for _ in range(n + 1)]
  degree = [0] * (n + 1)
  __init__(graph, degree, n)
  # 등수가 바뀐 쌍의 수     
  m = int(input())
  for _ in range(m):
    a, b = map(int, input().split())
    # 등수변경에 따른 그래프 연결 변경
    change_order(graph, degree, a, b)
  result = topology(degree, n)
  print(result)