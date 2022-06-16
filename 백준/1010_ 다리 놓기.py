# #factorial로 풀기
# t=int(input())
# import math
# for i in range(t):
#     n,m=map(int(input().split()))
#     answer=math.factorial(m)// (math.factorial(n)*math.factorial(m-n))
#     print(answer)



import sys
input=sys.stdin.readline

t=int(input())
dp = [[0 for _ in range(30)]for _ in range(30)] # [ [0 30개]씩 30개 ]

for i in range(1,30): #범위는 최대가 30 i는 서쪽
    for j in range(1,30): #j는 동쪽
        if i==1: #서쪽이 1일 때
            dp[i][j]=j
        elif i==j: #두 개의 사이트가 같을 때
            dp[i][j]=1
        else:
            if i<j: #동쪽에 사이트가 더 많을 때
                dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
            #서쪽이 더 많으면 무시
            

for i in range(t):
    n,m=map(int,input().split(' '))
    print(dp[n][m])
    
