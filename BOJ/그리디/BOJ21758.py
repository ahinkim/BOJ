n = int(input())
data = [0]
data.extend(list(map(int, input().split())))
prefix = [0]
sum = 0
for x in data[1:]:
    sum += x
    prefix.append(sum)

ans = 0
# 벌통이 맨 오른쪽에 있고 첫 번째 벌이 맨 왼쪽에 있을 때
# i: 두 번째 벌의 배열 위치
for i in range(2, n):
    # 두 번째 벌이 얻을 수 있는 꿀의 양
    s = prefix[n] - prefix[i]
    # 첫 번째 벌이 얻을 수 있는 꿀의 양: 전체 꿀의 양 중에서 첫 번째 벌 위치의 꿀과 두 번째 벌 위치의 꿀을 제외
    f = prefix[n] - prefix[1] - data[i]
    ans = max(ans, s + f)
# 벌통이 맨 왼쪽에 있고 첫 번째 벌이 맨 오른쪽에 있을 때
for i in range(n - 1, 0, -1):
    s = prefix[i - 1] 
    f = prefix[n - 1] - data[i]
    ans = max(ans, s + f)

# 벌통이 가운데 중 하나에 있고 벌들이 양쪽 끝에 있을 때
res = prefix[n - 1] - prefix[1] + max(data[2:n])
ans = max(ans, res)
print(ans)