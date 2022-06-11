def solution(record):
    dic={}
    answer=[]

    for x in record:
        id_name=x.split()
        if len(id_name)==3:
            dic[id_name[1]]= id_name[2]  

    for y in record:
        id_name=y.split()
        if id_name[0]=='Enter':
            answer.append('%s님이 들어왔습니다.' %dic[id_name[1]])
        elif id_name[0]=='Leave':
            answer.append('%s님이 나갔습니다.' %dic[id_name[1]])
    
    return answer