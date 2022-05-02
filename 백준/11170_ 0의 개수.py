t=int(input())

for _ in range(t):
    cnt=0
    n,m=map(int,input().split())
    for i in range(n,m+1):
        x=str(i)
        cnt+=x.count('0')
    print(cnt)
