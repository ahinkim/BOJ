from collections import defaultdict
import math
# 총 시간을 분으로 바꾸기
def timeToMinute(time):
    h, m = time.split(':')
    return int(h)*60+int(m)

def solution(fees, records):
    # key: 차량번호, value: 입차 시간
    in_dict = defaultdict(int)
    # 누적 주차 시간
    time_dict = defaultdict(int)
    # 차량 번호별 요금
    fee_dict = defaultdict(int)
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    default_time, default_fee, unit_time, unit_fee = fees
    # 누적 주차 시간 구하기
    for record in records:
        time, num, direction = record.split()
        if direction == 'IN':
            in_dict[num] = timeToMinute(time)
        else:
            diff = timeToMinute(time) - in_dict[num]
            time_dict[num] += diff
            del in_dict[num]  
    # in_dict에 남은 차량 번호들 23:59 기준으로 누적 주차 시간 구하기
    for num, time in in_dict.items():
        diff = 1439 - time
        time_dict[num] += diff

    # 요금 계산하기
    for num, time in time_dict.items():
        diff = time-default_time
        if time-default_time < 0:
            diff = 0  
        print(default_fee, diff, unit_time, unit_fee)
        print(default_fee + (diff/unit_time) * unit_fee )
        fee_dict[num] += default_fee + math.ceil(diff/unit_time) * unit_fee 
    answer = [x[1] for x in sorted(fee_dict.items())] # 차량번호 int로 정렬?
    return answer