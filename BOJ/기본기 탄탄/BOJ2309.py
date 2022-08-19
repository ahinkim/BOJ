from itertools import combinations
array = [int(input()) for _ in range(9)]
array = list(combinations(array, 7))

for x in array:
  if sum(x) == 100:
    x = list(x)
    x.sort()
    for y in x:
      print(y)
    break
