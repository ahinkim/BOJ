def solution(new_id):
    answer =''
    for i in new_id:
        # 1단계
        if i.isupper():
            answer += i.lower()
        # 2단계
        elif i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            answer += i
    # 3단계
    temp = ''
    for i in range(len(answer)-1):
        if not('.' == answer[i] == answer[i+1]):
            temp += answer[i]
    answer = temp + answer[len(answer)-1]
    print(answer)
    # 4단계
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if len(answer) == 0:
        answer += 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    if len(answer) <= 2:
        answer += answer[-1]*(3 - len(answer))
    return answer