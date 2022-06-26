n=int(input()) # 컴퓨터 수

m=int(input()) #연결된 쌍의 수

data=[ []*n for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    data[a].append(b) #연결은 쌍방이니까 ex) (1-2) 연결이면
    data[b].append(a) #1에도2 2에도 1 표시
    
cnt=0
visited=[0]*(n+1)

def dfs(start):
    global cnt
    visited[start]=1
    for i in data[start]:
        if visited[i]==0:
            dfs(i)
            cnt+=1
dfs(1)
print(cnt)
    


