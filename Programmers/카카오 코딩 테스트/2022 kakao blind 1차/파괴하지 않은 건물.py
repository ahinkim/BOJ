def solution(board, skill):
    # 누적합 구하기
    def cumulative_sum(array): 
        for type, r1, c1, r2, c2, degree in skill:
            if type == 1:
                degree = -degree
            array[r1][c1] += degree
            if c2+1 < M:
                array[r1][c2+1] -= degree
            if r2+1 < N:
                array[r2+1][c1] -= degree
            if c2+1 < M and r2+1 < N:
                array[r2+1][c2+1] += degree
                
        # 행 방향 누적합 구하기
        for i in range(N):
            for j in range(1, M):
                array[i][j] += array[i][j-1]
        # 열 방향 누적합 구하기
        for i in range(M):
            for j in range(1, N):
                array[j][i] += array[j-1][i]
            
            
    N = len(board)
    M = len(board[0])
    array = [[0]*M for _ in range(N)] 
    cumulative_sum(array)
    
    answer = 0
    for i in range(N):
        for j in range(M):
            board[i][j] += array[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer