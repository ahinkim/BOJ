import sys
def binary(target):
    start = 1 # 1초
    end = time[0] * M # 최대 초: 1명당 수용시간이 제일 적은 심사대에 모든 인원이 심사 받는다고 했을 때
    res = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for t in time:
            # mid초 동안 심사할 수 있는 인원
            total += mid // t
        # 인원을 수용할 수 있을 때 더 적은 시간으로 수용할 수 있는 지 확인
        if total >= target:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res

input = lambda : sys.stdin.readline().rstrip()
# 입국심사대 N, 상근이와 친구들 M
N, M = map(int, input().split())
# 한 명을 심사하는 데 걸리는 시간
time = []
for _ in range(N):
    t = int(input())
    time.append(t)
time.sort()
print(binary(M))