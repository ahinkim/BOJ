# 스타벅스에 서 있는 사람의 수 N
N = int(input())
tip = []
for _ in range(N):
    tip.append(int(input()))
tip.sort()
i = 0
ans = 0
while True:
    v = tip.pop() - i
    if v >= 0:
        ans += v
    i += 1
    if i == N:
        break

print(ans)