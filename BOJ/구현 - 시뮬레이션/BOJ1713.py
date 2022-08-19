import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()
# 사진들의 개수 N
N = int(input())
# 전체 학생의 총 추천 횟수
M = int(input())
# 추천 받은 학생 번호
recommended = list(map(int, input().split()))
# 학생 별 추천 받은 수 
dic = defaultdict(int)

for rnum in recommended:
    if rnum not in dic.keys() and len(dic) == N: # if dic[rnum] == 0 and len(dic) == N:
        key = list(dic.keys())
        val = list(dic.values())
        # 제일 작은 값 중 첫 번째(오래된) 인덱스
        temp = val.index(min(val))
        idx = key[temp]

        del(dic[idx])

    dic[rnum] += 1

print(*sorted(dic.keys()))