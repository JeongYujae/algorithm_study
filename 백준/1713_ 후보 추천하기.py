from collections import defaultdict

n=int(input())
vote=int(input())
data=list(map(int,input().split()))

dic=defaultdict(int) #각각의 후보자: 받은 표 수
photo=[] #사진틀
for x in data: #투표한 것들 하나하나 탐색
    dic[x]+=1 #먼저 누적 count 올리고
    if x in photo:
        continue
    elif len(photo)<n: #사진틀에 자리가 있으면
        photo.append(x)
        
    elif len(photo)==n: #꽉 차 있으면
        tmp=1000 #최대가 천번이니까
        for y in photo: #photo를 하나씩 돌면서
            if dic[y]<tmp: # photo 안에 있는 것들끼리 비교해서
                tmp=dic[y] #작으면 비교 타겟을 변경(최대가 1000이라 1000부터 시작)
                de=y #작은 수 지울 준비
        else:
            photo.remove(de) #만약 비교해서 tmp가 가장 작으면 사진틀에서 지워주기
            del(dic[de])
            photo.append(x)

photo=list(map(int,photo))
photo.sort()
print(*photo) #리스트 떄고 출력하는 방법
                
                
                
            
    


        








# dic[x]+=1
# if dic[x]>=max(picture):