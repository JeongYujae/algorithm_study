def solution(name):
    change=[min((ord(i)-ord('A')), ord('Z')-ord(i)+1) for i in name] #상하 최소 거리 -> 알파벳 변경
    count=0
    answer=0
    while True:
        answer+=change[count]
        change[count]=0
        if sum(change)==0:
            return answer
        
        
        left ,right =1 ,1
        while change[count-left]==0:
            left+=1
        while change[count-right]==0:
            right+=1
            
        if left<right:
            answer+=left
        else:
            answer+=right
            
        if left<right:
            change-=left
        else:
            change-=right
        
        
        