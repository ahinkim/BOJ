# DNA의 수 N, 문자열의 길이 M
N, M = map(int, input().split())
dna_arr = [input() for _ in range(N)]

# Hamming Distance의 합
hd_total = 0

for i in range(M):
    hd_dict = dict()
    for j in range(N):
        k = dna_arr[j][i]
        hd_dict[k] = hd_dict.get(k, 0) + 1
    hd_list = sorted(hd_dict.items(), key = lambda x:(-x[1], x[0]))
    hd_total += N - hd_list[0][1]
    print(hd_list[0][0], end='')

print()
print(hd_total)