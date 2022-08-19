from collections import defaultdict
def solution(s):
    answer = ''
    N = len(s)
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_dict = defaultdict(str)
    for i in range(len(nums)):
        num_dict[nums[i]] = str(i)
    
    # 문자열 돌기
    i = 0
    while i < N:
        if s[i].isdigit():
            answer += s[i]
            i += 1
            continue
        # 3 4 5 돌기
        for j in range(3, 6):
            if i + j > N:
                break
            search = s[i:i+j]
            if num_dict[search]:
                answer += num_dict[search]
                i = i+j
                break
        
    return int(answer)