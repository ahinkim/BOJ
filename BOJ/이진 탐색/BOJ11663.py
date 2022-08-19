import sys
from bisect import bisect_left, bisect_right
input = lambda : sys.stdin.readline().rstrip()
# 점의 개수 N, 선분의 개수 M
N, M = map(int, input().split())
# 점의 좌표
coordinates = list(map(int, input().split()))
coordinates.sort()
for i in range(M):
    # 선분의 시작점과 끝점
    s, e = map(int, input().split())
    s, e = bisect_left(coordinates, s), bisect_right(coordinates, e)
    print(e-s)