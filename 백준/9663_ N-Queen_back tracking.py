n=int(input())
answer=0
row=[0]*n #1차원으로 좌표 표현 ex) row[1]=2 -> (1,2)

def is_promising(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i): # 동일 열 or 대각선에 위치하면
            return False #false -> 위치 못시킨다는 표시
    return True #위치 가능하다는 표시

def solution(x):
    global answer
    
    if x==n: #x는 말을 두는 위치
        answer+=1
        return
    
    else:
        for i in range(n):
            row[x]=i #(x,i)에 퀸을 위치
            if is_promising(x):
                solution(x+1)
                
                
solution(0)
print(answer)

        
    