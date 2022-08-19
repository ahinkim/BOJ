def key_value(word):
    res = 0
    for x in word:
        if '0'<= x <='9':
            res += int(x)
    return res

N = int(input())
array = [input() for _ in range(N)]
array.sort(key = lambda x : (len(x), key_value(x), x))
print(*array, sep = "\n")