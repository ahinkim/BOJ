# 부분합과 투포인터의 차이 보기
n = int(input())
array = list(map(int, input().split()))
x = int(input())

start = 0
end = n-1
array.sort()

cnt = 0
for start in range(n):
    while array[start]+array[end] > x and end >= 0:
        end-=1
    if start >= end:
        break
    if array[start]+array[end] == x:
        cnt += 1

print(cnt)