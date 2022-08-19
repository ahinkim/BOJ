# 민혁이가 영수의 세 자리 수를 정확하게 맞추어 3 스트라이크가 되면 게임이 끝난다.
import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
data = []
for _ in range(n):
    # 민혁이가 질문한 세 자리수, 영수가 답한 스트라이크 개수, 볼의 개수
    a, b, c = map(int, input().split())
    data.append((a, b, c))

res = 0
for ans in range(123, 988): # 123~987까지 검사(중복되지 않는 범위)
    ans = str(ans) # 영수의 답
    # 하나라도 수가 중복되거나 0이 들어가면 연산하지 않는다.
    if len(set(ans)) != 3 or '0' in ans:
        continue
    check = True
    for q, cts, ctb in data:
        q = str(q) # 민혁이의 질문
        strike = 0 
        ball = 0
        for i in range(3):
            for j in range(3):
                if ans[i] == q[j]:
                    if i == j:
                        strike += 1
                    else:
                        ball += 1
        # strike, ball의 개수가 하나라도 틀리다면 가능성이 없는 답
        if cts != strike or ctb != ball:
            check = False
            break
    if check:
        res += 1
print(res)