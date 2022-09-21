def timeToSec(time):
    h, m, s = map(int, time.split(':'))
    return h*60*60 + m*60 + s

def secToTime(sec):
    h = sec//(60*60)
    sec -= h*60*60
    h = "{0:0>2}".format(h)
    m = sec//60
    sec -= m*60
    m = "{0:0>2}".format(m)
    s = "{0:0>2}".format(sec)
    return h+":"+m+":"+s

def solution(play_time, adv_time, logs):
    # 초 당 누적 시청자 수(최대 100시간 = 360000초)
    view_arr = [0] * (timeToSec(play_time) + 1)
    # 기록의 시작점, 끝점 초 단위로 저장 
    for log in logs:
        start, end = log.split('-')
        start_sec = timeToSec(start)
        end_sec = timeToSec(end)
        # 시청자 유입 +1
        view_arr[start_sec] += 1
        # 시청자 빠짐 -=1
        view_arr[end_sec] -= 1

    # 초 당 누적 시청자 수 구 하기
    for i in range(1, len(view_arr)):
        view_arr[i] += view_arr[i-1]

    # 접두사 합 구하기
    prefix_sum = [0]
    total = 0
    for i in range(len(view_arr)):
        total += view_arr[i]
        prefix_sum.append(total)          

    # 초 단위 광고 시간
    adv_time = timeToSec(adv_time)
    # 최대 누적 재생시간 광고 삽입 구간 구하기
    max_time = 0
    answer = 0
    for i in range(len(view_arr)):
        if i+1+adv_time >= len(prefix_sum):
            break
        insert_time = prefix_sum[i+adv_time] - prefix_sum[i]
        if insert_time > max_time:
            max_time = insert_time
            answer = i

    return secToTime(answer)