N = int(input())

array = []
for _ in range(N):
  array.append(input())

array = list(set(array))
array.sort(key = lambda x : (len(x), x))
# 사전 내림차순 하는 방법
# array.sort(key = lambda x : (-len(x), x), reverse = True)
for x in array:
  print(x)