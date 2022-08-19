import sys
input = lambda : sys.stdin.readline().rstrip()
# 수열 길이 N, 삭제할 수 있는 최대 횟수 K
N, K = map(int, input().split())
# prefix와 순서 맞추기 위함
array = [0]
array.extend(list(map(int, input().split())))
# 부분합
prefix = [0]*(N+1)
cnt = 0
for i in range(1, N+1):
    if array[i] % 2 != 0:
        cnt += 1
    prefix[i] = cnt 
    
end = 1
max_length = 0
for start in range(1, N+1):
    while end <= N and prefix[end] - prefix[start-1] <= K:
        # 전체길이에서 홀수 개수 뺀 값과 비교해서 짝수 최대길이 저장
        max_length = max(max_length, end - start + 1 - (prefix[end] - prefix[start-1]))
        end += 1

print(max_length)