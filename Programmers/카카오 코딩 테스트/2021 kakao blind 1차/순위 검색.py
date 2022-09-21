from collections import defaultdict
from bisect import bisect_left, bisect_right
def solution(info, query):
    answer = []
    # 언어
    lang = ['cpp', 'java', 'python', '-']
    # 직군
    job = ['backend', 'frontend', '-']
    # 경력
    career = ['junior', 'senior', '-']
    # 소울푸드
    food = ['chicken', 'pizza', '-']
    # key = 모든 경우의 수(점수 제외한 모든 조건), value = 점수 리스트
    info_dict = defaultdict()
    # 모든 경우의 수에 대한 점수 리스트 구하기
    for l in lang:
        for j in job:
            for c in career:
                for f in food:
                    info_dict[' '.join([l, j, c, f])] = []
        
    # info_dict에 해당하는 key의 값에 점수 추가하기
    for i in info:
        l, j, c, f, s = i.split()
        for k in info_dict.keys():
            k = k.split() # "a b c d" 같은 문자열도 split()으로 나눌 수 있다.        
            if (k[0] == '-' or k[0] == l) and (k[1] == '-' or k[1] == j) and (k[2] == '-' or k[2] == c) and (k[3] == '-' or k[3] == f):
                info_dict[' '.join(k)].append(int(s)) # 이 부분 int로 저장해야 후에 비교 가능하다.
    # info_dict의 값 정렬
    for k, v in info_dict.items():
        info_dict[k].sort() # 문자열로 sort하면 '50' < '150'이다. int로 바꿔서 sort해야 한다.
    # 해당 점수 이상의 값 찾기
    for q in query:
        q = q.replace('and', '')
        q = q.split() #' '든 '  '든 두 개의 문자열 사이에 한 개 이상의 스페이스가 있다면 쪼개준다. ex) a  b => [a, b] a b => [a, b]
        k = ' '.join(q[:-1])
        target = int(q[-1])
        answer.append(len(info_dict[k]) - bisect_left(info_dict[k], target))
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])