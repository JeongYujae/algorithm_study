def solution(n, lost, reserve):
    reserve_set=set(reserve)-set(lost) #여벌 체육복을 도난당했을 경우도 존재하기 때문에
    lost_set=set(lost)-set(reserve)
    for i in reserve_set: #여분의 체육복이 있는 사람 기준
        if i-1 in lost_set: #왼쪽부터 lost 사람이 있으면
            lost_set.remove(i-1) #reserve가 하나를 주니까 -> 잃어버린 리스트에서 삭제
        elif i+1 in lost_set: #만약 왼쪽에 lost가 없으면
            lost_set.remove(i+1) #한칸 오른쪽 탐색-> 동일 로직
    answer=n-len(lost_set)
    return answer