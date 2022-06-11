def solution(x):
    data=sum(list(map(int,list(str(x)))))

    if x%data==0:
        answer=True
    else:
        answer=False
        
    return answer