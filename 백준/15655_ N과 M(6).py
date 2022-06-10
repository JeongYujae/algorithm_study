n,m=map(int,input().split())

li=sorted(list(map(int,input().split()))) #데이터 input 받고 오름차순으로 정렬

data=[]

def dfs():
    if len(data)==m and data==sorted(data): #오름차순일때의 조건 포함
        print(' '.join(map(str,data))) 
        return
    
    for i in range(len(li)): #범위는 주어진 리스트의 길이, n으로 써도 됨
        if li[i] not in data:
            data.append(li[i]) 
            dfs()
            data.pop()
            
dfs()