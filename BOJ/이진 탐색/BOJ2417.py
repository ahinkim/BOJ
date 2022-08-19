import math
# math.ceil 올림, math.floor 내림, round(x, 1) 소수점 첫째짜리까지 반올림
n = int(input())
ans = math.ceil(math.sqrt(n))
if ans**2 >= n:
    print(ans)
else:
    print(ans + 1)