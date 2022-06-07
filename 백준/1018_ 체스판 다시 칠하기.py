n,m=map(int,input().split())
data=[] #체스판
for i in range(n):
    data.append(list(input()))

result=[] #각각 몇개의 색을 바꿔야하는지를 담는 리스트
for x in range(n-7): #8 x 8 로 뽑을 수 있는 경우의 수 中 가로
    for y in range(m-7): #8 x 8 로 뽑을 수 있는 경우의 수 中 세로
        cnt1=0 
        cnt2=0
        for i in range(x,x+8): #8X8의 경우의 수대로 짜른 판 中 가로 탐색 시작
            for w in range(y,y+8): #8X8의 경우의 수대로 짜른 판 中 세로 탐색 시작
                if (i+w) % 2==0: # 짝일때 경우
                    if data[i][w]=='W':
                        cnt1+=1
                    if data[i][w]=='B': 
                        cnt2+=1
            
                else: #홀일때 경우
                    if data[i][w]=='B':
                        cnt1+=1
                    if data[i][w]=='W':
                        cnt2+=1
        result.append(cnt1)
        result.append(cnt2)
print(min(result)) #가장 적게 바꿀 수 있는 경우
    
        