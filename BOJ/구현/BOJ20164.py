# 최소, 최대 홀수의 개수 찾는 함수
def count_odd(num):
  # 홀수의 개수 세기
  total = list(map(lambda a:int(a)%2, num)).count(1)
  n = len(num)
  # 한자리 수인 경우
  if n == 1:
    return int(num) % 2, int(num) % 2
  # 두자리 수인 경우
  if n == 2:
    while len(num) > 1:
      num = str(int(num[0]) + int(num[1]))
      total += list(map(lambda a:int(a)%2, num)).count(1)
    return total, total
  # 세자리 수 이상인 경우
  max_value = 0
  min_value = int(1e9)
  for i in range(1, n - 1):
    for j in range(i + 1, n):
      total_num = int(num[0:i]) + int(num[i:j]) + int(num[j:])
      total_num = str(total_num)
      odd_count = count_odd(total_num)
      min_value = min(min_value, odd_count[0])
      max_value = max(max_value, odd_count[1])
  return total + min_value, total + max_value

num = str(input())
n = len(num)

print(*count_odd(num)) 
