import sys
import math
input = lambda : sys.stdin.readline().rstrip()
# 색을 칠해야 하는 문제의 수 N
N = int(input())
# 문제 R 빨간색, B 파란색
problem = input()

prev = problem[0]
cnt = 0
for now in problem[1:]:
    if prev != now:
        cnt += 1
        prev = now

print(math.ceil(cnt/2)+1)