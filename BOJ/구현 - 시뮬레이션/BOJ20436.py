# 문자의 키보드 위치 찾기
def find_loc(s):
    i, j = 0, 0 
    for x in keyboard:
        j = 0 
        for y in x:
            if y == s:
                return i, j
            j += 1
        i += 1

keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
# 모음
vowel = 'yuiophjklbnm'
l, r = input().split()
# 출력 데이터
data = input()
# l의 위치
xl, yl = find_loc(l)
# r의 위치
xr, yr = find_loc(r)

# 문자열 출력하는 시간의 최솟값 구하기
ans = 0
for x in data:
    if x in vowel:
        xf, yf = find_loc(x)
        ans += abs(xr-xf) + abs(yr-yf)
        xr, yr = xf, yf
    else:
        xf, yf = find_loc(x)
        ans += abs(xl-xf) + abs(yl-yf)
        xl, yl = xf, yf
    ans += 1
print(ans)