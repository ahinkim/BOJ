T = int(input())
for t in range(T):
    N = int(input())
    salePriceList = list(map(int, input().split()))
    f = salePriceList[N-1]
    res = 0
    # 현재 기준값보다 큰 값이 나올 때까지 기준값 - 현재값 저장
    for i in range(N-1, -1, -1):
        # 기준값보다 더 큰 값 나오면 기준값을 더 큰 값으로 바꾸기
        if f < salePriceList[i]:
            f = salePriceList[i]
        else:
            res += f - salePriceList[i]
    print('#' + str(t+1) + ' ' + str(res))