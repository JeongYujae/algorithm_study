from collections import defaultdict
#defaultdict: key에 대한 빈 value 값을 포함해주는 기능
#형태를 꼭 지정해줘야함

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report) # 중복 제거!(중요한 코드) -> 시간 초과를 해결해줌
    
    user_list_who_i_report = defaultdict(set) #비어있는 dict 구조 생성/ string 형태
    num_of_reported = defaultdict(int) #int 형태
    suspended = [] #k번 이상 신고당한 유저 목록 

    for r in report:
        do_report, be_reported = r.split() #공백 기준으로 잘라주고
        num_of_reported[be_reported] += 1 #신고당한 count +=1
        user_list_who_i_report[do_report].add(be_reported) #신고하는 계정에 신고된 계정 count 추가해주기
        
        if num_of_reported[be_reported] == k:
            suspended.append(be_reported)

    for s in suspended: #k번 이상 신고당한 유저목록을 하나하나씩
        for i in range(len(id_list)): #id_list의 길이만큼 돌면서
            if s in user_list_who_i_report[id_list[i]]: #유저목록이 내가 신고한 유저목록에 있다면
                answer[i] += 1

    return answer