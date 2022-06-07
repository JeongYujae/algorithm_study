data=[]
num=666
n=int(input())

while True:
    if '666' in str(num):
        data.append(num)
    if len(data)==n:
        print(data[-1])
        break
    num+=1
        
    