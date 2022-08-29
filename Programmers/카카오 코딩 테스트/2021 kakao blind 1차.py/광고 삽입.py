# 시간복잡도 넘기지 않으니 완탐으로 구현
from time import gmtime
from time import strftime
def solution(play_time, adv_time, logs):
    answer = ''
    # 초 단위로 저장한 logs
    logs_arr = []
    # 기록의 시작점, 끝점 저장 
    for log in logs:
        start, end = log.split('-')
        h, m, s = map(int, start.split(':'))
        start_sec = h*60*60 + m*60 + s
        h, m, s = map(int, end.split(':'))
        end_sec = h*60*60 + m*60 + s
        logs_arr.append((start_sec, end_sec))
    # play_time의 전체 초 단위 시간
    h, m, s = map(int, play_time.split(':'))
    play_secs = h*60*60 + m*60 + s
    # adv_time의 전체 초 단위 시간
    h, m, s = map(int, adv_time.split(':'))
    adv_secs = h*60*60 + m*60 + s
    # 기록의 시작점이나 끝점이 광고 삽입할 구간안에 들어가면 들어가는 기록의 합 구해서 max값 찾기
    max_v = -1
    for i in range(play_secs + 1 - adv_secs):
        total = 0
        for s, e in logs_arr:
            # 시작점과 끝점이 삽입할 구간 안에 있다면
            if i <= s <= i+adv_secs and i <= e <= i+adv_secs:
                total += e-s
            # 시작점이 삽입할 구간 안에 있다면
            elif i <= s <= i+adv_secs:
                # 구간의 끝 - 시작점
                total += i+adv_secs - s
            # 끝점이 삽입할 구간 안에 있다면
            elif i <= e <= i+adv_secs:
                # 끝점 - 구간의 시작
                total += e - i
            if i == 3600:
                print(s, e, i, i+adv_secs)
        if max_v < total:
            max_v = total
            answer = i
    return strftime("%H:%M:%S", gmtime(answer))