import sys
board = sys.stdin.readline().rstrip()
board = board.replace("XXXX", "AAAA") # 무조건 board = 이런식으로 대입해줘야 한다. replace는 값을 반환해주지만 board안의 값까지 바꿔주지는 않는다.
board = board.replace("XX", "BB")

if 'X' in board:
  print("-1")
else:
  print(board)