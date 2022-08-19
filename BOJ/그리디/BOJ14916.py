import sys
input = sys.stdin.readline
# 홀수 + 홀수를 더했을 때 무조건 짝수라는 개념을 생각해서 풀면 for문을 쓰지 않고 풀 수 있다.
n = int(input())
result = 0

# 5미만인 수 빼고는 다 5와 2로 거스름돈을 만들 수 있다. 왜냐하면 5이상의 모든 수가 홀수(5 + 짝수) 형태이거나 짝수 형태 둘 중 하나기 때문이다.
if n < 5:
  if n % 2 == 0:
    result = n // 2
  else:
    result = -1
else:
  ct, n = divmod(n, 5) # 몫과 나머지를 반환하는 함수
  if n == 0:
    result = ct
  else:
    # n이 짝수일 때
    if n % 2 == 0:
      ct += n // 2
      result = ct
    # n이 홀수일 때
    else:
      ct += (n + 5) // 2 - 1 # n + 5는 무조건 짝수 왜냐하면 홀수 + 홀수이기 때문
      result = ct
  
print(result)





# 원래 작성했던 코드: 비효율적
# n = int(input())
# count = n // 5
# check = False
# for i in range(count, -1, -1):
#   if (n - 5 * i) % 2 == 0:
#     check = True
#     break

# if check == False:
#   print(-1)
# else:
#   print(i + (n - 5 * i) // 2)
