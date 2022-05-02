#이코테_5 볼링공

import itertools

#n은 개수, m은 최대 무게
n,m=map(int,input().split())
data=list(map(int,input().split()))

#순열 조합 구하기
data_comb=(list(itertools.combinations(data,2)))
answer=[]
for x in data_comb:
  #중복되는 값 제거하기
  if x[0]!=x[1]:
    answer.append(x)

print(len(answer))