def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        prev = s[0:step]
        count = 1
        compressed = ''
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                count = 1
                prev = s[j:j + step]
        
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer