from copy import deepcopy
# 라이언이 점수를 가져가는 경우와 못가져가는 경우로 나뉜다. 모든 경우의 수는 2*11
res = 0
answer = [0]*11
# 화살의 개수를 담은 자연수 n, 어피치가 맞힌 과녁 점수의 개수를 10점부터 0점까지 순서대로 담은 정수 배열 info
def solution(n, info):
    # 라이언이 현재까지 맞힌 과녁 점수 결과 리스트 lion_info, 인덱스 i, 어피치가 맞힌 총 화살 개수 n, 라이언이 얻은 총 점수 lion_total
    def dfs(lion_info, n, i, lion_total):
        global res
        global answer
        # 과녁 점수 score
        score = 10-i
        # n==0으로 막으면 안된다 3, 2 만 정답이된다
        if i > 10: # n이 0 이상으로 온다는 건 마지막 과녁에 다 맞췄다는 얘기
            if i > 10:
                i = 10
            lion_info[i] += n
            if lion_total > res:
                res = lion_total
                answer = lion_info
            # 라이언의 점수가 같을 경우 가장 낮은 점수를 더 많이 맞힌 경우를 return
            elif lion_total == res:
                for i in range(10, -1, -1):
                    if answer[i] > lion_info[i]:
                        break
                    elif answer[i] < lion_info[i]:
                        answer = lion_info
                        break
            return

        # 어피치가 맞힌 경우
        if info[i] != 0:
            # 라이언이 해당 과녁을 맞히지 않은 경우(어피치만 점수 획득)
            dfs(deepcopy(lion_info), n, i+1, lion_total-score)
        # 어피치가 맞히지 못한 경우
        else:
            # 라이언이 해당 과녁을 맞히지 않은 경우(둘 다 점수 획득 x)
            dfs(deepcopy(lion_info), n, i+1, lion_total)
        
        # 라이언이 이기기 위해 맞혀야 할 화살 개수
        lion_n = info[i]+1
        # 라이언이 어피치 보다 많이 해당 과녁을 맞힌 경우(라이언 점수 획득)
        if n >= lion_n:
            lion_info = deepcopy(lion_info)
            lion_info[i] = lion_n
            dfs(lion_info, n - lion_n, i+1, lion_total+score)


    dfs([0]*11, n, 0, 0)
    # 라이언의 점수가 더 높을 경우
    if res > 0:
        return answer
    # 라이언의 점수가 어피치의 점수보다 낮거나 같은 경우
    else:
        return [-1]

solution(5, [2,1,1,1,0,0,0,0,0,0,0])