#시간 초과
import sys
k,n=map(int,sys.stdin.readline().split()) #k= 가지고 있는 랜선, n = 필요한 랜선

data=[]
for x in range(k):
    data.append(int(sys.stdin.readline()))

answer=sum(data)//n
# for i in range(1,answer):
while True:
    count=0
    for q in data:
        count+=(q//answer)
    if count==n:
        print(answer)
        break
    else:
        answer-=1
