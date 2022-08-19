import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
graph = [[False] * 26 for _ in range(26)]
for _ in range(n):
    a, oper, b = input().split()
    a = ord(a) - ord('a')
    b = ord(b) - ord('a')
    graph[a][b] = True

for k in range(26):
    for a in range(26):
        for b in range(26):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = True

m = int(input())
for _ in range(m):
    a, oper, b = input().split()
    a = ord(a) - ord('a')
    b = ord(b) - ord('a')
    if graph[a][b]:
        print('T')
    else:
        print('F')