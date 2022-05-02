#2980

import sys

n,l=map(int,input().split())
count=0 #초 경과를 누적하기 위함
p=0 #위치(버스의)
for _ in range(n):
    d,r,g=map(int,sys.stdin.readline().split())
    count+=d-p #신호등으로 위치 이동
    p=d #위치변경
    if count%(r+g)<=r: #하단 부분 설명 기제
        count+=(r-(count%(r+g)))
count+=(l-p) #마지막 신호등에서 도로의 끝사의 거리만큼 count 추가
print(count)