import sys
input=sys.stdin.readline
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)] #2차원 리스트로 표현

w=0
b=0
def solution(x,y,n):
    global w, b
    finding_color=data[x][y] #찾고 있는 색 0 or 1
    flag=True # 같다고 기본값을 두고
    
    for i in range(x,x+n): # x를 0부터 시작할거니까 0~n 까지 탐색(가로)
        if not flag: # flag가 false => 찾는 색과 현재 좌표가 위치한 색이 다르다
            break
        
        for j in range(y,y+n):
            if finding_color!=data[i][j]: #찾고 있는 색과 현재 좌표가 위치한 색이 다르면
                flag=False #다르다고 두고
                solution(x,y,n//2) # 4개로 짜르기 시작 중 (좌 상)
                solution(x,y+n//2,n//2) #4개로 짜르기 시작 중 (우 상)
                solution(x+n//2,y,n//2) # 4개로 짜르기 시작 중 (좌 하)
                solution(x+n//2,y+n//2,n//2) # 4개로 짜르기 시작 중 (우 하)
                break
    if flag:
        if finding_color:
            b+=1
        else:
            w+=1
            
solution(0,0,n)
print(w)
print(b)