import sys
data=[]
n,k=map(int,sys.stdin.readline().split())

for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))


data.sort(key=lambda x: (x[1],x[2],x[3]), reverse=True) # lambda, 다중조건으로 sort 하기

for i in range(n):
    if data[i][0]==k:
        index=i

for q in range(n):
    if data[index][1:]==data[q][1:]:
        print(q+1)
        break
        
 
#순위 조건 구현하기

    