import sys
from collections import deque
def topology():
    q = deque()
    for i in range(1, M+1):
        if indegree[i] == 0:
            q.append((1, i))
    while q:
        order, now = q.popleft()
        for i in adj[now]:
            indegree[i] -= 1
            if order > max_order[i]: 
                max_order[i] = order
                count[i] = 1
            elif order == max_order[i]:
                count[i] += 1
            if indegree[i] == 0:
                if count[i] == 1:
                    q.append((max_order[i], i))
                else:
                    q.append((max_order[i]+1, i))
    return order

input = lambda : sys.stdin.readline().rstrip()
T = int(input())
for i in range(T):
    # 테스트 케이스 번호, 노드의 수, 간선의 수
    K, M, P = map(int, input().split())
    indegree = [0] * (M+1)
    # 들어오는 강의 순서 중 가장 큰 값
    max_order = [0] * (M+1)
    # 순서가 가장 큰 값의 강이 들어오는 개수
    count = [0] * (M+1)
    adj = [[] for _ in range(M+1)]
    for _ in range(P):
        # 간선의 정보
        A, B = map(int, input().split())
        indegree[B] += 1
        adj[A].append(B)
    print(i+1, topology())