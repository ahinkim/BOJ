import sys
sys.setrecursionlimit(10**5)
def dfs(visited, finished, check, v):
    global cycle
    if finished[v]:
        return
    if visited[v]:
        # 사이클을 이루고 있는 노드 개수 구하기
        cycle = len(check) - check.index(v)
        return
    visited[v] = True
    check.append(v)
    next = data[v]
    dfs(visited, finished, check, next)
    finished[v] = True 

input = lambda : sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n = int(input())
    data = [0]
    data.extend(list(map(int, input().split())))
    res = 0
    finished = [False] * (n + 1)
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        cycle = 0
        # 어디서부터 cycle인지 확인하기 위한 리스트
        check = []
        if not visited[i]:
            dfs(visited, finished, check, i)
            if cycle:
                res += cycle
    print(n - res)