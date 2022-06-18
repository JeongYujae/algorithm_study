# n=int(input()) #스위치 개수

# status=list(map(int,input().split())) #스위치의 상태

# student=int(input())

# for i in range(student):
#     gender, target=map(int,input().split())
#     same_list=[]
#     if gender==1:
#         for x in status:
#             if x%target==0:
#                 if x==0:
#                     status[x]=1
#                 else:
#                     status[x]=1
    
#     if gender==2: #여자일때
#         for i in range(min(abs(0-target), n-target)): #우어진 범위만큼
#             if status[target-i] != status[target+i]: #만약 좌우가 다르면
#                 if status[target]==0: #자기 자신만 바꿔줌
#                     status[target]=1
#                     break
#                 else:
#                     status[target]=0
#                     break
                    
#             else: #만약 좌우가 같으면
#                 if target not in same_list: #same_list 자기 자신 없으면
#                     same_list.append(status[target-i])
#                     same_list.append(status[target])
#                     same_list.append(status[target+i])
#                 else: #same_list에 자기 자신 있으면(1,2 그 이상으로 넘어갈떄를 고려)
#                     same_list.append(status[target-i])
#                     same_list.append(status[target+i])
                    

def change(num):
    if switch[num]==0:
        switch[num]=1
    else:
        switch[num]=0
    return


n=int(input())
switch=[-1]+list(map(int,input().split()))
students=int(input())

for _ in range(students):
    gender,num=map(int,input().split())
    if gender==1: #남자면
        for i in range(num,n+1,num): #배수만 찾는 for문 스킬
            change(i)
    else: #여자면
        change(num) #먼저 자기자신부터 바꿈 -> 좌우에 같든 틀리든 자기 자신으 바꿔야되니까
        for j in range(n//2): #반씩 탐색이니까 -> 범위를 반으로 두고
            if num+j>n or num-j<1: #범위를 넘어가면 그만
                break
            if switch[num+j]==switch[num-j]: # 좌우가 같을 시,
                change(num+j) #바꿔줌
                change(num-j)
                
            else: #좌우가 다르면,
                break #끊어줌
            
for i in range(1,n+1): #20씩 끊어서 print 해주기
    print(switch[i],end = " ")
    if i%20==0:
        print()
            

    