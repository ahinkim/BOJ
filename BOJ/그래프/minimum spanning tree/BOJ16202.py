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
# 그래프의 정점의 개수 N, 그래프 간선의 개수 M, 턴의 수 K
N, M, K = map(int, input().split())
edges = []
w = 1
for _ in range(M):
    a, b = map(int, input().split())
    edges.append((w, a, b))
    w += 1

edges.sort()

for _ in range(K):
    parent = [i for i in range(N+1)]
    cost = 0
    for edge in edges:
        w, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cost += w

    parent = [find_parent(parent, i) for i in range(N+1)] 
    # MST가 아닐 때
    if len(set(parent[1:])) == 1:
        print(cost, end=' ')
    else:
        print(0, end = ' ')
    edges.pop(0)