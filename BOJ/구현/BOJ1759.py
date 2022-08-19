from itertools import combinations
# 자음이 2개 이상 모음이 1개 이상이면 True반환
def count(s):
  vowels = ['a', 'e', 'i', 'o', 'u'] 
  vowels_cnt = 0
  consonants_cnt = 0
  for x in s:
    if x in vowels:
      vowels_cnt += 1
    else:
      consonants_cnt += 1
  if vowels_cnt >= 1 and consonants_cnt >= 2:
    return True

L, C = map(int, input().split())

array = list(input().split())
array.sort()
array = list(combinations(array, L))
for s in array:
  if count(s):
    print(''.join(s))