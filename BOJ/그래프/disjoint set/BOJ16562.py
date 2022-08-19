import sys
from copy import deepcopy
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
input = lambda : sys.stdin.readline().rstrip()
# 학생 수, 친구 관계 수, 갖고 있는 돈
n, m, k = map(int, input().split())
cost = [0]
cost.extend(list(map(int, input().split())))
parent = [i for i in range(n + 1)]
min_cost = deepcopy(cost)
for _ in range(m):
    a, b = map(int, input().split())
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        union_parent(parent, a, b)
        if min_cost[a] < min_cost[b]:
            min_cost[b] = min_cost[a]
        else:
            min_cost[a] = min_cost[b]

min_freinds = set()
for i in range(1, n + 1):
    min_freinds.add(find_parent(parent, i))
ans = 0
for x in min_freinds:
    ans += min_cost[x]

if ans == 0 or ans > k:
    print("Oh no")
else:
    print(ans)