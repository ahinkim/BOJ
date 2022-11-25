import sys
from copy import deepcopy
from collections import deque
# 동전 뒤집기
def turn_coin(x):
    if x == 1:
        return 0
    else:
        return 1
# 행 뒤집는 함수
def turn_row(bit, start):
    bit = deepcopy(bit)
    end = (start + 3)
    for i in range(start, end):
        bit[i] = turn_coin(bit[i])
    return bitToNum(bit)
# 열 뒤집는 함수
def turn_col(bit, start):
    bit = deepcopy(bit)
    for i in range(start, 9, 3):
        bit[i] = turn_coin(bit[i])
    return bitToNum(bit)
# 왼쪽 대각선 뒤집는 함수
def turn_left(bit):
    bit = deepcopy(bit)
    bit[0] = turn_coin(bit[0])
    bit[4] = turn_coin(bit[4])
    bit[8] = turn_coin(bit[8])
    return bitToNum(bit)
# 오른쪽 대각선 뒤집는 함수
def turn_right(bit):
    bit = deepcopy(bit)
    bit[2] = turn_coin(bit[2])
    bit[4] = turn_coin(bit[4])
    bit[6] = turn_coin(bit[6])
    return bitToNum(bit)

# 비트 숫자로 변환
def bitToNum(coins):
    res = 0
    for i in range(9):
        res += coins[i] * 2**(8-i)
    return res

# 숫자를 비트로 바꾸기
def numToBit(num):
    bit = bin(num)[2:] # 맨 앞 0b 빼기 위해 [2:]
    bit = f'{bit:0>9}'
    return list(map(int, bit))

# 모두 같은 면인지 확인하기
def isAllSame(bit):
    f = bit[0]
    for i in range(9):
        if bit[i] != f:
            return False
    return True

def bfs(coins):
    idx = bitToNum(coins)
    # 비트 graph를 숫자로 바꾼 idx와 현재까지 뒤집은 횟수 cnt 저장
    q = deque([(idx, 0)])
    while q:
        idx, cnt = q.popleft()
        bit = numToBit(idx)
        if visited[idx]:
            continue
        else:
            visited[idx] = True
        if isAllSame(bit):
            return cnt
        # 1번 ~ 3번 행 뒤집기
        for i in range(0, 9, 3): 
            q.append((turn_row(bit, i), cnt + 1))
        # 1번 ~ 3번 열 뒤집기
        for i in range(3): 
            q.append((turn_col(bit, i), cnt + 1))
        # 왼쪽 대각선 뒤집기
        q.append((turn_left(bit), cnt + 1))
        # 오른쪽 대각선 뒤집기
        q.append((turn_right(bit), cnt + 1))
    return -1

input = lambda : sys.stdin.readline().rstrip()
T = int(input())
INF = int(1e9)

for _ in range(T):
    coins = []
    # 000000000 ~ 111111111
    visited = [False] * (2**9)
    # 문자를 비트로 바꿔주기: 'H' -> 1, 'T' -> 0
    for i in range(3):
        data = input().split()
        for j in range(3):
            if data[j] == 'H':
                coins.append(1)
            else:
                coins.append(0)

    ans = bfs(coins)
    print(ans)