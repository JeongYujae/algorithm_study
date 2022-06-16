
def solution(numbers, target):
    answer=dfs(numbers,target,0)
    return answer
    
def dfs(numbers,target,s):
    answer=0
    if s==len(numbers): #탐색이 모두 완료되면
        if sum(numbers)==target: #target에 맞으면
            return 1
        else:
            return 0
    else: #탐색 완료 전
        answer+=dfs(numbers,target,s+1) #현재 값을 더한채로 다음 index dfs 계산
        numbers[s]*=-1 #현재 값을 -로 변환하고
        answer+=dfs(numbers,target,s+1) #현재 값을 뺀채로 다음 index dfs 계산 
        return answer
