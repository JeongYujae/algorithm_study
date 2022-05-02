data=list(map(int,input()))
result=data[0]
for i in range(len(data)-1):
    if data[i] !=0 and data[i+1] !=0:
        result=result*data[i+1]
    else:
        result=result+data[i+1]
print(result)