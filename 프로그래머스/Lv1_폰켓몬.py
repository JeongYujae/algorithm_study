def solution(nums):
    answer = 0
    n= len(nums)/2
    nums=list(set(nums))
    if len(nums)>=n:
        answer=n
    elif len(nums)<n:
        answer=len(nums)
    return answer