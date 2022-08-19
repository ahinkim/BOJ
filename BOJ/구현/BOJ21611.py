import sys
# 구슬을 빈칸을 없애고 이동시켜주는 함수
def moveballs(balls):
  newballs = []
  for ball in balls:
    if ball != -1 and ball != 0:
      newballs.append(ball)
  return newballs
# 구슬 폭발 함수: 폭발했는 지 여부와 폭발한 구슬의 개수 곱한 값의 total을 return
def explosion(balls):
  total = 0 #구슬의 개수 번호대로 곱한 값의 total
  cnt = 1
  i = 0
  check = False # 폭발 여부
  while i < len(balls):
    if i == len(balls) - 1:
      if cnt >= 4:
        total += cnt * balls[i]   
        balls[i - cnt + 1:i + 1] = [-1] * cnt # 특정 범위 인덱스 한 번에 바꾸는 문법
        check = True
      break
    if balls[i] != balls[i + 1]:
      if cnt >= 4:
        total += cnt * balls[i]
        balls[i - cnt + 1:i + 1] = [-1] * cnt # del ball[a:b + 1] a ~ b 이거와 마찬가지
        check = True
      cnt = 1
    else:
      cnt += 1
    i += 1
  balls = moveballs(balls) # 여기서 balls의 값이 바뀌지 않는다. 또 다른 리스트를 참조하는 것일 뿐 인자로 온 balls가 참조하는 것이랑 다르다. 그래서 return을 해줘야 한다.
  return balls, check, total 
# 구슬 파괴 함수
def destruction(balls, d, s, dx, dy):
  # 상어의 위치
  x, y = (n - 1) // 2, (n - 1) // 2 
  for _ in range(s):
    x += dx[d]
    y += dy[d]
    # 얼음 파편을 던졌을 때 구슬이 있는 지 확인
    # grid_num[x][y] - 1 이 조건을 처음에 걸었다가 코드 바꾸면서 빼버려서 런타임에러났다. 항상 조건을 잘 생각하고 인덱스 범위 넘지 않게 조심하자
    if grid_num[x][y] - 1 < len(balls) and balls[grid_num[x][y] - 1] != 0:
      # 구슬이 있다면 없애기
      balls[grid_num[x][y] - 1] = -1
  balls = moveballs(balls)
  return balls
# 구슬 변화 함수
def change(balls):
  newballs = []
  cnt = 1
  for i in range(len(balls)):
    if len(newballs) >= n * n - 1:
      break
    if i == len(balls) - 1:
      newballs.append(cnt)
      newballs.append(balls[i])
      break
    if balls[i] != balls[i + 1]:
      newballs.append(cnt)
      newballs.append(balls[i])
      cnt = 1
    else: 
      cnt += 1
  return newballs


input = sys.stdin.readline
n, m = map(int, input().split())
grid = [] # 구슬번호가 있는 격자
grid_num = [[0] * n for _ in range(n)] # 칸의 번호가 있는 격자
balls = []# 구슬 순서 리스트
for _ in range(n):
  data = list(map(int, input().split()))
  grid.append(data)
i, j = 0, -1
num = n**2  
# 48, 47... 1 순서대로 달팽이 모양으로 점점 작아지면서 insert
num_dx = [0, 1, 0, -1]
num_dy = [1, 0, -1, 0]
cnt = 0
while True:
  ni, nj = i + num_dx[cnt % 4], j + num_dy[cnt % 4] #nexti, nextj
  if 0 <= ni < n and 0 <= nj < n and grid_num[ni][nj] == 0:
    i = ni
    j = nj
    num -= 1
    # 구슬 삽입이 머리부터가 아닌 꼬리부터 들어간다. (그래서 따로 아래에서 reverse연산)
    balls.append(grid[i][j])
    grid_num[i][j] = num
    if num == 1:
      break
  else:
    ni = i
    nj = j
    cnt += 1

balls.reverse() #구슬의 순서를 뒤집는다.

# 마법의 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total = 0

for _ in range(m):
  # 뱡향, 거리
  d, s = map(int, input().split()) 
  d -= 1 # 인덱스 0, 1, 2, 3에 맞추기 위함
  # 구슬 파괴
  balls = destruction(balls, d, s, dx, dy)
  #구슬 폭발
  check = True
  while check != False:
    check = False
    balls, check, subtotal = explosion(balls) 
    total += subtotal
  
  # 구슬 변화
  balls = change(balls)
      
print(total)
