N, S = map(int, input().split())
array = list(map(int, input().split()))
end = 0
cnt = 0
total = 0
min_value = int(1e9)
for start in range(N):
  while total < S and end < N:
    total += array[end]
    end += 1
  if total >= S:
    cnt += 1
    min_value = min(min_value, end - start)
  total -= array[start]

if cnt == 0:
  print(0)
else:
  print(min_value)