t=int(input())

def solution(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    else:
        return solution(n-1)+solution(n-2)+solution(n-3) #점화식 대입
        #없는 값들은 계속 함수 호출로 값 만들어주기


for i in range(t):
    n=int(input())
    print(solution(n))


