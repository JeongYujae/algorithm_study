import sys
import heapq

input=sys.stdin.readline
INF=100000000

V,E=map(int,input().split())
#시작점
k=int(input())

dp=[INF]* (V+1)
heap=[]
data=[[] for _ in range(V+1)]

def solution(start):
    #dp 시작점을 0으로 초기화
    dp[start]=0
    heapq.heappush(heap,(0,start))
    
    while heap:
        num,now=heapq.heappop(heap)
        
        #현재 테이블보다 더 가중치가 큰 튜플(즉, 더 오래걸리는 경우) 무시
        if dp[now]<num:
            continue
        
        
        for w,next in data[now]:
            #현재까지의 가중치 + 다음 노드까지의 가중치
            next_num=w+num
            if next_num<dp[next]: #다음 노드까지의 가중치 < 현재의 값=> 찾고자 하는 조건임
                dp[next]=next_num #dp에 넣고
                heapq.heappush(heap,(next_num,next)) #(가중치, 다음 점) append
              
#다시 초기화  
for _ in range(E):
    u,v,w=map(int,input().split())
    data[u].append((w,v))
                
solution(k)
for i in range(1,V+1):
    if dp[i]==INF:
        print("INF")
    else:
        print(dp[i])