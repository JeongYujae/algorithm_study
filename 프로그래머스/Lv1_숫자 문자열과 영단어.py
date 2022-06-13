def solution(s):
    dic={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    answer=s
    for x in dic.items():
        answer=answer.replace(x[0],str(x[1]))
        
    return int(answer)