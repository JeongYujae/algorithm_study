# n=int(input())
# #word에 input값 추가하기
# word=[]
# for _ in range(n):
#     word.append(str(input()))


# word=list(set(word)) #중복 제거
# word=sorted(word, key = lambda x : len(x)) #lambda 함수로 len을 기준으로 정렬
# print(word)
# answer= "".join(sorted(word))
# print(word)


import sys
n=int(sys.stdin.readline())

data=[]
for i in range(n):
    data.append(sys.stdin.readline().strip())

s_data=set(data) #중복 제거 set -> dict 형태로
answer=list(s_data) #리스트 형태로 변환
answer.sort() #알파벳 순으로 먼저 정렬
answer.sort(key= len)

for x in answer:
    print(x)