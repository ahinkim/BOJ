import math
def is_prime_number(x) :
    # if x == 1: 예외처리 해줘야 할 수도 있다.
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True