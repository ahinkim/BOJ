import sys
from collections import Counter
# 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
names = []
# 듣도 못한 사람의 이름
for _ in range(N):
    names.append(input())
# 보도 못한 사람의 이름
for _ in range(M):
    names.append(input())
# most_common()함수를 통해 배열로 바꿔줘야 값에 인덱스로 접근할 수 있다.
counter = Counter(names).most_common()
ans = []
for c in counter:
    if c[1] == 1:
        break
    ans.append(c[0])
ans.sort()
print(len(ans))
print(*ans, sep="\n")