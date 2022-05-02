#2960

#참고 풀이

n,k=map(int,input().split())

count=0

data=[True]*(n+1) #True로 된 data값을 길이보다 하나 크게 생성(0~n까지의 list 생성)
 
for x in range(2, len(data)+1): # 2부터 끝까지 범위 부여 -> x라는 숫자에 대한 control을 위한 for문
    for y in range(x, n+1, x): # 배수를 처리하는 방법
        if data[y]==True: 
            data[y]=False #가장 작은 소수의 배수들을 지워주는 과정을 False로 바꾸며 구현
            count+=1
            if count==k:
                print(y)
                break
















# n,k=map(int,input().split())

# #리스트 구현(2~n까지)
# data=[]
# a=2
# for x in range(n-1):
#     data.append(a+x)

# # 조건 구현

# count=0
# while count!=k:
#     for x in data:
#         p=min(data)
#         if x%p==0:
#             data.remove(x)
#         count+=1
#     print(data,p,count)
        
    








# count=0
# p=min(data)
# for x in data: 
#     if count==k:
#         print(x)
#         break
    
#     if x%p==0:
#         data.remove(x)

#     if x%p==0 not in data:
#         p=min(data)
    
#     count+=1
   