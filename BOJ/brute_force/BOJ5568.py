from itertools import permutations
n = int(input())
k = int(input())
array = [str(input()) for _ in range(n)]
array = list(permutations(array, k))
res = set()
for x in array:
    x = ('').join(x)
    res.add(x)

print(len(res))