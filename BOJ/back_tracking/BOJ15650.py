def dfs(data, res):
    if len(res) == M:
        print(*res)
        return
    new_data = data
    for x in data:
        new_data = new_data.replace(x, '')
        dfs(new_data, res + x)
        

import sys
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
data = ''.join([str(i) for i in range(1, N + 1)]) 
dfs(data, "")