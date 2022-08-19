import sys
from collections import deque
def topology():
    q = deque()
    progenitors = []
    for person in people:
        if indegree[person] == 0:
            q.append(person)
    # 각 가문의 시조들 출력
    print(len(q))
    for x in q:
        print(x, end=' ')
    print()

    while q:
        now = q.popleft()
        for i in adj[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                children[now].append(i)

input = lambda : sys.stdin.readline().rstrip()
# 석호촌에 살고 있는 사람의 수 N
N = int(input())
# 현재 살고 있는 사람들의 이름
people = list(input().split())
people.sort()
# 기억하는 정보의 개수 M 
M = int(input())
adj = {person:[] for person in people}
indegree = {person:0 for person in people} 
# 자식들
children = {person:[] for person in people}

for i in range(M):
    # X의 조상 중에 Y가 있다
    X, Y = input().split()
    adj[Y].append(X)
    indegree[X] += 1

topology()

# 사람이름 자식 수
for p, c in children.items():
    print(p, end=' ')
    print(len(c), end=' ')
    c.sort()
    print(*c, sep=' ')