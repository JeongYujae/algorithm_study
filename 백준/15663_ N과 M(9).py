n,m=map(int,input().split())

li=sorted(list(map(int,input().split())))

visited=[False]*n #방문여부를 등록해주고 ->방문할 숫자 결정
data=[]

def dfs():
    if len(data)==m:
        print(' '.join(map(str,data))) 
        return
    flag=0 #중복 순열 방지
    for i in range(n):
        if not visited[i] and flag!=li[i]:
            visited[i]=True
            data.append(li[i])
            flag=li[i]
            dfs() #나머지 로직 동일
            visited[i]=False
            data.pop()
            
dfs()

