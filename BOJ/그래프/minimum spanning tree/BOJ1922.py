import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
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
# 컴퓨터의 수 N
N = int(input())
# 선의 수 M
M = int(input())
parent = [i for i in range(N + 1)]
info = []
for _ in range(M):
  a, b, c = map(int, input().split())
  info.append((c, a, b))
info.sort()
ans = 0
for c, a, b in info:
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    ans += c

print(ans)