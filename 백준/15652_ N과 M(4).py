n,m=map(int,input().split())

data=[] 
def dfs(start):
    if len(data)==m: 
        print(' '.join(map(str,data))) 
        return
    
    for i in range(start,n+1):
            data.append(i) 
            dfs(i) #재귀 호출할 때 start를 돌리는 값이 다른 문제에서는 1이었다면, 
                   #이 문제에서는 하나씩 올려서 (2,1) (3,1) (3,2) 이런 값들은 애초에 X
            data.pop()
            
dfs(1)