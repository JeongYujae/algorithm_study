# data=input() #전체 문자열
# goal=input() #찾고자 하는 문자열
# count=0

# #goal의 길이를 단위로 해서 0번 인덱습부터 goal의 길이만큼 더한 만큼 탐색
# for i in range(0,(len(data)-len(goal))):
#     if data[i:(i+len(goal))]==goal:
#         count+=1

#     print(data[i:(i+len(goal))], count)

###########################################오류 코드#################################################################

#if문이 맞으면, count +=1 후에 문자열을 넘겨줘야됨
#if문이 틀리면, 그대로 for문을 유지


data=input() #전체 문자열
goal=input() #찾고자 하는 문자열
count=0 
x=0 #for문에서의 범위를 컨트롤 할 수 없기에, while 문을 이용
 
while x<= len(data) - len(goal): #최대길이
    if data[x:x+len(goal)] ==goal:
        count+=1
        x+=len(goal) #x를 임의로 문자열의 길이만큼 증가-> 
                     #즉 위 코드에서의 문자열의 인덱스 번호를 넘겨주는걸 가능케
    else:
        x+=1 #그대로
print(count)