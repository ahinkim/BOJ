import sys
from collections import deque
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    if stones[a] < stones[b]:
        stones[b] = stones[a]
    else:
        stones[a] = stones[b]

sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
# 강의동의 수 N, 공사구간의 수 M, 건덕이가 가진 돌의 수 K
n, m, k = map(int, input().split())
# 강의동에서 와우도까지 놓아야하는 돌의 개수
stones = [0]
stones.extend(list(map(int, input().split())))
edges = []
is_blocked = [False] * (n + 1)
for i in range(1, n):
    edges.append((i, i + 1))
edges.append((n, 1))

for _ in range(m):
    # 공사중인 길
    i, j = map(int, input().split())
    is_blocked[j] = True

parent = [i for i in range(n + 1)]
for a, b in edges:
    if not is_blocked[b]:
        union_parent(parent, a, b)
parent = [find_parent(parent, i) for i in range(n + 1)]
# 중복 제거
parent = set(parent[1:])
res = 0
# parent 원소가 1개 밖에 없는 경우 모두 연결되어 있는 것
if len(parent) > 1:
    for x in parent:
        res += stones[x]
if res <= k:
    print('YES')
else:
    print('NO')