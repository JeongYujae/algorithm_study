def solution(nums):
    from itertools import combinations
    data=list(map(sum,list(combinations(nums,3))))
    count=0
    for x in data:
        prime=0
        for i in range(2,x):
            if x%i==0:
                prime=1
        if prime==0:
            count+=1
    answer=count
    return answer