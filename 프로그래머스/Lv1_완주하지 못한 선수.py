def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer=''
    for p,c in zip(participant,completion):
        if p!=c:
            return p
    answer=participant.pop()
            
    return answer