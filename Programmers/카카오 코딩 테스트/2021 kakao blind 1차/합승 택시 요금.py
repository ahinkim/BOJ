def solution(n, s, a, b, fares):
    INF = int(1e9)
    adj = [[INF]*(n+1) for _ in range(n+1)]
    # 경로 비용 입력
    for i, j, c in fares:
        adj[i][j] = c
        adj[j][i] = c
    # 자기 자신으로 가는 길 0으로 저장
    for i in range(n+1):
        adj[i][i] = 0
    # 플로이드를 이용해 모든 지점까지의 최단 거리 구하기
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])
    # 출발 지점(s)에서 모든 지점을 걸쳐 a, b에 도착하는 거리 중 최소 거리 구하기(s->? + ?->a + ?->b, 만약 물음표가 a일 경우 s->a->b의 경우도 알 수 있다. 또한 ?가 s일 경우 출발 지점에서 합승하지 않는 경우도 구할 수 있다.)
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, adj[s][i] + adj[i][a] + adj[i][b])
    return answer