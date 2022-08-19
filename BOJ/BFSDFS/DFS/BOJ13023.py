def dfs(visited, v, depth):
    res = 0
    visited[v] = True
    if depth == 5:
        return 1
    for i in graph[v]:
        if not visited[i]:
            res += dfs(visited, i, depth + 1)
            visited[i] = False
    return res

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
ans = 0
check = True
visited = [False] * N
for i in range(N):
    ans = dfs(visited, i, 1)
    visited[i] = False
    if ans > 0:
        check = False
        print(1)
        break
if check:
    print(0)