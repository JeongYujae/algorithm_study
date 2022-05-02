# 13414

import sys

input = sys.stdin.readline

k,l=map(int,input().split())
data=[]
for _ in range(l):
  data.append(input())

for x in data:
  if data.count(x)>=2:
    #인덱스 값이 작은 것을 삭제
    data.remove(x)
for y in range(k):
  print(data[y])