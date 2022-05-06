# #출력초과
# import sys
# h,w=map(int,sys.stdin.readline().split())
# data=[]
# for _ in range(h):
#     data.append(list(sys.stdin.readline().strip()))
# print(data)

# for x in data:
#     count=0
#     ans=[]
#     for y in x:
#         if 'c' not in x:
#             ans=[-1]*w
#         else:
#             if 'c'==y:
#                 ans.append(0)
#                 count=0
#             else:
#                 if 0 not in ans:
#                     ans.append(-1)
#                 else:
#                     ans.append(count)
#             count+=1
#     print(ans)

            
h,w=map(int,input().split())
data=[]
for i in range(h):
    data.append(input()) #2차원 리스트 구조 x
cloud=[[0]*w for i in range(h)]
flag=False
count=1
for i in range(h):
    for j in range(w):
        if flag==False and data[i][j]=='.': #c를 만나기 이전의 구름이 없는 상황
            cloud[i][j]=-1
        elif data[i][j]=='c':
            flag=True #c 등장
            count=1
            
        else: #flag가 True고 나오는 칸
            cloud[i][j]=count
            count+=1
    flag=False #다시 초기화해놓고 새로운 줄 계산
    count=1

for i in range(h):
    for j in range(w):
        print(cloud[i][j], end=' ')
    print() #줄 바꿈
        
        
            