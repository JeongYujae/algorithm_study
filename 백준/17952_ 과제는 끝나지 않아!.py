# # 시간 초과
# import sys
# input=sys.stdin.readline

# n=int(input())
# working=[]
# score=0
# for i in range(n):
#     inp=input()
#     if inp[0] =='0':
#         if working[-1][1]-1==0: #working에서 과제를 완료하면
#             score+=working[-1][0]
#             working.pop(-1)
#         else: #과제를 완료하지 못했으면
#             working[-1][1]-=1
            
#     else:
#         a,s,t=map(int,inp.split())
#         if t-1==0:
#             score+=s
#         else:
#             working.append([s,t-1]) #(점수,시간) 으로 working리스트에 넣는다
# print(score)
        
        
from collections import deque
import sys

input=sys.stdin.readline

working=deque()
score=deque()

n=int(input())

for i in range(n):
    data=list(map(int,input().split()))
    if data[0]==1: #앞이 1이면
        working.append([data[1],data[2]]) # working 리스트에 넣기
    else:
        pass #0이면 그냥 넘겨주기
    
    if working: #working에 추가 로직 거친 후에, working에 값이 있다면
        working[-1][-1]-=1 #1초 지났으니 1 줄여줌
        if working[-1][-1]==0: #줄여서 0이면?
            score.append(working[-1][0]) #score에 점수를 추가
            working.pop() #working 리스트에서 삭제
            
print(sum(score))