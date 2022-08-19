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
# 점의 개수, 차례의 수
n, m = map(int, input().split())
parent = [i for i in range(n)]
ans = 0
for i in range(1, m + 1):
    # 플레이어가 선택한 두 번호
    a, b = map(int ,input().split())
    if ans == 0 and find_parent(parent, a) == find_parent(parent, b):
        ans = i
    union_parent(parent, a, b)

print(ans)