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
    
    count[a] += count[b] 
    count[b] = count[a]

input = lambda : sys.stdin.readline().rstrip()
# 호재의 지시 횟수 N
N = int(input())
# 부품 개수
M = 10**6
parent = [i for i in range(M+1)]
# 총 부품 개수 저장
count = [1 for i in range(M+1)]

for _ in range(N):
    oper = list(input().split())
    if oper[0] == 'I':
        if find_parent(parent, int(oper[1])) != find_parent(parent, int(oper[2])):
            union_parent(parent, int(oper[1]), int(oper[2]))
    else:
        oper[1] = find_parent(parent, int(oper[1]))
        print(count[oper[1]])