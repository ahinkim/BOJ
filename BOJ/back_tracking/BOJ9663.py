def is_promising(row):
  # 같은 열 상단에 퀸이 놓여 있을 때 or 대각선 상단에 퀸이 놓여있을 때 
  for i in range(row - 1, -1, -1):
    if col[row] == col[i] or (abs(col[row] - col[i]) == abs(row - i)):
      return False
  return True

def n_queen(row):
  global ans
  # N - 1행까지 퀸을 다 놓았을 때
  if row == N:
    ans += 1
    return
  # 열 검사
  for i in range(N):
    # 배열은 어디에서나 참조 가능하고 값 변경 가능, 변수는 어디서나 참조 가능하지만 값 변경은 global로 선언해줘야 가능
    col[row] = i
    # 이 경우가 유망할 때
    if is_promising(row):
      n_queen(row + 1)

N = int(input())
col = [0] * N
ans = 0

n_queen(0)  
print(ans)