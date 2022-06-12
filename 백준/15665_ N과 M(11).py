n,m=map(int,input().split())

li=sorted(list(map(int,input().split())))

visited=[False]*n 
data=[]

def dfs():
    if len(data)==m:
        print(' '.join(map(str,data))) 
        return
    flag=0 #중복 순열 방지
    for i in range(n):
        if flag!=li[i]:
            visited[i]=True
            data.append(li[i])
            flag=li[i]
            dfs()
            visited[i]=False
            data.pop()
            
dfs() 

