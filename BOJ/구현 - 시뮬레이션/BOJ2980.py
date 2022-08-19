# 신호등의 개수 N, 도로의 길이 L
N, L = map(int, input().split())

total = 0
prev = 0
for _ in range(N):
    # 신호등의 정보: 신호등의 위치 D, 빨간색, 초록색이 지속되는 시간 R, G
    D, R, G = map(int, input().split())
    # 신호등까지 이동 시간 더하기
    total += D - prev
    # 현재시간까지의 빨간불, 초록불 주기가 돈 시간 빼기
    r = total - (total // (R+G)) * (R+G)
    # 주기를 빼고 남은 시간이 빨간색 지속시간보다 작다면 현재 빨간 불 크다면 초록불
    if r <= R:
        # 대기시간 더하기
        total += R-r
    prev = D

print(total + L-D)