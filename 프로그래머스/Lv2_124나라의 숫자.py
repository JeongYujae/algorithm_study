def solution(n):
    nation_124=[1,2,4]
    answer=''
    while n>=1:
        n=n-1
        answer=str(nation_124[n%3]) + answer
        n=n//3
    return answer