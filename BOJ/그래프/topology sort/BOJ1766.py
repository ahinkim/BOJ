import sys
import heapq
def topology(indegree):
    q = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    while q:
        now = heapq.heappop(q)
        print(now, end = " ")
        for i in adj[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

input = lambda: sys.stdin.readline().rstrip()
# 문제의 수 n, 정보의 개수 m
n, m = map(int, input().split())
# 진입 차수
indegree = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

topology(indegree)