import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
data = list(map(int, input().split()))
candidates = []
for i in range(n):
    # 눈덩이 번호와 지름 저장
    candidates.append((i, data[i]))
candidates = list(combinations(candidates, 2))
snows = []
for candidate in candidates:
    num1, r1 = candidate[0]
    num2, r2 = candidate[1]
    # 눈사람의 키, 구성된 눈덩이 번호1, 2
    snows.append((r1 + r2, num1, num2))
# 눈사람 키 순으로 정렬
snows.sort()
# 만들 수 있는 눈사람 개수
m = len(snows)
min_value = int(1e10)
for i in range(m - 1):
    a = snows[i]
    b = snows[i + 1]
    # 겹치는 눈덩이가 있다면 continue
    if a[1] == b[1] or a[1] == b[2] or a[2] == b[1] or a[2] == b[2]:
        continue
    min_value = min(min_value, b[0] - a[0])
print(min_value)