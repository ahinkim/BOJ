import sys
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
# 건물의 개수, 도로의 개수
N, M = map(int, input().split())
ex_cost = 0
edges = []
parent = [i for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    ex_cost += c

edges.sort()
now_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        now_cost += cost
parent = [find_parent(parent, i) for i in range(N + 1)]

# 모든 건물이 연결되어 있지 않은 경우
if len(set(parent[1:])) != 1:
    print(-1)
else:
    print(ex_cost - now_cost)
