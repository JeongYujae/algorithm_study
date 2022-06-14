#dp로 풀이

import sys
input=sys.stdin.readline

n=int(input())

if n==1:
    print(1)
else:
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    
    for i in range(3,n+1):
        dp[i]= (dp[i-1]+dp[i-2]) % 15746
        
    print(dp[n])


# #메모리 초과
# from itertools import product
# data=['0','1']

# n=int(input())
# data=list(product(data,repeat=n))
# for i in range(len(data)):
#     data[i]=''.join(data[i])

# answer=[]
# for x in data:
#     if x.count('0')%2==0:
#         if '00' in x:
#             answer.append(x)
            
            
# if n==1:
#     print(1)
# elif n==2:
#     print(2)
# else:
#     print(len(answer))