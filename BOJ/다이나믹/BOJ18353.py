n = int(input())
array = list(map(int, input().split()))
solidiers = [1] * n
for i in range(n):
  for j in range(i - 1, -1, -1):
    if array[i] < array[j]:
      solidiers[i] = max(solidiers[i], solidiers[j] + 1)
print(n - max(solidiers))