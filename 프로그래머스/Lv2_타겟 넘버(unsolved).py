#dfs 잘 모르겠음...(unsolved...)
#dfs로는 출력초과남


def solution(numbers, target):
    answer=dfs(numbers,target,0)
    return answer
    
def dfs(numbers,target,s):
    answer=0
    if s==len(numbers):
        if sum(numbers)==target:
            return 1
        else:
            return 0
    else:
        answer+=dfs(numbers,target,s+1)
        numbers[s]*=-1
        answer+=dfs(numbers,target,s+1)
        return answer
