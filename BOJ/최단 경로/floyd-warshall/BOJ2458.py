# 학생들의 수 N, 두 학생 키를 비교한 횟수 M
N, M = map(int, input().split())

adj = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    # 두 학생의 키를 비교한 결과
    a, b = map(int, input().split())
    # 0: 키 비교를 못하는 경우, 1: a < b, 2: b > a
    adj[a][b] = 1
    adj[b][a] = 2

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            # a가 k보다 작고 k가 b보다 작으면 a는 b보다 작다 b는 a보다 크다
            if adj[a][k] == 1 and adj[k][b] == 1:
                adj[a][b] = 1
                adj[b][a] = 2

ans = N
for a in range(1, N+1):
    for b in range(1, N+1):
        # 키 비교를 못하는 경우
        if a!=b and adj[a][b] == 0:
            ans -= 1
            break

print(ans)