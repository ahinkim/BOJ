import sys
input = lambda : sys.stdin.readline().rstrip()
# 도시의 개수
N = int(input())
# 두 도시를 연결하는 도로의 길이
road = list(map(int, input().split()))
# 주유소의 리터당 가격
cost = list(map(int, input().split()))
min_cost = cost[0]
res = cost[0] * road[0]

for i in range(1, N - 1):
    min_cost = min(min_cost, cost[i])
    res += min_cost * road[i]
print(res)