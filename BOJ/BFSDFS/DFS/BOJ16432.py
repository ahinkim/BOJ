import sys
def dfs(prev, d): # prev: 이전 날 먹은 떡 종류 d: 날짜
    global route
    global ans
    if d == N:
        ans = route[:]
        return

    for i in adj[d]:
        # 이전 날 먹은 떡과 다른종류 and 먹지 않았던 떡
        if i != prev and not dp[d][i]:
            dp[d][i] = True
            route.append(i)
            dfs(i, d+1)
            route.pop()


input = lambda : sys.stdin.readline().rstrip()
# 떡을 팔아야 할 날의 수 N
N = int(input())

# 떡을 먹었는 지 여부
dp = [[False] * 10 for _ in range(N)]
adj = [[] for _ in range(N)]
for i in range(N):
    #  동희가 들고 가는 떡들의 개수 m, 동희가 가져가는 떡의 종류
    _input = list(map(int, input().split()))
    adj[i].extend(_input[1:])

# 가능한 종류의 떡 경로
route = []
ans = []
dfs(-1, 0)
if ans:
    print(*ans, sep="\n")
else:
    print(-1)