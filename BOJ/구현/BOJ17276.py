import sys
# 시계 방향
def forward(graph):
    for _ in range(d):
        prev = []
        for i in range(n):
            prev.append(graph[i][i])
        # 주 대각선 => 가운데 열
        for j in range(n):
            temp = graph[j][n // 2]
            graph[j][n // 2] = prev[j]
            prev[j] = temp
        # 가운데 열 => 부 대각선
        r = 0
        for c in reversed(range(n)):
            temp = graph[r][c]
            graph[r][c] = prev[r]
            prev[r] = temp 
            r += 1
        # 부 대각선 => 가운데 행
        for j in range(n):
            temp = graph[n // 2][j]
            graph[n // 2][j] = prev[n - j - 1]
            prev[n - j - 1] = temp
        # 가운데 행 => 주 대각선 
        for j in range(n):
            temp = graph[j][j]
            graph[j][j] = prev[n - j - 1]
            prev[n - j - 1] = temp

def reverse(graph):
    for _ in range(-d):
        prev = []
        for i in range(n):
            prev.append(graph[i][i])
        # 주 대각선 => 가운데 행
        for j in range(n):
            temp = graph[n // 2][j]
            graph[n // 2][j] = prev[j]
            prev[j] = temp
        # 가운데 행 => 부 대각선
        c = 0
        for r in reversed(range(n)):
            temp = graph[r][c]
            graph[r][c] = prev[c]
            prev[c] = temp 
            c += 1
        # 부 대각선 => 가운데 열
        for j in range(n):
            temp = graph[n - j - 1][n // 2]
            graph[n- j - 1][n // 2] = prev[j]
            prev[j] = temp
        # 가운데 열 => 주 대각선 
        for j in range(n):
            temp = graph[j][j]
            graph[j][j] = prev[n - j - 1]
            prev[n - j - 1] = temp
t = int(input())
input = lambda : sys.stdin.readline().rstrip()
for _ in range(t):
    # 배열의 크기, 각도
    n, d = map(int, input().split())
    d //= 45
    graph = [list(map(int, input().split())) for _ in range(n)]
    if d > 0:
        forward(graph)
    elif d < 0:
        reverse(graph)

    for i in range(n):
        print(*graph[i])