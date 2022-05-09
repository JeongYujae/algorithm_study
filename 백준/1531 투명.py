import sys
n,m=map(int,sys.stdin.readline().split())
data=[]
count=0
for i in range(100):
    data.append([0]*100)

for i in range(n):
    l_x,l_y,r_x,r_y=map(int,sys.stdin.readline().split())
    for q in range(l_x,r_x+1):
        for w in range(l_y,r_y+1):
            data[q-1][w-1]+=1
for x in data:
    for y in x:
        if y>m:
            count+=1
print(count)