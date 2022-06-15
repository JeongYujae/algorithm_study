n=int(input())
table=[]
for i in range(n):
    a,b=map(int,input().split())
    table.append([a,b])

dp=[0]*(n+1)
for i in range(n-1,-1,-1):
    if i+ table[i][0]>n: #범위를 넘어가면
        dp[i]=dp[i+1]  #0으로 설정하기
        
    else:
        dp[i]=max(dp[i+1], table[i][1]+dp[i+table[i][0]])
    
print(dp[0])
        
