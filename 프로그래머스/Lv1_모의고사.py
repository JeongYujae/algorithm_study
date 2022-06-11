def solution(answers):
    player_1=[1,2,3,4,5]
    player_2=[2,1,2,3,2,4,2,5]
    player_3=[3,3,1,1,2,2,4,4,5,5]
    result=[0,0,0]
    answer = []
    for i in range(len(answers)):
        if answers[i]==player_1[(i%len(player_1))]:
            result[0]+=1
        if answers[i]==player_2[(i%len(player_2))]:
            result[1]+=1
        if answers[i]==player_3[(i%len(player_3))]:
            result[2]+=1
        
    for i in range(3):
        if result[i]==max(result):
            answer.append(i+1)


    return answer