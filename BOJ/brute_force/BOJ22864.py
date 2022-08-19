A, B, C, M = map(int, input().split())

totalA = 0 # 쌓인 총 피로도
totalB = 0 # 처리한 일의 총량
for _ in range(24):
  totalA += A  
  if totalA <= M:
    totalB += B
  else:
    totalA -= A
    totalA -= C
    if totalA < 0:
      totalA = 0
print(totalB)