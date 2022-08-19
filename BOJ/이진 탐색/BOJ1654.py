import sys
# 랜선의 최대 길이 찾기
def binary(start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        # 랜선의 총 개수
        cnt = 0
        for c in cables:
            if c < mid:
                continue
            cnt += c//mid
        if cnt >= N:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

input = lambda : sys.stdin.readline().rstrip()
# 오영식이 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N
K, N = map(int, input().split())
# 랜선
cables = []
for _ in range(K):
    cables.append(int(input()))

cables.sort()
# 랜선의 길이: 1 ~ 2**31-1
ans = binary(1, 2**31-1)

print(ans)