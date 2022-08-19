import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
costs = []
for _ in range(N):
    costs.append(int(input()))

costs.sort(reverse = True)
ans = 0
for i in range(N):
    if (i+1) % 3 != 0:
        ans += costs[i]

print(ans)