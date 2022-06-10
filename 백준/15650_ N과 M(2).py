n,m=map(int,input().split())

data=[] 
def dfs():
    if len(data)==m and data==sorted(data): #만약 m개를 뽑고 오름차순이라는 조건
        print(' '.join(map(str,data))) 
        return
    
    for i in range(1,n+1): #1부터 max값까지
        if i not in data: #m개의 자리 중에 그 수가 없다면
            data.append(i) #추가해주고
            dfs() #재귀적으로 호출
            data.pop()
            
dfs()