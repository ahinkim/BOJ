for k in range(10):
    N = int(input())
    building = list(map(int, input().split()))
    res = 0
    for i in range(2, N-2):
        h = building[i]
        max_h = max(building[i-2], building[i-1], building[i+1], building[i+2])
        if max_h < h:
            res += h-max_h

    print(f'#{k+1} {res}')