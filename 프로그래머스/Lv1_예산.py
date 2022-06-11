def solution(d, budget):
    d.sort()
    cnt=0
    for i in d:
        if budget-i>=0:
            cnt+=1
            budget-=i

    answer = cnt
    return answer