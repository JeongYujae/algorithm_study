import sys
n,m=map(int,sys.stdin.readline().split())
data=[]
count=0
for i in range(100): #0이 가로 100, 세로 100인 빈 리스트 구현
    data.append([0]*100)

for i in range(n):
    l_x,l_y,r_x,r_y=map(int,sys.stdin.readline().split())
    for q in range(l_x,r_x+1): #각 끝칸도 포함된다는 문제의 조건 -> 마지막에 +1
        for w in range(l_y,r_y+1):
            data[q-1][w-1]+=1 #인덱스 번호임으로 -1한 값으로 계산

for x in data: #각각의 리스트 돌면서 조건에 맞는 case들을 count에 추가
    for y in x:
        if y>m:
            count+=1
print(count)