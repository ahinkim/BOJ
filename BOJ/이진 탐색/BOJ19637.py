import sys
def binary(start, end, target):
    res = 0
    while start <= end:
        mid = (start + end)//2
        if target <= powers[mid][0]:
            res = powers[mid][1]
            end = mid - 1
        else:
            start = mid + 1
    return res

input = lambda : sys.stdin.readline().rstrip()
# 칭호의 개수 N, 칭호를 출력해야 하는 캐릭터들의 개수 M
N, M = map(int, input().split())
powers = []
for _ in range(N):
    # 각 칭호, 해당 칭호의 전투력 상한값
    name, limit = input().split()
    powers.append((int(limit), name))

for _ in range(M):
    print(binary(0, N, int(input())))