#1316

n=int(input())

answer=0
for _ in range(n):
    data=input()
    count=0
    for x in range(len(data)-1): #x+1로 하기 때문에, index를 맞춰줌
        if data[x]!=data[x+1]: #이어진 두 문자가 다른 경우
            data_new=data[x+1:] #새로운 문자열을 만들기 -> 비교한 문자열을 버린다는 개념
            if data_new.count(data[x])>0: #남은 문자열에 해당 문자가 있다면
                count+=1
    
    if count==0: # 비교하고 난 후 그 뒤의 문자열에 비교한 문자가 포함되어 있지 않은 경우만 포함
                 #ex) happy 에서 h 와 a를 비교한 후에 data_new=[appy]가 되는데, h가 없기 때문, 즉 정답의 문자열 경우기 때문에, 
        answer+=1
print(answer)


