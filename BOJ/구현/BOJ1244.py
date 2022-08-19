def change(switches, sex, k):
  # 남학생일 때
  if sex == 1:
    for i in range(k, N + 1, k):
      if switches[i] == 1:
        switches[i] = 0
      else:
        switches[i] = 1 
  # 여학생일 때
  else:
    d = 0
    for i in range(1, N + 1):
      # 인덱스값 변경하고 이 부분 수정 안해줘서 틀렸었다.
      if k - i < 1 or k + i > N:
        break
      if switches[k - i] == switches[k + i]:
        d = i
      # else부분 쓰지 않아서 히든 케이스 처리 안됐었다.
      else:
        break
    for i in range(k - d, k + d + 1):
      if switches[i] == 1:
        switches[i] = 0
      else:
        switches[i] = 1
        
# 스위치의 개수
N = int(input())
# 인덱스에 맞게 리스트 만들기 위해
switches = [0]
# 스위치의 상태
data = list(map(int, input().split()))
switches.extend(data) # switches = switches.extend(data) 했더니 계속 에러났다. extend는 리스트를 반환하는 함수가 아니다.
# 학생의 수
M = int(input())

for _ in range(M):
  # 성별, 학생이 받은 수
  sex, k = map(int, input().split()) # map(int, input())이라고만 썼다. 조심하자.
  # 스위치 상태 변경 
  change(switches, sex, k)

for i in range(1, N + 1):
  print(switches[i], end = " ")
  # 이 부분 예외처리 깜박하고 안해줬다. 문제 읽고 주석 잘 쓰고 풀자.
  if i % 20 == 0:
    print()