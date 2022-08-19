import sys
from collections import defaultdict
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
likedict = defaultdict(list)
for _ in range(n**2):
  _input = list(map(int, input().split()))
  likedict[_input[0]] = _input[1:]

classroom = [[-1] * (n + 1) for _ in range(n + 1)]

#처음에 k, v라고 했는데 아래 for k i range랑 겹쳐서 잘못된 값 나왔다. 변수 중복해서 쓰는 거 주의하자
for key, value in likedict.items(): # likedict라고만 하면 안되고 .items()붙여야 한다.
  maxrow = 0
  maxcol = 0
  maxlike = -1
  maxempty = -1 
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if classroom[i][j] == -1:
        likecnt = 0
        emptycnt = 0
        for k in range(4):
          nrow = i + dx[k]
          ncol = j + dy[k]
          if nrow < 1 or nrow > n or ncol < 1 or ncol > n:
            continue
          if classroom[nrow][ncol] in value:
            likecnt += 1
          if classroom[nrow][ncol] == -1:
            emptycnt += 1
        if maxlike < likecnt or (maxlike == likecnt and maxempty < emptycnt):
          maxlike = likecnt
          maxempty = emptycnt
          maxrow = i
          maxcol = j
  classroom[maxrow][maxcol] = key

total = 0
for i in range(1, n + 1):
  for j in range(1, n + 1):
    likecnt = 0
    for k in range(4):
      nrow = i + dx[k]
      ncol = j + dy[k]
      if nrow < 1 or nrow > n or ncol < 1 or ncol > n:
        continue
      if classroom[nrow][ncol] in likedict[classroom[i][j]]:
        likecnt += 1
    if likecnt > 0:
      total += 10**(likecnt - 1)

print(total)


