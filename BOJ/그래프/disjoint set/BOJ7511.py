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

sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
# 테스트 케이스 t
t = int(input())
for i in range(t):
    # 유저의 수 n
    n = int(input())
    parent = [i for i in range(n)]
    # 친구 관계의 수 k 
    k = int(input())
    for _ in range(k):
        # 친구 관계
        a, b = map(int, input().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)

    # 미리 구할 쌍의 수 m
    m = int(input())
    print(f"Scenario {i+1}:")
    for _ in range(m):
        # 해야하는 쌍 u, v
        u, v = map(int, input().split())
        if find_parent(parent, u) == find_parent(parent, v):
            print(1)
        else:
            print(0)
    print()