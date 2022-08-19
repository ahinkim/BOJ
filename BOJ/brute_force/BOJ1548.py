import sys
input = lambda : sys.stdin.readline().rstrip()
# 수열의 크기 n
n = int(input())
# 수열 A
A = list(map(int, input().split()))
A.sort()
start = 0
ans = 0
for i in range(2, n):
    if A[start] + A[start + 1] <= A[i]:
        ans = max(ans, i - start)
        while start < i and A[start] + A[start + 1] <= A[i]:
            start += 1
ans = max(ans, n - start)
print(ans)