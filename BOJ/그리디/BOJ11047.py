import sys
input = lambda : sys.stdin.readline().rstrip()
N, K = map(int, input().split())

data = []
for _ in range(N):
  data.append(int(input()))

ans = 0
for i in reversed(range(N)):
  if K == 0:
    break
  d, m = divmod(K, data[i])
  if d > 0:
    ans += d
    K = m
print(ans)