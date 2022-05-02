#1475 

n=int(input())

data=[0]*9
for x in n: #문자열 하나하나씩을 비교
    x=int(x)
    if x ==9: #9를 6으로 바꿔주고
        x=6
    data[x]+=1 #0이었던 리스트의 count를 올려줌
data[6]=(data[6]+1)//2
print(max(data))