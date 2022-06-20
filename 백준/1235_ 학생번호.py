n=int(input())
data=[] #주어진 문자열들을 추가하기
for i in range(n):
    data.append(input().strip())

cnt=1 #맨 뒷자리에서 같으면 1이니까
for i in range(len(data[0]),0,-1): #맨 뒤에서 맨 앞까지 이동
    result=set() #set형으로 중복을 제거
    for x in data: #각 data 하나씩 돌면서
        target=x[i-1:len(data[0])] #탐색 범위 지정
        result.add(target) #set형에 추가 -> 중복되면 자동으로 제거
    if len(result)==n: #만약 3개가 모두 숫자가 추가되었다면,
        print(cnt) #cnt 출력
        break
    else: #set형에 의해 중복이 제거되었다면,
        cnt+=1 #범위 늘려서 다시 탐색
            
        