# 시간 초과
# from itertools import permutations
# n=int(input())

# data=[i for i in range(1,n+1)]

# li=list(map(list,permutations(data,n)))
# target=list(map(int,input().split()))

# for x in li:
#     if target ==x:
#         if li.index(x)==0:
#             print(-1)
#         else:
#             q=li[li.index(x)-1]
#             for w in q:
#                 print(w, end=' ')
                
                
                

                
n=int(input())
a=list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if a[i] < a[i-1]: #앞 인덱스보다 뒷 인덱스보다 크면
        x, y = i-1, i #자리 바꿔주기 (내림차순이니까)
        for j in range(n-1, 0, -1):
            if a[j] < a[x]: #앞 인덱스보다 뒷 인덱스보다 크면
                a[j], a[x] = a[x], a[j] #자리 바꿔주기 (내림차순이니까)
                a = a[:i] + sorted(a[i:], reverse=True)
                print(*a)
                exit(0)
print(-1)               
                
                