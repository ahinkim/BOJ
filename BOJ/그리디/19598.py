import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()
# 회의 개수
N = int(input())

meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

# 회의실에 들어갈 회의들 오름차순 정렬
meetings.sort()

# 회의실(가장 마지막으로 끝난 회의시간만 저장 => 다른 정보는 필요없기 때문에)
q = [meetings[0][1]]
for meeting in meetings[1:]:
    # 현재 회의실에 들어갈 회의
    s, e = meeting
    # 회의실 중 끝나는 시간이 가장 작은 회의실(마지막으로 끝난 회의 시간) 빼기
    he = heapq.heappop(q)
    # 들어갈 회의의 시작시간이 회의실에 있는 회의보다 더 작다면
    if he > s:
        # 둘은 같은 회의실에 들어갈 수 없기 때문에 따로 저장
        heapq.heappush(q, he)
    # 같은 회의실에 들어갈 수 있다면 회의실(마지막으로 끝난 시간) 하나만 저장, 
    # 즉 항상 q의 원소 개수는 최소 회의실의 개수가 된다.
    heapq.heappush(q, e)

print(len(q))