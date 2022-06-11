def solution(a, b):
    data=[]
    for i in range(len(a)):
        data.append(a[i]*b[i])
    answer=sum(data)
    return answer