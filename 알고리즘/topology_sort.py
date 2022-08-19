from collections import deque
def topology_sort():
    result = []
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in adj[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

N = 10
adj = [[] for i in range(N+1)]
indegree = [0]*(N+1)