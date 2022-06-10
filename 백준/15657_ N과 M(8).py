n,m=map(int,input().split())

li=sorted(list(map(int,input().split()))) #데이터 input 받고 오름차순으로 정렬

data=[]

def dfs(start):
    if len(data)==m: #데이터가 원하는 조건일 때 끊어주기
        print(' '.join(map(str,data))) 
        return
    
    for i in range(start,len(li)+1): #인덱스번호로 접근할거니까 1칸씩 밀어주기
        data.append(li[i-1])# 1번 값의 인덱스는 0번이니까/ 인덱스 번호로 접근해야함
        dfs(i) #나머지 로직 동일
        data.pop()
            
dfs(1)