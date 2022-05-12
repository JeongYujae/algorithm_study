import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
data_limit=max(data)

m=int(sys.stdin.readline())
answer=list(map(int,sys.stdin.readline().split()))

for x in answer:
    if x>data_limit:
        print(0)
    else:
        print(1)


