import sys
from collections import deque
def topology():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            res[i] = time[i] # 초기 건물 짓는 값은 초기화해줘야 한다.

    while q:
        now = q.popleft()
        for i in adj[now]:
            indegree[i] -= 1
            res[i] = max(res[i], res[now]+time[i])
            if indegree[i] == 0:
                q.append(i)

input = lambda : sys.stdin.readline().rstrip()
# 건물의 종류 수 
N = int(input())
adj = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
# 건물을 짓는 데 걸리는 시간
time = [0]*(N+1)
# N개의 각 건물이 완성되기까지 걸리는 최소 시간
res = [0]*(N+1)

for i in range(N):
    # 건물을 짓는 데 걸리는 시간, 건물을 짓기 위해 먼저 지어져야 하는 건물들의 번호
    _input = list(map(int, input().split())) # 정수로 받을 때는 map()꼭 쓰자. 안그러면 문자열로 받아진다.
    time[i+1] = _input[0]
    for x in _input[1:-1]:
        adj[x].append(i+1)
    indegree[i+1] = len(_input)-2

topology()
print(*res[1:], sep = "\n")