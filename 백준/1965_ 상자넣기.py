n=int(input())
data=list(map(int,input().split()))

dp=[]
dp.append(1)

for i in range(1,n): #기준점을 탐색시키는 for문
    temp=[] #나보다 작은 값들의 dp 값들을 임의로 담아두는 리스트
    for j in range(i): #기준점보다 뒤에 있는 index를 탐색시키는 for문
        if data[i]>data[j]: #나보다 작은 수가 있으면
            temp.append(dp[j]+1) #1을 더해서 임의의 리스트에 추가
    
    if len(temp)==0: #나보다 작은 값이 없다면
        dp.append(1) #그냥 1 더해주기
    
    else: #나보다 작은 값이 있으면
        dp.append(max(temp)) #그 값들 중에서 가장 큰 값을 내 dp에 추가해줘
        
print(max(dp))