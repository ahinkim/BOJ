N = int(input())

# 알파벳 전체 개수: 52개
graph = [[False] * 52 for _ in range(52)]
# 명제의 개수
cnt = 0
for _ in range(N):
  x, oper, y = input().split()
  # isUpper이 아니라 isupper이다.
  # 대문자면 0 - 25
  if x.isupper():
    x = ord(x) - ord('A')
  # 소문자면 26 - 51
  else:
    x = ord(x) - ord('a') + 26
  if y.isupper():
    y = ord(y) - ord('A')
  else:
    y = ord(y) - ord('a') + 26
  if x != y and graph[x][y] != True:
    cnt += 1
    graph[x][y] = True

for k in range(52):
  for a in range(52):
    for b in range(52):
      if a != b and graph[a][b] != True:
        graph[a][b] = graph[a][k] and graph[k][b]
        if graph[a][b] == True:
          cnt += 1

print(cnt)
for i in range(52):
  for j in range(52):
    if graph[i][j] == True:
      # x가 소문자
      if i >= 26:
        print(chr(ord('a') + i - 26), "=>", end = " ")
      # x가 대문자면 
      else:
        print(chr(ord('A') + i), "=>", end = " ")

      if j >= 26:
        print(chr(ord('a') + j - 26))
      else:
        print(chr(ord('A') + j))