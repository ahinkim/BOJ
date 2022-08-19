import sys
def binary(start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for h in heights:
            if h > mid:
                total += h - mid
        if total == m:
            return mid
        elif total > m:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res
input = lambda : sys.stdin.readline().rstrip()
# 나무의 수 n, 나무의 길이 m
n, m = map(int, input().split())
# 나무의 높이
heights = list(map(int, input().split()))
print(binary(0, max(heights)))