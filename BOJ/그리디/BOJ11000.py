import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
data = []
for _ in range(n):
    s, t = map(int, input().split())
    data.append((s, t))
data.sort()

q = [data[0][1]]
for x, y in data[1:]:
    if x >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, y)
print(len(q))