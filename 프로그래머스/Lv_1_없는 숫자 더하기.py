def solution(numbers):
    num=[0,1,2,3,4,5,6,7,8,9]
    data=[]
    for x in num:
        if x not in numbers:
            data.append(x)
    answer=sum(data)

    return answer