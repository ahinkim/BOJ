import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    note1 = dict()
    # 수첩 1’에 적어 놓은 정수의 개수 N
    N = int(input())
    data = list(map(int, input().split()))
    for x in data:
        note1[x] = 1
    #  ‘수첩 2’에 적어 놓은 정수의 개수 M
    M = int(input())
    note2 = list(map(int, input().split()))

    for num in note2:
        print(note1.get(num, 0))