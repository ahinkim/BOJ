import sys
input = lambda : sys.stdin.readline().rstrip()
# 건물 종류의 개수 N, 건물 사이 관계의 개수 M, 영우의 게임 정보의 개수 K
N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    indegree[Y] += 1

# 건설한 건물
build = [0] * (N + 1)
# 영우의 건물 건설 순서
res = "King-God-Emperor"
for _ in range(K):
    # 명령, 건물
    cmd, a = map(int, input().split())
    # 건물을 건설했을 때
    if cmd == 1:
        # 건설할 수 없는 건물을 건설할 때(순서 맞지 않을 때)
        if indegree[a] > 0:
            res = "Lier!"
        # 한 건물을 여러 번 지을 수 있기 때문에 한번도 지어진 적 없는 건물만 인접건물의 진입차수 빼기
        if build[a] == 0:
            for i in graph[a]:
                indegree[i] -= 1
        # 건설한 건물의 개수 ++
        build[a] += 1
    # 건물을 파괴했을 때
    else:    
        # 건설한적 없는 건물이 파괴되었을 때
        if build[a] == 0:
            res = "Lier!"
        else:
            build[a] -= 1
            # 건물이 아예 사라졌을 때 진입차수 다시 만들기
            if build[a] == 0:
                for i in graph[a]:
                    indegree[i] += 1

print(res)