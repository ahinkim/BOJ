def binary_search(array, start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return 1
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  
  return 0

# 상근이가 가지고 있는 숫자 카드의 개수
N = int(input())
# 상근이의 숫자 카드
card = list(map(int, input().split()))
# query 개수
M = int(input())
# query할 카드
array = list(map(int, input().split()))
card.sort() 
for x in array:
  print(binary_search(card, 0, N - 1, x), end = " ")

