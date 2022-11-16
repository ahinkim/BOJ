from copy import deepcopy
def back_tracking(nums, idx, cnt):
    global N
    global res
    if idx == N or cnt == 0:
        if cnt  % 2 == 0:
            res = max(res, int(''.join(nums)))
        else:
            nums[N-1], nums[N-2] = nums[N-2], nums[N-1]
            res = max(res, int(''.join(nums)))
        return

    # 바꾸지 않는 경우
    new_nums = deepcopy(nums)
    back_tracking(new_nums, idx+1, cnt)
    # 바꾸는 경우
    for i in range(N):
        # 자기 자신과 바꾸는 것 제외
        if i == idx:
            continue
        new_nums = deepcopy(nums)
        new_nums[i], new_nums[idx] = new_nums[idx], new_nums[i]
        back_tracking(new_nums, idx+1, cnt-1)

T = int(input())
N = 0
res = 0
for k in range(T):
    nums, cnt = map(int, input().split())
    nums = list(str(nums))
    N = len(nums)
    res = 0
    back_tracking(nums, 0, cnt)
    print(f'#{k+1} {res}')