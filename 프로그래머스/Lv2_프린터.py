def solution(priorities, location):
    from collections import deque
    answer=0
    data=[]
    for v,i in enumerate(priorities):
        data.append((i,v))
    data=deque(data)
    while len(data):
        item=data.popleft()
        if data and max(data)[0]>item[0]: #맨 앞 작업이 중요도가 젤 높은게 아니라면
            data.append(item)
        else: #가장 크다면
            answer+=1 #count를 올려줌
            if item[1]==location: #만약 찾고자 하는 작업이 나온다면, 1번 인덱스 -> 작업의 순서번호니까
                                  #1 1 1 1들이 다 같은 1이 아니라 서로 다른 1임을 이용한 코드
                break
    return answer