def solution(left, right):
    result=0
    for x in range(left,right+1):
        count=0
        for i in range(1,x+1):
            if x%i==0:
                count+=1
        if count%2==0:
            result+=x
        else:
            result-=x
    return result