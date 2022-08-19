# 백트래킹
def back(depth, result, data):
  if depth == M:
    print(*result)
    return
  for x in data:
    new = data.replace(x, '')
    back(depth + 1, result + x, new)
  
N, M = map(int, input().split())
data = ""
for i in range(1, N + 1):
  data += str(i)
  
back(0, "", data)