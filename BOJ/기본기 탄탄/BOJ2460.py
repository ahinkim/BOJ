total = 0
max_value = 0
for i in range(10):
  getoff, geton = map(int, input().split())
  total += geton
  total -= getoff
  if total > max_value:
    max_value = total

print(max_value)