# 관찰 횟수
N = int(input())
location = [-1] * 11
ans = 0
for _ in range(N):
    # 소의 번호, 위치
    m, l = map(int, input().split())
    if location[m] != -1 and location[m] != l:
        ans += 1
    location[m] = l
print(ans)