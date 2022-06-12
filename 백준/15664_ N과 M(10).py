n,m=map(int,input().split())

li=sorted(list(map(int,input().split())))

visited=[False]*n 
data=[]

def dfs(start):
    if len(data)==m:
        print(' '.join(map(str,data))) 
        return
    flag=0 #중복 순열 방지
    for i in range(start,n):
        if not visited[i] and flag!=li[i]:
            visited[i]=True
            data.append(li[i])
            flag=li[i]
            dfs(i+1)
            visited[i]=False
            data.pop()
            
dfs(0) #인덱스로 값을 호출하니까 0부터 시작

