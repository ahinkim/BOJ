import sys
sys.setrecursionlimit(10**6)
def solutions(stack):
  temp = []
  result = [0] * (N)
  while stack:
    h, i = stack.pop()
    if not stack:
      break
    if h < stack[-1][0]:
      result[i] = len(stack) 
      while temp:
        if temp[-1][0] < stack[-1][0]:
          h, i = temp.pop()
          result[i] = len(stack) 
        else:
          break
    else:
      temp.append((h, i))
  return result
    
N = int(input())
data = list(map(int, input().split()))
stack = []
i = 0
for h in data:
  # 탑의 높이와 번호
  stack.append((h, i))
  i += 1

print(*solutions(stack))