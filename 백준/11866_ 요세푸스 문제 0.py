# n,k=map(int,input().split())
# data=[]
# for x in range(n):
#     data.append(x+1)

# #원형이라는 조건 -> index로 접근이 아닌 data가 계속 순환 해야만 해


# while len(data)>1:
#     cur=1

#     if cur==k:
#         data.pop(k)
#     else:
#         cur+=1

#######################################################

from collections import deque #deque라는 쌍방향 outlet을 가진 특수한 자료구조

data = deque()
answer = []

n, k = map(int, input().split())

for i in range(1, n+1): #1부터 n까지 숫자 만들어주고
    data.append(i)

while data: #while data=True
    for i in range(k-1): #지우고싶은 수 전까지
        data.append(data.popleft()) #popleft ->왼쪽에서부터 데이터를 지우는 함수
        #지운 데이터들을 data에 추가해주고
    answer.append(data.popleft())
    #answer에는 지울 값을 추가해준다

print("<",end='')
for i in range(len(answer)-1): #마지막 남는 수는 배제
    print("%d, "%answer[i], end='')
print(answer[-1], end='') #마지막 남은 수는 range로 계산할 수 없으니까 따로 계산해줌
print(">")



