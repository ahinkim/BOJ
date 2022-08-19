# matrix를 90도 회전시키는 함수
def rotate_90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = matrix[i][j]
    return result
# 열쇠가 자물쇠에 맞는 지 확인하는 함수
def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n):
        for j in range(n):
            if new_lock[n + i][n + j] != 1:
                return False
    return True
def solution(key, lock):
    answer = False  
    n = len(lock)
    m = len(key)
    # 자물쇠 크기 조정 # changed lock
    new_lock = [[0] * (n * 3) for _ in range(n * 3)] 
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
            
    for a in range(n * 2):
        for b in range(n * 2):
            # 4가지 방향에 대해
            for _ in range(4):
                # 열쇠 회전
                key = rotate_90(key)
                # 열쇠 채우기
                for i in range(m):
                    for j in range(m):
                        new_lock[a + i][b + j] += key[i][j]
                # 열쇠가 자물쇠에 맞는 지 확인
                if check(new_lock):
                    return True
                # 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[a + i][b + j] -= key[i][j]

    return False