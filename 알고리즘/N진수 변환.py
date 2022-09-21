# N을 n진수 => m진수로 변환하는 함수
def convertNum(N, n, m):
    i=0
    # 10진수
    M = 0
    # n진수를 10진수로 바꾸기
    while N > 0:
        N, mod = divmod(N, 10)
        M += mod * n**i
        i+=1
    res = ''
    # 10진수를 m진수로 변환
    while M > 0:
        M, mod = divmod(M, m)
        res += str(mod)
    # 역순인 진수 뒤집어 주기(문자열은 아래와 같이 뒤집어야 함 reverse같은 내장함수 문자열에 존재하지 x)
    return res[::-1]



# 10진수 n을\ → m 진수 
def convertNum(n, m):
    res = ''
    while n > 0:
        n, mod = divmod(n, m)
        res += str(mod)
    return res[::-1]