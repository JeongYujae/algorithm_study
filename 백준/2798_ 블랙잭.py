#2798

n,m=map(int,input().split())
data=list(map(int,input().split()))
answer=[]
for i in range(0,n-2):
    for x in range(i+1,n-1):
        for q in range(x+1,n):
            if data[i]+data[x]+data[q]<=m:
                answer.append(data[i]+data[x]+data[q])
            else:
                continue
answer=sorted(answer,reverse=True)
print(answer[0])

            
    





    

# for i in range(n):
