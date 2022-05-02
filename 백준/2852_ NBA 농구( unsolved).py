# data=[0,0]
# minute=0
# n=int(input())

# for _ in range(n):
#     team,time=input().split()
#     team=int(team)
#     minute=int(time[3:])+int(time[:2])*60
#     data[team-1]=minute
#     if max(data)==data[team-1]:
        

#     print(abs(data[0]-data[1])) #앞서고 있던 시간 계산




############################


n=int(input())

score=[0,0]
t=[0,0]
minute=0
answer=[0,0]
for _ in range(n):
    team,time=input().split()
    team=int(team)
    minute=(int(time[:2])*60)+int(time[3:]) #시 분 -> 분으로 전환
    score[team-1]+=1
    if score[team-1]==max(score): #2개중에 가장 크다면 -> 이기고 있다면
        t[team-1]+=minute
        print('aaaaa:',t[team-1])
        answer[team-1]=abs(t[0]-t[1])
    print(score,minute,t,answer)

    

