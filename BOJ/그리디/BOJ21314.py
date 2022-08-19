data = input()
m = 0
max_v = ''
min_v = ''
for x in data:
    if x == 'M':
        m += 1
    if x == 'K':
        max_v += str(5 * 10 ** m)
        if m == 0:
            min_v += '5'
        else:
            min_v += str(int(10 ** m + 5)) 
        m = 0
if m:
    max_v += '1' * (m)
    min_v += str(10 ** (m - 1))

print(max_v)
print(min_v)