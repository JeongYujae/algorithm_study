n=int(input())

data=list(map(int,input().split()))

dp_up=[1]*n
dp_down=[1]*n

for i in range(1,n):
    if data[i-1]>=data[i]: #오름 차순
        dp_up[i]=max(dp_up[i],dp_up[i-1]+1)
    
    if data[i-1]<=data[i]: #내림 차순
        dp_down[i]=max(dp_down[i],dp_down[i-1]+1)
        
print(max(max(dp_up), max(dp_down)))
        







# if set(data)[0]>set(data[1]):
#     flag=0 #내림 차순 수열
# else:
#     flag=1 #오름 차순 수열

# cnt=0
# for i in range(n):
#     target=data[i]
#     for j in range(i,n):
#         if flag==0: # 내림 차순 수열이라면   
#             if target>=j:
#                 cnt+=1
#                 target=data[j]
#             else:
#                 print(cnt)
#                 break
#         else:
#             if target<=j:
#                 cnt+=1
#                 target=data[j]
#             else:
#                 print(cnt)
#                 break