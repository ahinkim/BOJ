from math import sqrt
import sys
def solution(brown, yellow):
    input = lambda : sys.stdin.readline().rstrip()
    for i in range(1, int(sqrt(yellow * brown))):
        if yellow % i == 0:
            col = i      
            row = yellow // i
            print(col, row, brown)
            if 2 * col + 2 * row + 4 == brown:
                answer = [row + 2, col + 2]
                break
    return answer