n=int(input())
count=0
row=[0]*n #1차원으로 좌표 표현 ex) row[1]=2 -> (1,2)
visited=[False]*n

def solution(x):
    global count
    if x==n: # x는 말을 두는 위치
        count+=1
        
    else:
        for i in range(n):
            if visited[i]: # 없어도 됨
                continue 
            
            row[x]=i # (x,i)-> 퀸 위치
            
            if check(x): #만약 탐색 가치가 있다면
                visited[i]=True #위치할 수 있음을 의미
                solution(x+1)
                visited[i]=False #다시 바꿔주고
                
def check(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i]) ==abs(x-i):
            return False
    return True

solution(0)
print(count)
