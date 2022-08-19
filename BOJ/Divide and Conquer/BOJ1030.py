import sys
def dc(size, k, x, y, s):
    # 가운데 위치
    m = (size - k) // 2
    print(size, m, x, y)
    for i in range(x + m, x + m + k):
        for j in range(y + m, y + m + k):
            graph[i][j] = 1
    # 시간이 다 되었을 때
    if s == 1:
         return
    size //= N
    for i in range(s + 1):
        for j in range(s + 1):
            dc(size, k // N, x + size * i, y + size * j, s - 1)

input = lambda : sys.stdin.readline().rstrip()
# 시간 S, N*N 흰색, K*K 검정, 출력할 시작행 R1, 끝 행 R2, 시작 열 C1, 끝 열 C2
S, N, K, R1, R2, C1, C2 = map(int, input().split())
graph = [[0] * N**S for _ in range(N**S)]
# 한 변의 길이, 검정색 한 변의 길이, 시작 행 위치, 시작 열 위치, 시간
dc(N ** S, K * (N**S//N), 0, 0, S)
for x in graph:
    print(x)