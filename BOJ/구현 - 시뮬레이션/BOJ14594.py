# 동아리방의 개수
N = int(input())
rooms = [1] * N
# 빅-종빈빌런의 행동 횟수를 나타내는 음이 아닌 정수
M = int(input())
for _ in range(M):
    # 빅-종빈빌런의 행동이 양의 정수 x, y
    x, y = map(int, input().split())
    for i in range(x, y):
        rooms[i] = 0
print(rooms.count(1))