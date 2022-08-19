# 빙고인지 확인
def check(r, c):
    # 빙고가 될 수 있는 총 경우의 수 
    bingo = 0
    # 주 대각선
    if r+c == 4 and graph[0][4]+graph[1][3]+graph[2][2]+graph[3][1]+graph[4][0] == -5:
        bingo += 1
    # 반대 대각선
    if r==c and graph[0][0]+graph[1][1]+graph[2][2]+graph[3][3]+graph[4][4] == -5:
        bingo += 1
    # 해당 행의 열 0 ~ 4까지, 해당 열의 행 0~ 4 빙고인지 확인
    if sum(graph[r]) == -5:
        bingo += 1
    if sum([graph[i][c] for i in range(5)]) == -5:
        bingo += 1
    return bingo
        
# 빙고판
graph = []
# 각 숫자 위치(행, 열)
loc = dict()
# 빙고판 숫자 입력
for i in range(5):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(5):
        # dict에다 숫자 위치 저장
        loc[data[j]] = (i, j)

nums = []
# 사회자가 부르는 수 입력
for _ in range(5):
    nums.extend(list(map(int, input().split())))
ans = 0
for i in range(25):
    # 사회자가 부른 숫자 지우기 
    r, c = loc[nums[i]]
    graph[r][c] = -1
    # 빙고 개수 더하기
    ans += check(r, c)
    if ans >= 3:
        print(i + 1)
        break