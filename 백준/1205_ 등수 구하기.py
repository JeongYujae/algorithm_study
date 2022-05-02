#1205

n,score,p=map(int,input().split())

if n: #n이 0이 아니라면 
  rank=list(map(int,input().split()))
  rank.append(score) #새로운 점수를 rank에 넣어주고
  rank.sort(reverse=True) #정렬
  answer=rank.index(score)+1 #인덱스에 1씩 더한 값= 순위
  if answer>p: #rank의 범위보다 크다면
    print(-1)
  else: #rank의 범위와 같고 append 한 값이 추가되어서 범위를 넘기는 경우의 수 고려
    if n==p and score==rank[-1]:
      print(-1)
    else: #아니라면 순위 계산
      print(answer)
else:
  print(1)