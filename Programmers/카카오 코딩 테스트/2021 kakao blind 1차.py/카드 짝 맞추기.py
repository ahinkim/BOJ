from collections import deque
from copy import deepcopy
# 카드 사이의 최단 거리 구하기
def get_short_dist(board, start_x, start_y, target):
    # 상, 하, 좌, 우
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 방문 기록
    visited = [[False]*4 for _ in range(4)]
    q = deque([(0, start_x, start_y)])
    visited[start_x][start_y] = True
    while q:
        d, x, y = q.popleft()
        if board[x][y] == target:
            return d, x, y
        # 상하좌우 이동
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue
            if not visited[nx][ny]:
                q.append((d+1, nx, ny))
                visited[nx][ny] = True
        # ctrl+상하좌우 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue
            while 0 <= nx+dx[i] < 4 and 0 <= ny+dy[i] < 4:
                # 가장 가까운 카드로 이동 (가까운 카드가 없다면 끝까지 이동)
                if board[nx][ny] != 0:
                    break
                nx, ny = nx + dx[i], ny + dy[i]
            if not visited[nx][ny]:
                q.append((d+1, nx, ny))
                visited[nx][ny] = True

def is_end(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                return False
    return True

# 최소 키 조작 횟수 (solution 함수 안에 초기화 하면 에러 난다. 전역 변수 초기화는 함수 밖에서)
answer = int(1e9)

def dfs(board, start_x, start_y, target, cnt): # cnt = 키 조작 횟수
    global answer
    board = deepcopy(board)
    # 커서가 놓인 시작 위치부터 다음 카드를 선택하는 위치까지의 최단 거리를 구한다.
    d, target_x, target_y = get_short_dist(board, start_x, start_y, target)
    cnt += d
    # 카드를 선택한 시작 위치부터 해당 카드와 같은 숫자 카드의 최단 거리를 구한다.
    start_x, start_y = target_x, target_y
    target = board[start_x][start_y]
    board[start_x][start_y] = 0
    d, target_x, target_y = get_short_dist(board, start_x, start_y, target)
    board[target_x][target_y] = 0
    cnt += d
    # 두 개의 카드를 뒤집는다.
    cnt += 2
    if is_end(board):
        answer = min(answer, cnt)
        return
    # 보드를 돌며 두번 째 카드를 선택할 위치를 모두 탐색한다.
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dfs(board, target_x, target_y, board[i][j], cnt)
    
def solution(board, r, c):
    # 보드를 돌며 카드를 처음 선택하는 위치 6개를 모두 탐색한다. (총 카드 개수 6개)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                dfs(board, r, c, board[i][j], 0)
                

    return answer

# solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)