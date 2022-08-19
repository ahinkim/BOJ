import sys
# 괄호열이 올바른 지 검사
def check(s):
  stack = []
  for x in s:
    if x == '(' or x == '[':
      stack.append(x)
    else:
      # 오른쪽 괄호가 왼쪽 괄호보다 먼저 나왔을 때
      if not stack:
        return 0
      # 오른쪽 괄호와 왼쪽 괄호가 같은 지 검사
      left = stack.pop()
      if x == ')':
        if left != '(':
          return 0
      elif x == ']':
        if left != '[':
          return 0
  # 왼쪽 괄호의 수와 오른쪽 괄호의 수가 맞지 않을 때
  if stack:
    return 0
  return 1
# 괄호열의 값 검사
def cal_value(s):
  stack = []
  for x in s:
    if x == '(' or x == '[':
      stack.append(x)
    # x == 오른쪽 괄호일 때
    else:
      left = stack.pop()
      # ()형태 2로 바꿔서 stack에 push
      if x == ')':
        if left == '(':
          stack.append('2')
        # left == 숫자일 때
        else:
          # 왼쪽 괄호가 나올 때까지 괄호안에 있는 숫자 다 더하고 (x)형태니 마지막에 곱하기
          temp = int(left)
          while '0' <= stack[-1] <= '9':
            left = stack.pop()
            temp += int(left)
          stack.pop() # 왼쪽괄호 제거  
          stack.append(str(2 * temp))
      elif x == ']':
        if left == '[':
          stack.append('3')
        # left == 숫자
        else:
          temp = int(left)
          while '0' <= stack[-1] <= '9': 
            left = stack.pop()
            temp += int(left)
          stack.pop()
          stack.append(str(3 * temp))
  return stack

#괄호열 입력
input = sys.stdin.readline
s = input().rstrip() 

check = check(s)
# 괄호열이 올바르지 않을 때
if check == 0:
  print(0)
# 괄호열이 올바를 때 괄호열의 값 검사
else:
  stack = cal_value(s)
  result = 0
  for x in stack:
    result += int(x)
  print(result)
