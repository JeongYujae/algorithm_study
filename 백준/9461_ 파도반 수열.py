import sys

input=sys.stdin.readline

n=int(input())

p=[1,1,1,2,2] # 조건에 부합하지 않은 앞자리 5개 미리 지정
for i in range(5,100):
    p.append(p[i-1]+p[i-5]) #조건에 맞게 값들 미리 append

for i in range(n): 
    x=int(input()) #input이 오면 
    print(p[x-1]) #그에 맞는 값 출력



 