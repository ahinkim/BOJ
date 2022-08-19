import sys
from collections import deque
def topology():
    q = deque()
    res = []
    cnt = 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        cnt += 1
        res.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    if cnt == n:
        for x in res:
            print(x)
    else:
        print(0)

input = lambda : sys.stdin.readline().rstrip()
# 가수의 수 n, 보조 pd의 수 m
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    order = list(map(int, input().split()))
    for i in range(1, order[0]):
        a, b = order[i], order[i + 1]
        graph[a].append(b)
        indegree[b] += 1

topology()