import sys
# 상한액 구하기
def binary(start, end):
    res = 1
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for budget in budgets:
            if budget <= mid:
                total += budget
            else:
                total += mid
        if total <= M:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res
input = lambda : sys.stdin.readline().rstrip()
# 지방의 수
N = int(input())
# 각 지방의 예산 요청
budgets = list(map(int, input().split()))
# 총 예산
M = int(input())

# 정수 상한액 계산
print(binary(1, max(budgets)))