# for문 중간에 i값 절대 못바꾼다
# n = 1
# for i in range(n,4):
#   print(i)
#   n += 1 # 아무 영향 x
#   i += 1 # 아무 영향 x
# 이런식으로 하고싶으면 while문 써야 한다. 
# 처음에 완전탐색으로 풀어서 틀렸다. 완전탐색으로는 구현이 어렵다는 것을 미리 파악해야 한다. 그 다음에 다이나믹 프로그래밍으로 접근해야 한다. n의 수가 적다고 무조건 완전탐색으로 구현이 가능하다고 생각하지 말자
n = int(input())
T = [0] * (n + 1)
P = [0] * (n + 1)
array = [0] * (n + 1)
for i in range(1, n + 1):
  t, p = map(int, input().split())
  T[i] = t
  P[i] = p

for i in range(n, 0, -1):
  if i + T[i] - 1 <= n:
    array[i] = P[i]
    if i + T[i] <= n:
      array[i] += array[i + T[i]]
  #아래 if의 위치를 tap한 번 더한 위치에 놔서 T가 10 1 1 인 경우가 히든케이스가 되었었다. 내 머리에 생각한 것이 코드로 그대로 잘 반영되었는 지 확인하고 히든케이스가 생각안나면 이것저것 데이터를 입력해보는 것도 방법이 될 수 있다.
  if i + 1 <= n:
    array[i] = max(array[i], array[i + 1])

print(array[1])
  