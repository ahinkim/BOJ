from itertools import combinations
from math import sqrt
def find_parent(parent ,x):
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
# 별의 개수
n = int(input())
# 별들의 좌표
stars = []
for i in range(n):
    # 좌표
    x, y = map(float, input().split())
    stars.append((x, y))
# 별 두 개씩 조합
candidate = list(combinations(range(n), 2))
# 별들 사이 거리
edges = []
for a, b in candidate:
    x1, y1 = stars[a]
    x2, y2 = stars[b]
    edges.append((sqrt((x1-x2)**2 + (y1-y2)**2), a, b))
edges.sort()

ans = 0
parent = [i for i in range(n)]
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost
# 별자리 만드는 최소 비용
print(f'{ans:.2f}')