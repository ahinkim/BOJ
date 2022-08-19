n = int(input())
array = []
INF = int(1e9)
for _ in range(n):
  data = list(map(int, input().split()))
  for i in range(len(data)):
    if data[i] == 0:
      data[i] = INF
  array.append(data)

for k in range(n):
  for a in range(n):
    for b in range(n):
      array[a][b] = min(array[a][b], array[a][k] + array[k][b])

for i in range(n):
  for j in range(n):
    if array[i][j] != INF:
      print(1, end =' ')
    else:
      print(0, end = ' ')
  print()