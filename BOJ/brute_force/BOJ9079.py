import sys
from copy import deepcopy
from collections import deque
# 행 뒤집는 함수
def turn_row(graph, r):
    for i in range(3):
        if graph[r][i] == 1:
            graph[r][i] = 0
        else:
            graph[r][i] = 1

# 열 뒤집는 함수
def turn_col(graph, c):
    for i in range(3):
        if graph[i][c] == 1:
            graph[i][c] = 0
        else:
            graph[i][c] = 1

# 왼쪽 대각선 뒤집는 함수
def turn_left(graph):
    for i in range(3):
        if graph[i][i] == 1:
            graph[i][i] = 0
        else:
            graph[i][i] = 1

# 오른쪽 대각선 뒤집는 함수
def turn_right(graph):
    for i in range(3):
        if graph[i][2-i] == 1:
            graph[i][2-i] = 0
        else:
            graph[i][2-i] = 1

# 비트 숫자로 변환
def bitToNum(graph):
    n = 8
    res = 0
    for i in range(3):
        for j in range(3):
            res += graph[i][j] * (2**n)
            n -= 1
    return res

# 숫자를 비트 graph로 바꾸기
def numToBit(num):
    bit = bin(num)[2:] # 맨 앞 0b 빼기 위해 [2:]
    bit = f'{bit:0>9}'
    graph = []
    for i in range(0, 9, 3):
        graph.append(list(map(int, bit[i:i+3])))
    return graph

# 모두 같은 면인지 확인하기
def isAllSame(graph):
    f = graph[0][0]
    for i in range(3):
        for j in range(3):
            if graph[i][j] != f:
                return False
    return True
def bfs(graph):
    idx = bitToNum(graph)
    # 비트 graph를 숫자로 바꾼 idx와 현재까지 뒤집은 횟수 cnt 저장
    q = deque([(idx, 0)])
    while q:
        idx, cnt = q.popleft()
        if not visited[idx]:
            visited[idx] = True
        else:
            continue
        if isAllSame(numToBit(idx)):
            return cnt
        # 숫자를 비트 graph로 바꾸기
        graph = numToBit(idx)
        # 1번 ~ 3번 행 뒤집기
        for i in range(3):
            copy_graph = deepcopy(graph) 
            turn_row(copy_graph, i)
            q.append((bitToNum(copy_graph), cnt + 1))
        # 1번 ~ 3번 열 뒤집기
        for i in range(3):
            copy_graph = deepcopy(graph) 
            turn_col(copy_graph, i)
            q.append((bitToNum(copy_graph), cnt + 1))
        # 왼쪽 대각선 뒤집기
        copy_graph = deepcopy(graph) 
        turn_left(copy_graph)
        q.append((bitToNum(copy_graph), cnt + 1))
        # 오른쪽 대각선 뒤집기
        copy_graph = deepcopy(graph) 
        turn_right(copy_graph)
        q.append((bitToNum(copy_graph), cnt + 1))
    return -1

input = lambda : sys.stdin.readline().rstrip()
T = int(input())

graph = []
# 000000000 ~ 111111111
visited = [False] * (2**9 + 1)
INF = int(1e9)
for _ in range(T):
    # 문자를 비트로 바꿔주기: 'H' -> 1, 'T' -> 0
    for i in range(3):
        data = input().split()
        for j in range(3):
            if data[j] == 'H':
                data[j] = 1
            else:
                data[j] = 0
        graph.append(data)

    ans = bfs(graph)
    print(ans)