import sys
input = lambda : sys.stdin.readline().rstrip()
# 센서의 개수 n
n = int(input())
# 집중국의 개수 k
k = int(input())
# 센서의 좌표
sensors = list(map(int, input().split()))
sensors.sort()
# 센서 중복 제거
sensors = list(set(sensors))
n = len(sensors)
edges = []
for i in range(n - 1):
    edges.append(sensors[i + 1] - sensors[i])

edges.sort(reverse = True)
print(sum(edges[k - 1:]))