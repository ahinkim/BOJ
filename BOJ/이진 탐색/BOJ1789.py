s = int(input())
start = 1
end = s // 2 + 1

while start <= end:
  mid = (start + end) // 2
  sum_value = 0
  for i in range(1, mid + 1):
    sum_value += i
  if sum_value == s:
    result = mid
    break
  elif sum_value > s:
    # 1 2 3 4 5 6 더해서 20을 찾고 있는데 6까지 더하면 21이 나온다 근데 21은 21 - 1 = 20이니까 하나만 빼면 된다. 이런식으로 딱 하나 더 초과되는 경우 해당되는 수 n에서 1, 2, 3..., n - 1 중에 하나만 빼도 원하는 값이 나올테니 최댓값 - 1을 해주면 된다.
    end = mid - 1
    result = mid - 1
  else:
    start = mid + 1

print(result)
