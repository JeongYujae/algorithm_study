def solution(orders, course):
    from collections import Counter
    from itertools import combinations
    answer=[] #추천하는 메뉴 조합을 담을 리스트
    for i in course: #원하는 조합의 숫자를 하나씩 돌면서
        result=[]
        for menu in orders: #각각의 주문 메뉴 하나씩 접근
            for x in combinations(menu,i): #combinations의 경우로 각각을 x로 돌게 하고
                r=''.join(sorted(x)) #쉼표 제거 + 정렬한 상태로
                result.append(r) # 리스트에 추가
        counter=Counter(result).most_common() 
        for menu,num in counter:
            if num>1 and num==counter[0][1]: #최대 값과 같다면
                answer.append(menu)
    return(sorted(answer))
            