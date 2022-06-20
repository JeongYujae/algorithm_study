import sys
input=sys.stdin.readline

n,m=map(int,input().split())

d=set() #set형식으로 중복 제거 조건 만족시키고

for i in range(n):
    d.add(input().strip())

b=set()
for i in range(m):
    b.add(input().strip())
    
answer=sorted(list(d&b)) #두 집합의 교집합을 리스트로 만들고 정렬

print(len(answer))

for x in answer:
    print(x)



# import sys
# input=sys.stdin.readline

# n,m=map(int,input().split())
# d=[]
# b=[]
# for _ in range(n):
#     d.append(input().strip())
# d=list(set(d))
# for _ in range(m):
#     name=input().strip()
#     if name in d:
#         b.append(name)   
# b=list(set(b))
# b.sort()        
# print(len(b))
# for x in b:
#     print(x)