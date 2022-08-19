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

V, E = map(int, input().split())
info = []
parent = [i for i in range(V + 1)]
for _ in range(E):
  A, B, C = map(int ,input().split())
  info.append((C, A, B))

info.sort()
result = 0
for C, A, B in info:
  if find_parent(parent, A) != find_parent(parent, B):
    union_parent(parent, A, B)
    result += C
print(result)