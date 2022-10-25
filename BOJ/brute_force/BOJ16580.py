import sys
from itertools import combinations
from copy import deepcopy
# 알파벳(민호가 원하는 단어 중)이 책 안에 있으면 오리기
# 민호가 원하는 단어의 알파벳도 오리기(단어의 길이가 0일 때 다 찾은 걸 확인하기 위해)
def cut(word, book):
    copy_word = deepcopy(word)
    for alpha in word:
        if alpha in book:
            # book.replace()하면 book가 바뀌는 것이 아니라 replace()된 문자열을 반환한다. 그래서 result = book.replace()필수다.
            book = book.replace(alpha, '', 1)
            copy_word = copy_word.replace(alpha, '', 1)
    return copy_word

input = lambda : sys.stdin.readline().rstrip()
# 민호가 만들고자 하는 단어를 의미하는 문자열 T
T = input()
# 민호가 가진 전공책의 개수를 의미하는 정수 N 
N = int(input())
books = []
for _ in range(N):
    # 전공책 가격을 의미하는 정수 C, 제목을 의미하는 문자열 W
    C, W = input().split()
    books.append([int(C), W])

candidates = []
# 0번책 부터 1번 책까지 선택할 수 있는 조합 구하기
for i in range(1, N+1):
    candidates.extend(list(combinations(range(N), i)))

INF = int(1e9)
min_cost = INF
for candidate in candidates:
    word = T
    cost = 0
    for i in candidate:
        word = cut(word, books[i][1])
        cost += books[i][0]
        if not word: # word가 빈 값인 경우
            break
    if not word:
        min_cost = min(min_cost, cost)

# 민호가 원하는 단어 만들는 가장 적은 비용
if min_cost == INF:
    print(-1)
else:
    print(min_cost)