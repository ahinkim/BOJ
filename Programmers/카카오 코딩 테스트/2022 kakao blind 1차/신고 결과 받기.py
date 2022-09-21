def solution(id_list, report, k):
    # 동일한 유저에 대한 신고 횟수는 1회로 처리되기 때문에 중복 제거
    report = set(report)
    # id_list 순서대로 신고 당한 수 저장할 사전
    reported_dict = {people:0 for people in id_list}
    # 유저별 신고한 id 저장
    report_dict = {people:[] for people in id_list}
    # 신고 당한 개수 세기
    for x in report:
        reporter, respondent = x.split()
        reported_dict[respondent] += 1
        report_dict[reporter].append(respondent)
    
    answer = []
    for reporter, respondents in report_dict.items():
        cnt = 0
        for respondent in respondents:
            # k번 이상 신고당한 경우
            if reported_dict[respondent] >= k:
                cnt += 1
        answer.append(cnt)
    return answer