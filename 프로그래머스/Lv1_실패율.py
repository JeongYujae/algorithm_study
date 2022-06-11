def solution(N, stages):
    answer = []
    people=len(stages)
    dic={}
    for i in range(1, N+1):
        if people!=0:   
            dic[i]=stages.count(i)/people
            people-=stages.count(i)
        else:
            dic[i]=0
            
    answer=sorted(dic, key=lambda i: dic[i], reverse=True)
    return answer