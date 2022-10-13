import sys
input = lambda : sys.stdin.readline().rstrip()
T = int(input())
INF = int(1e9)
for _ in range(T):
    # 방의 개수 N, 비밀 통로의 개수 M
    N, M = map(int, input().split())
    adj = [[INF]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        # 두 방 번호 a, b, 통로 길이 c
        a, b, c = map(int, input().split())
        adj[a][b] = c
        adj[b][a] = c
    # 모임에 참여하는 친구의 수 K
    K = int(input())
    friends = list(map(int, input().split()))
    for i in range(K):
        friends[i]
    # 자기 자신으로 이동하는 거리 0으로 초기화    
    for i in range(1, N+1):
        adj[i][i] = 0
    # 플로이드
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                adj[a][b] = min(adj[a][b], adj[a][k]+adj[k][b])
    # 친구들의 이동 거리의 총합이 최소가 되는 방 번호 찾기
    min_d = INF
    res = 0
    for i in range(1, N+1):
        total_d = 0
        for friend in friends:
            total_d += adj[friend][i]
        if min_d > total_d:
            res = i
            min_d = total_d
    print(res)