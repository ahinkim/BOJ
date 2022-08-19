import math
n = int(input())
array = []
array = list(map(int, input().split()))
cnt = 0
for x in array:
  check = False
  if x == 1:
    continue
  # 제곱근까지만 풀어도 된다는 사실 잘 기억하자
  for i in range(2, int(math.sqrt(x)) + 1): #sqrt: square root
    if x % i == 0:
      check = True
  if check == False:
    cnt += 1
print(cnt)