import sys
from collections import deque
# 위상정렬 수행
def topology():
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    while q:
        now = q.popleft()
        for i in graph[now]:
            cost = dp[now] + time[i]
            if cost > dp[i]:
                dp[i] = cost
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
# 인접 행렬
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
# 각 작업에 걸리는 시간
time = [0] * (N + 1)
# 각 작업이 완료되기 까지 걸리는 총 시간(선행 작업 시간 포함)
dp = [0] * (N + 1)
for i in range(1, N + 1):
    # 작업에 걸리는 시간, 선행관계에 있는 작업들의 개수, 선행 관계에 있는 작업들의 번호
    data = list(map(int, input().split()))
    indegree[i] += data[1]
    time[i] = data[0]
    for x in data[2:]:
        graph[x].append(i)
topology()
print(max(dp))