import sys
def dfs(v):
    global route
    global cycle
    if finished[v]:
        return
    if visited[v]:
        cycle = True
        route = route[route.index(v):]
        return

    visited[v] = True
    route.append(v)
    dfs(graph[v]) 

    finished[v] = True

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
graph = [0] * (N + 1)
visited = [False] * (N + 1)
finished = [False] * (N + 1)
for i in range(1, N + 1):
    graph[i] = int(input())

res = []
for i in range(1, N + 1):
    cycle = False
    route = []
    if not visited[i]:
        dfs(i)
        if cycle:
            res.extend(route)

res.sort()
print(len(res))
print(*res, sep = '\n')