n = int(input())
array = list(map(int, input().split()))
max_value = array[0]
min_value = array[0]
for x in array:
  if max_value < x:
    max_value = x
  if min_value > x:
    min_value = x
print(min_value, max_value) 