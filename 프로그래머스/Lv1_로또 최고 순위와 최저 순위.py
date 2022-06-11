def solution(lottos, win_nums):
    new_lottos= lottos
    new_win_nums=win_nums
    answer = []
    count=0
    for i in win_nums:
        if i in lottos:
            new_lottos.remove(i)
            count+=1

    worst=7-count
    for i in lottos:
        if i in win_nums:
            new_win_nums.remove(i)

    for x in new_lottos:
        if x==0 and len(new_win_nums)>=1:
            count+=1
    best=7-count
    
    if best==7:
        answer.append(6)
    else:
        answer.append(best)
    if worst==7:
        answer.append(6)
    else:
        answer.append(worst)
        
    return answer