n,m=map(int,input().split())

li=sorted(list(map(int,input().split()))) #데이터 input 받고 오름차순으로 정렬

data=[]

def dfs():
    if len(data)==m: #데이터가 원하는 조건일 때 끊어주기
        print(' '.join(map(str,data))) 
        return
    
    for i in range(len(li)):
        data.append(li[i]) 
        dfs()
        data.pop()
            
dfs()