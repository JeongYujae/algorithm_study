n=input()
f=int(input())
target=int(n)-int(n[-2:])

for x in range(target,target+100):
    if x%f==0:
        x=(str(x))
        print(x[-2:])
        break