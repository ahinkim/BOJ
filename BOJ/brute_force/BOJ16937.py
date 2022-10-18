import sys
input = lambda : sys.stdin.readline().rstrip()
# 모눈 종이의 크기
H, W = map(int, input().split())
graph = [[0] * W for _ in range(H)]
# 스티커의 수
N = int(input())
stickers = [list(map(int, input().split())) for _ in range(N)]

res = 0
for i in range(N):
    for j in range(i+1, N):
        r1, c1 = stickers[i]
        r2, c2 = stickers[j]
        # stk1, stk2 그대로인 경우
        if r1+r2 <= H and max(c1, c2) <= W or c1+c2 <= W and max(r1, r2) <= H: 
            res = max(res, r1*c1 + r2*c2)
        # stk1만 90도 회전하는 경우(r1 <-> c1)
        elif c1+r2 <= H and max(r1, c2) <= W or r1+c2 <= W and max(c1, r2) <= H: 
            res = max(res, r1*c1 + r2*c2)
        # stk2만 90도 회전하는 경우(r2 <-> c2)
        elif r1+c2 <= H and max(c1, r2) <= W or c1+r2 <= W and max(r1, c2) <= H: 
            res = max(res, r1*c1 + r2*c2)
        # 둘 다 90도 회전하는 경우(r1 <-> c1, r2 <-> c2)
        elif c1+c2 <= H and max(r1, r2) <= W or r1+r2 <= W and max(c1, c2) <= H: 
            res = max(res, r1*c1 + r2*c2)

# 두 스티커가 붙여진 넓이의 최댓값
print(res)