from itertools import permutations
from copy import deepcopy
# 왼쪽에서부터 차례대로 연산해주는 함수
def operation(operand, operator):
  copy_operator = list(operator)
  copy_operand = deepcopy(operand) 
  # 하나 남을 때까지 돌기
  while len(copy_operand) > 1:
    a = copy_operand.pop()
    b = copy_operand.pop()
    x = copy_operator.pop()
    copy_operand.append(int(eval(str(a)+x+str(b))))
  return copy_operand.pop()
  
# 수의 개수
n = int(input()) 
# n개의 수로 이루어진 수열
operand = list(map(int, input().split()))
# 연산자의 개수: + - * // 순서
operator_cnt = list(map(int, input().split())) 
# 연산자
operator = ['+', '-', '*', '/'] 
# 순열 후보자
candidate = []

for i in range(4):
  for j in range(operator_cnt[i]): 
    candidate.append(operator[i])
candidate = list(permutations(candidate, n - 1))
candidate = list(set(candidate))
min_value = int(1e10)
max_value = -int(1e10)
operand.reverse()
for oper in candidate:
  result = operation(operand, oper)
  min_value = min(min_value, result)
  max_value = max(max_value, result)

print(max_value, min_value, sep = '\n')
