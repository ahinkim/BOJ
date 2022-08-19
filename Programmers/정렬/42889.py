def solution(N, stages):
    array = []
    answer = []
    # 단계별 클리어 하지 못한 사용자 수 저장하는 배열
    fail = [0] * (N + 1)
    # 단계별 클리어 하지 못한 사용자 수 세기
    for i in stages:
        if i > N:
            continue
        fail[i] += 1

    total = len(stages)
    for i in range(1, N + 1):
        # 이 부분 예외처리 안해줘서 틀렸었다. => "스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다."
        if total == 0:
            array.append((0, i))
        else:
            array.append((fail[i] / total, i))
            total -= fail[i]

    array.sort(key = lambda x : (-x[0], x[1]))

    for fail_rate, num in array:
        answer.append(num)
    return answer