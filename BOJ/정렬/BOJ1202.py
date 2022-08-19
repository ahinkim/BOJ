import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()
# 보석의 개수 N, 가방의 개수 K
N, K = map(int, input().split())

dia = []
for _ in range(N):
    # 보석의 정보: 무게 M, 가격 V
    M, V = map(int, input().split())
    dia.append((M, V))
dia.sort()

back = []
for _ in range(K):
    # 가방에 담을 수 있는 최대 무게 C
    C = int(input())
    back.append(C)
back.sort()

q = []
total = 0
for b in back:
    while dia and dia[0][0] <= b:
        d = heapq.heappop(dia)
        # 보석의 가치 최대힙에 저장
        heapq.heappush(q, -d[1])
    if q:
        total -= heapq.heappop(q)
print(total)
