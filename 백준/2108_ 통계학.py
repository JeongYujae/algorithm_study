import sys

n=int(sys.stdin.readline())
data=[]
for i in range(n):
    data.append(int(sys.stdin.readline()))
    
#평균 구하기
print(round((sum(data)/len(data))))

#중앙값
data.sort()
print(data[len(data)//2])

#최빈값
from collections import Counter
freq=Counter(data).most_common() #1. 가장 많이 나온 요소 순, 2. 인덱스순
if len(freq)>1 and freq[0][1]==freq[1][1]:
    print(freq[1][0])
else:
    print(freq[0][0])

#범위
print(max(data)-min(data))
    