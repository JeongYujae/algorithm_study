a,b=map(int,input().split())
data=[]
for x in range(1,b+1):
    for _ in range(x):
        data.append(x)

print(sum(data[a-1:b]))
