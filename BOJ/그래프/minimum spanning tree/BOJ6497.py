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

while True:
    edges = []
    # 집의 수 m, 길의 수 n
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    init_cost = 0
    for _ in range(n):
        # x번 집과 y번 집 사이 거리가 z미터
        x, y, z = map(int, input().split())
        init_cost += z
        edges.append((z, x, y))

    edges.sort()

    parent = [i for i in range(m)]
    total_cost = 0

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost

    print(init_cost - total_cost)