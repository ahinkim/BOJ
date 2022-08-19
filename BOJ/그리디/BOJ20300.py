N = int(input())
# 운동기구 Fitness equipment
fe = list(map(int, input().split()))

# 운동기구가 홀수개인 경우 짝 맞추기 위해 리스트 맨 앞에 0 추가
if len(fe) % 2 != 0:
    fe = [0] + fe
    N+=1

fe.sort()

max_v = 0
for i in range(N//2):
    max_v = max(max_v, fe[i] + fe[N-1-i])

print(max_v)