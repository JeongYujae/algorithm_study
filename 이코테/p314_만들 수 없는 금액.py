#이코테 _4 만들 수 없는 금액 -> 정답 확인해보기

import itertools

n=int(input())
data=list(map(int,input().split()))
data.sort()
data_comb=[]
for i in range(len(data)-1):
  a=data_comb.extend(list(itertools.combinations(data,i+1)))
answer_list=[]
for x in data_comb:
  answer_list.append(sum(x))

answer_list.sort()

new_list=[]
for v in answer_list:
    if v not in new_list:
      new_list.append(v)
      
x=1
for y in new_list:
  if x-y<0:
    print(x)
    break
  else:
    x+=1
