import sys
input = lambda : sys.stdin.readline().rstrip()
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
total = [0] * (k + 1)
total[0] = 1
for i in range(n):
    for j in range(1, k + 1):
        if coin[i] <= j:
            total[j] += total[j - coin[i]]
print(total[k])