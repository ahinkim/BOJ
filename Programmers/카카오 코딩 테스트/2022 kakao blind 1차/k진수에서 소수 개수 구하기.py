import math
# n을 m진수로 변환하는 함수
def convertNum(n, m):
    res = ''
    while n > 0:
        n, mod = divmod(n, m)
        res += str(mod)
    return res[::-1]

# 소수인지 확인하는 함수
def is_prime_number(x) :
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    n = convertNum(n, k) + '0'
    print(n)
    nums = ''
    N = len(n)
    # 조건 모두 오른쪽에 0이 나왔을 때 식별하면 된다
    for i in range(N):
        if nums != '' and (n[i] == '0' or i==N-1):
            if is_prime_number(int(nums)):
                answer += 1
                print(nums)
            nums = ''
        else:
            nums += str(n[i])
    return answer