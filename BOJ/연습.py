import sys
def keyValue(x):
    return students[x]

input = lambda : sys.stdin.readline().rstrip()
# 사진들의 개수 N
N = int(input())
# 전체 학생의 총 추천 횟수
M = int(input())
# 추천 받은 학생 번호
recommended = list(map(int, input().split()))
# 학생 별 추천 받은 수 
students = [0]*101

# 게시된 사진들
q = []
for rnum in recommended:
    students[rnum] += 1
    if rnum in q:
        q.sort(key = keyValue)
        print(rnum, q)
        continue
    elif len(q) < N:
        q.append((rnum))
    else:
        remove = q.pop(0)
        students[remove] = 0
        q.append((rnum))
    q.sort(key = keyValue)
    print(rnum, q)

q.sort()
print(*q)