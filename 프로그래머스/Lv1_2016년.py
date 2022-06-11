def solution(a, b):
    days=[31,29,31,30,31,30,31,31,30,31,30,31]
    month_to_day=0
    for i in range(a-1): #월을 일자로 계산
        month_to_day+=days[i]
    total_day= month_to_day+b #일자까지 더하기
    answer=''
    if total_day%7 ==1:
        answer='FRI'
    elif total_day%7 ==2:
        answer='SAT'
    elif total_day%7 ==3:
        answer='SUN'
    elif total_day%7 ==4:
        answer='MON'
    elif total_day%7 ==5:
        answer='TUE'
    elif total_day%7 ==6:
        answer='WED'
    elif total_day%7 ==0:
        answer='THU'
    return answer