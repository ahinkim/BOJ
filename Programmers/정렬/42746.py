def solution(numbers):
    def getKey(x):
        x = str(x)
        if len(x) < 4:
            x += x[0 : 4 - len(x)] * 3
        return x
    numbers.sort(key = getKey, reverse = True)
    answer = ''
    for x in numbers:
            answer += str(x)
    # [0, 0, 0]인 경우 "000"으로 나올 수 있으니 예외처리
    answer = str(int(answer))
    return answer