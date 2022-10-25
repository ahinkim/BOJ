import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()
# 회의 개수
N = int(input())

rooms = []
for _ in range(N):
    s, e = map(int, input().split())
    rooms.append((s, e))

rooms.sort()

q = [rooms[0][1]]
for room in rooms[1:]:
    s, e = room
    he = heapq.heappop(q)
    if he > s:
        heapq.heappush(q, he)
    heapq.heappush(q, e)

print(len(q))