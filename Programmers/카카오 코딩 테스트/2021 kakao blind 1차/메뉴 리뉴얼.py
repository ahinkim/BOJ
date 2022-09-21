from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    # course 개수에 따라 조합 구해서 사전에 저장
    for i in course:
        # 가능한 단품메뉴 조합, 개수 저장
        candidate = []
        for order in orders:
            candidate.extend(list(combinations(sorted(order), i)))
        most_ordered = Counter(candidate).most_common()
        answer.extend([k for k, v in most_ordered if v >= 2 and v == most_ordered[0][1]])
    
    
    return [ ''.join(v) for v in sorted(answer) ]