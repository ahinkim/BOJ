import sys
input = lambda : sys.stdin.readline().rstrip()
# 원생 수 n, 조 k
n, k = map(int, input().split())
data = list(map(int, input().split()))
# 원생 i, i + 1, 연결된 비용
cost = []
for i in range(n - 1):
    cost.append((data[i + 1] - data[i]))
cost.sort()
# 끝에서 k - 1개의 연결 비용 제거 
for _ in range(k - 1):
    cost.pop()
print(sum(cost))