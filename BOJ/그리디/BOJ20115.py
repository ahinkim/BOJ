# 에너지 드링크의 수 N
N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

ans = 0
for i in range(N-1):
    ans += drinks[i] / 2
ans += drinks[N-1]
print(ans)