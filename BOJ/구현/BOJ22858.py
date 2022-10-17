import sys
input = lambda : sys.stdin.readline().rstrip()
# 카드의 개수 N, 카드를 섞은 횟수 K
N, K = map(int, input().split())
# K번 카드를 섞은 후 카드의 배치를 의미하는 S
S = list(map(int, input().split()))
# N개의 D
D = list(map(int, input().split())) 

for _ in range(K):
    temp = [-1] * N
    for i in range(N):
        temp[D[i]-1] = S[i]
    S = temp

print(*S, sep = ' ')