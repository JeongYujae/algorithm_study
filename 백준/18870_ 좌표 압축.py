#시간 초과
# import sys
# input=sys.stdin.readline
# n=int(input())

# data=list(map(int,input().split()))
# data_sorted=sorted(list(set(data)))
# dic={}
# for x in data:
#     cnt=0
#     for y in data_sorted:
#         if x>y:
#             cnt+=1
#     dic[x]=cnt

# result=[]
# for i in data:
#     result.append(dic[i]) 
# print(result)


#해결
import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))

data_sorted=sorted(list(set(data)))


dic={data_sorted[i]:i for i in range(len(data_sorted))}
for i in data:
    print(dic[i],end=' ')