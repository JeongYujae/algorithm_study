import itertools
import sys
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num=list(itertools.permutations(n,3)) #순열로 3개씩 뽑기

a=int(sys.stdin.readline())

for _ in range(a):
    t,s,b=map(int,sys.stdin.readline().split())
    t=list(str(t)) #int 형은 list로 변환이 불가능!
    removed_count=0

    for i in range(len(num)):
        strike=ball=0
        i-=removed_count # num 0부터 조회/ 만약 제거되어서 removed_count가 올라간다면 그 수 만큼 빼줘서
                         # 완전 탐색진행
        for j in range(3):
            t[j]=int(t[j])
            if t[j] in num[i]:
                if j==num[i].index(t[j]):
                    strike+=1
                else:
                    ball+=1

        if (strike !=s) or (ball !=b): #위의 반복문을 돌고난 후에 
            num.remove(num[i])         #입력받은 strike과 ball이 다르면 -> 제거해줌(경우의 수에 해당이 안되기 때문에)
            removed_count+=1       
print(len(num))                        




