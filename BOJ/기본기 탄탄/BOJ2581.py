from math import sqrt
m = int(input())
n = int(input())
num = [True] * (n + 1)
num[0] = False
num[1] = False
for i in range(2, int(sqrt(n)) + 1):
  j = 2
  while i*j <= n:
    num[i * j] = False 
    j += 1

sum_value = 0
min_value = 0 
check = True
for i in range(m, n + 1):
  if num[i]:
    sum_value += i
    if check:
      check = False
      min_value = i
if sum_value == 0:
  print(-1)
else:
  print(sum_value, min_value, sep = "\n")