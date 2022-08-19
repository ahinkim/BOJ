a, b = map(int, input().split())
array = []
i = 0
while True:
  i += 1
  for _ in range(i):
    array.append(i)
  if len(array) > 1000:
    break
print(sum(list(array[a - 1:b])))