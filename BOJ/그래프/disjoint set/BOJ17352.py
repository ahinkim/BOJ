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
# 섬 N개
N = int(input())

# 모든 다리
edges = list(zip(range(1, N), range(2, N+1)))
parent = [i for i in range(N+1)]

for _ in range(N-2):
    # 이어진 두 섬의 번호
    a, b = map(int, input().split())
    # 이어진 섬 다리 연결
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

parent = [find_parent(parent, i) for i in range(N+1)]
for edge in edges:
    a, b = edge
    # 연결되지 않은 다리가 있다면 연결
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # 연결되지 않은 다리 == 다리로 이을 두 섬의 번호 
        print(a, b)