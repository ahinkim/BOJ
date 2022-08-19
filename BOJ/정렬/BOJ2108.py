import sys
from collections import Counter
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
array = []
for _ in range(N):
    num = int(input())
    array.append(num)

array.sort()
counter = Counter(array).most_common(2)
# 산술평균
print(round(sum(array) / N))
# 중앙값
print(array[N//2])
# 최빈값
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])
# 범위
print(max(array) - min(array))