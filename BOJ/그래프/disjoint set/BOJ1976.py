import sys
input = lambda : sys.stdin.readline().rstrip()
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

# 도시의 수
N = int(input())
# 여행 계획에 속한 도시들의 수
M = int(input())
parent = [i for i in range(N)]
# 도시의 연결 정보
for i in range(N):
    _input = list(map(int, input().split()))
    for j in range(N):
        if _input[j] == 1:
            if find_parent(parent, i) != find_parent(parent, j):
                union_parent(parent, i, j)

parent = [find_parent(parent, i) for i in range(N)]
# 여행 계획
plans = list(map(int, input().split()))
ans = "YES"
for i in range(1, M):
    a = plans[i - 1] - 1
    b = plans[i] - 1
    if parent[a] != parent[b]:
        ans = "NO"
        break
print(ans)