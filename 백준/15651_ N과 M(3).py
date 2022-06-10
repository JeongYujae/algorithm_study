n,m=map(int,input().split())

data=[] 
def dfs():
    if len(data)==m: #만약 m개를 뽑았다면
        print(' '.join(map(str,data))) 
        return
    
    for i in range(1,n+1): #1부터 max값까지
            data.append(i) #추가해주고
            dfs() #재귀적으로 호출
            data.pop()
            
dfs()