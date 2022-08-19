import sys
def is_promising(col):
    if col in row:
        return False
    return True
# i == 행
def dfs(graph, i, total):
    global max_value
    if i == 11:
        max_value = max(max_value, total)
        return
    for j in range(11):
        if graph[i][j] != 0 and is_promising(j):
            row[i] = j
            dfs(graph, i + 1, total + graph[i][j])
            row[i] = -1

input = lambda : sys.stdin.readline().rstrip()
# 테스트 케이스 개수
c = int(input())
for _ in range(c):
    row = [-1] * 11
    graph = []
    for _ in range(11):
        graph.append(list(map(int, input().split())))
    max_value = 0
    dfs(graph, 0, 0)
    print(max_value)