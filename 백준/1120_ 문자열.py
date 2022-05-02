a,b=input().split()

answer=[]

for x in range(len(b)-len(a)+1): #두 문자열의 길이차를 기준으로 비교/ +1을 하는 이유 -> 두 문자열의 길이가 같아도 동작하게 하려고
    count=0
    for y in range(len(x)): #첫번째 문자열의 길이만큼 기본값으로 설정
        if a[y]!= b[x+y]:
            count+=1
    answer.append(count)
    

                            
                