from collections import deque

m,n=map(int,input().split())

#토마토의 위치를 2차원 리스트로 받아주고
data=[list(map(int,input().split())) for i in range(n)]

queue=deque([])

#방향 이동 리스트 (-1,0) (1,0) (0,-1) (0,1) 이런식으로 이동
dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=0
for i in range(n): #첫 토마토 위치 좌표
    for j in range(m):
        if data[i][j]==1:
            queue.append([i,j])

def bfs():
    while queue: #토마토가 1인 자리를 추가했으면,
        #첫 좌표
        x,y=queue.popleft() #그 자리 좌표 꺼내고
        #좌표 기준 좌 우 하 상 탐색
        for i in range(4):
            nx=dx[i]+x #좌표를 이동시켜두고
            ny=dy[i]+y #좌표를 통해 조건에 맞나 확인
            
            #n,m 크기를 벗어나면 안되고, 토마토가 0, 익지x
            if 0<= nx < n and 0<=ny <m and data[nx][ny]==0:
                data[nx][ny]=data[x][y]+1 #그 좌표에 count를 올려줌
                queue.append([nx,ny])
bfs()

for i in data:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answer=max(answer,max(i))

print(answer-1)
