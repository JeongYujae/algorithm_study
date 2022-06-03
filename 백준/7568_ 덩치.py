n=int(input())
data=[]
cnt=[0]*n
for i in range(n):
    data.append(list(map(int,input().split())))

for x in data:
    rank=1
    for y in data:
        if x[0]<y[0] and x[1]<y[1]:
            rank+=1
    print(rank, end=' ')