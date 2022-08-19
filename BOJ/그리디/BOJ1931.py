import sys
input = lambda : sys.stdin.readline().rstrip()
# 회의의 수 N
N = int(input())

meetings = []
for _ in range(N):
    # 회의의 시작 시간 s, 끝나는 시간 e
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key = lambda x:(x[1], x[0]))
q = [meetings[0][1]]

for i in range(1, N):
    s, e = meetings[i]
    if q[-1] <= s:
        q.append(e)

print(len(q))