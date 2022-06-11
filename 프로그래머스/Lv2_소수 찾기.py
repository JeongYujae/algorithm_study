def solution(numbers):
    from itertools import permutations
    numbers=list(numbers) #str형을 각 문자로 쪼개기
    data=[]
    for i in range(1,len(numbers)+1): #모든 경우의 수 구하기
        data.append(list(map(''.join, permutations(numbers,i))))
    data=list(map(int,sum(data,[]))) #sum~~ 2차원 리스트 -> 1차원 리스트
    data=set(data) #중복 제거
    answer=[]
    for n in data:                    
        if n < 2:                                
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1): #제곱근보다 작은 숫자까지 나누고
            if n % i == 0: #나눠떨어지는게 있으면
                check = False
                break
        if check: #없으면 소수!
            answer.append(n)
    return len(set(answer))