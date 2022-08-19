import sys
# 이 부분 없으면 틀린다. 파이썬은 재귀 깊이 제한이 1000밖에 안되기 때문에 재귀문제는 항상 설정해주자.
sys.setrecursionlimit(10**6)
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

input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
  oper, a, b = map(int, input().split())
  if oper == 0:
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
  elif oper == 1:
    if find_parent(parent, a) == find_parent(parent, b):
      print('YES')
    else:
      print('NO')