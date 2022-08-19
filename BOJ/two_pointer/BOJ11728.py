import sys
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = [0] * (N + M)
i, j, k = 0, 0, 0
while i < N or j < M:
  if j >= M or (i < N and A[i] < B[j]):
    result[k] = A[i]
    i += 1
  else:
    result[k] = B[j]
    j += 1
  k += 1
    
print(*result)