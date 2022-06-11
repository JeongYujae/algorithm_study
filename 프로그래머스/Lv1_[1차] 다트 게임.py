def solution(dartResult):
    n=''
    score=[]
    for i in dartResult:
        if i.isnumeric(): #숫자면
            n+=i
        elif i=='S': #S는 숫자 뒤에 오니까
            n=int(n)**1 #앞에 있는 숫자 처리
            score.append(n) #점수에 더해주고
            n='' #n다시 초기화
        elif i=='D':
            n=int(n)**2
            score.append(n)
            n=''
        elif i=='T':
            n=int(n)**3
            score.append(n)
            n=''
        elif i=='*':
            if len(score)>1: #*앞에 숫자가 최소 2개가 있을 때
                score[-2]=score[-2]*2
                score[-1]=score[-1]*2
            else:
                score[-1]=score[-1]*2
        elif i=='#':
            score[-1]=score[-1]*-1
            
    return sum(score)