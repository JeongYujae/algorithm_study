#2941

croa=['c=','c-','dz=','d-','lj','nj','s=','z=']
data=input()
for x in croa:
    data=data.replace(x,'*')
print(len(data))
    