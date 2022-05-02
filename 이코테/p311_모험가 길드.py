#이코테_ 1 모험가 길드_ 311

#모험가의 수

n=int(input())
data=list(map(int,input().split()))
data.sort()
answer=0 #총 그룹의 수
count=0 #현재 그룹의 모함가 수

for x in data:
  count+=1 #모험가 한명씩 추가
  if count>=x: #현재 그룹의 모험가 수> 공포도 -> 그룹으로 결정
    answer+=1 #그룹의 수 증가
    count=0 #그룹 내 모험가 수 초기화

print(answer)
