def solution(num):
    count=0
    while True:
        if num==1:
            break
        else:
            if num%2==0:
                num=num//2
                count+=1
            else:
                num=num*3 +1
                count+=1
        if count>500:
            return -1
            break
    answer=count
    return answer