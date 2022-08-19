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
# 행성의 수
n = int(input())
edges = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        # 플로우 관리비용 data[j], 행성 i, j
        edges.append((data[j], i, j))

edges.sort()
parent = [i for i in range(n)]
res = 0
for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent ,b):
        union_parent(parent, a, b)
        res += c
print(res)