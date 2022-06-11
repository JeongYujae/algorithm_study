def solution(s):
    answer = len(s)
    #1부터 압축 단위 늘려가면서 전부 탐색
    for i in range(1, len(s)//2+1):
        data=''
        prev=s[0:i] #맨 앞에서부터 i 까지의 문자열 추출
        count=1
        for q in range(i,len(s),i): #단위 크기만큼 증가
            if prev==s[q:q+i]: #이전 상태와 같다면, count +1 
                count+=1
            else: #다른 문자열이 나왔을 때(더 이상 압축 X)
                data+=str(count)+prev if count>=2 else prev #2보다 크면 개수와 문자열, 아니면 문자열만
                prev=s[q:q+i] #문자열 초기화
                count=1
        #남은 문자열 처리
        data+=str(count) + prev if count>=2 else prev
        answer=min(answer,len(data))
    return answer