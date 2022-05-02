# import sys
# k=int(sys.stdin.readline())
# data=[]
# for _ in range(k):
#     data.append(sys.stdin.readline().strip())
# data=list(map(int,data))
# new_data=data

# for x in range(1,k):
#     if data[x]==0:
#         new_data=new_data.remove(new_data[x-1])
#     print(data, new_data)

# ------------------------

#정답 코드

k=int(input())
data=[]
for i in range(k):
    num=int(input())
    if num==0:
        data.pop()
    else:
        data.append(num)
print(sum(data))









# y=1
# while y<len(data):
#     if data[y]==0:
#         data=data.remove(data[y-1])
#     y+=1
#     print(data)

