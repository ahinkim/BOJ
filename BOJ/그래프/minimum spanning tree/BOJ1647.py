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

n, m = map(int, input().split())
parent = [0] * (n + 1)
edges = []

for i in range (1, n + 1):
  parent[i] = i

for _ in range(m):
  A, B, C = map(int, input().split())
  edges.append((C, A, B))

edges.sort()

result = 0
final_cost = 0

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    final_cost = cost

print(result - final_cost)