def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1]) # 진출 지점 기준으로 오름차순 정렬
    camera = -30001
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
    