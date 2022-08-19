# 오리들의 전체 소리
sound = input()

order = {"q": 0, "u": 1, "a": 2, "c":3, "k": 4}
# 오리들 각각 소리 저장
ducks = []
ans = 0
for x in sound:
    new_sound = True
    # 현재 소리 순서
    now = order[x]
    for i in range(len(ducks)):
        # 마지막 소리가 현재 소리 이전에 나오는 소리일 때 
        if order[ducks[i][-1]] % 5 == (now-1) % 5:
            ducks[i] = ducks[i] + x
            new_sound = False
            break
    # 새로 나온 오리 소리일 때 
    if new_sound:
        if x == 'q':
            ducks.append(x)
        else: # 순서에 맞지 않게 오리소리가 나왔을 때 
            ans = -1

if ans!= -1:
    for d in ducks:
        if len(d) % 5 == 0:
            ans += 1
        else:
            ans = -1
            break

print(ans)