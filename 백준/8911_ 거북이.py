import sys

input=sys.stdin.readline
t=int(input())

dx=[0,-1,0,1] #이동 좌표를 미리 지정 (0,1) (0,-1) (0,-1) (1,0)
dy=[1,0,-1,0] #북:(0,1) 서:(0,-1) 남:(0,-1) 동:(1,0)
for _ in range(t):
    order=list(map(str,input().strip()))
    dir=0 #북:0 서:1 남:2 동:3
    min_x,min_y,max_x,max_y=0,0,0,0
    x,y=0,0 #현재 좌표
    for ord in order:
        if ord=='F': #front는 앞으로
            x+=dx[dir]
            y+=dy[dir]
            
        elif ord=='B': #back은 뒤로
            x-=dx[dir]
            y-=dy[dir]
            
        elif ord=='L': #left면 왼쪽으로 변경
            if dir==3: #동에서 왼쪽은 북
                dir=0 #북으로 변경(4를 처리해주는 로직)
            else:
                dir+=1
        elif ord=='R':
            if dir==0:
                dir=3
            else:
                dir-=1
        
        min_x=min(min_x,x)
        min_y=min(min_y,y)
        max_x=max(max_x,x)
        max_y=max(max_y,y)

    print(abs(max_x-min_x)*abs(max_y-min_y))
        
            