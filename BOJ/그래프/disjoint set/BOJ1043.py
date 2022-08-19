def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# n : 사람의 수, m : 파티의 수
n, m = map(int, input().split())
# know_truth : 진실을 아는 사람
know_truth = list(map(int, input().split()))[1:] 

parent = [i for i in range(n + 1)]
parties = []

for _ in range(m):
  # 각 파티 참여자 정보 추가
  __input = list(map(int, input().split()))[1:]
  parties.append(__input)
  
  # 파티 참여자끼리 결합
  if len(__input) > 1:
    for x, y in zip(__input[:-1], __input[1:]):
      # 이 부분 잘 기억해두자. 전 코드에서는 안짰는데 안그러면 매우 비효율적으로 union연산만 여러번 하게 된다.
      if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)

parent = [find_parent(parent, i) for i in parent]
know_truth = [find_parent(parent, i) for i in know_truth]

answer = 0
#각 파티에 대하여
for party in parties:
  check = True # 진실을 아는 자가 없다고 가정
  # 파티에 대한 참여자에 대하여
  for x in party:
    # 진실을 아는 자가 존재할 때
    if find_parent(parent, x) in know_truth:
      check = False
      break
  # 진실을 아는자가 파티에 존재하지 않을 때
  if check:
    answer += 1

print(answer)
