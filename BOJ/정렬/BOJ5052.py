import sys
# 전화번호 일관성 있는 지 확인해주는 함수
def check(a, b):
  for i in range(len(a)):
    if a[i] != b[i]:
      # 일관성이 있을 때
      return True
  # 일관성이 없을 때
  return False

input = sys.stdin.readline
# 테스트 케이스의 개수
t = int(input().rstrip())
# 전화번호의 수
for i in range(t):
  n = int(input().rstrip())
  numbers = []
  Flag = False
  for j in range(n):
    numbers.append(input().rstrip())
  # 전화번호 사전순 정렬
  numbers.sort()
  for j in range(n - 1):
    # 전화번호 일관성 확인
    if not check(numbers[j], numbers[j + 1]):
      print("NO")
      Flag = True
      break
  if Flag == False:
    print("YES")