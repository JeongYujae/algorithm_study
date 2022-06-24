# n=int(input())
# data=list(map(int,input().split()))

# result=[]
# for i in range(0,n):
#     up_list=[0]
#     down_list=[0]
#     if i==0:
#         target_up=data[0]
#         up_list.append(target_up)
#         target_down=data[0]
#         down_list.append(target_down)
        
#     for x in range(i,n):
#         target_up=max(up_list)
#         target_down=max(down_list)
#         if target_up<data[x]: #
#             up_list.append(data[x])
            
#         elif target_down>data[x]:
#             down_list.append(data[x])
    
#     if len(up_list)>=len(down_list):
#         result.append(up_list)
#     else:
#         result.append(down_list)
        
# for x in result:
#     del x[0]
# result.sort(key=len,reverse=True)
# print(len(result[0]))
# print(*result[0])


n=int(input())
data=list(map(int,input().split()))
dp=[1]*n

for i in range(1,n): #처음부터 탐색
    for j in range(i): #처음의 수와 비교할 값들 탐색
        if data[i]>data[j]: #더 크면
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))

result=max(dp)
list=[]
for i in range(n-1,-1,-1): #거꾸로 탐색하면서
    if dp[i]==result: #dp값과 맞으면
        list.append(data[i]) #해당하는 dp값 모두를 list에 넣어야하니까
        result-=1 #count를 -1 해주고
        
list.reverse() #뒤집어주고
for i in list:
    print(i, end=' ')