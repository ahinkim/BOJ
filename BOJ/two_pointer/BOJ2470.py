n = int(input())
array = list(map(int, input().split())) 
array.sort()

left = 0
right = n - 1
min_value = int(1e10)
result = []

while left < right:
  total = array[left] + array[right]
  if abs(total) < min_value:
    min_value = abs(total)
    result = [array[left], array[right]]

  if total > 0:
    right -= 1
  else:
    left += 1

print(result[0], result[1])
