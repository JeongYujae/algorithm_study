#5800
x = int(input())

for i in range(x):
    data = list(map(int, input().split())) # 한 줄씩 받은 데이터를 바탕으로 data 구성, 하고 print
    del data[0] #필요없다고 생각하여 데이터의 길이값 삭제
    data.sort() #내림차순 정렬
    answer = []
    print('Class', i+1)
    # 성적을 내림차순으로 정렬했을 때 가장 큰 인접한 점수 차이구하는 for문
    for i in range(len(data)-1):
        answer.append(data[i+1] - data[i])
    # 하나하나 문제에서 요구하는 식 제대로 구현
    print('Max', str(max(data))+',' ,'Min', str(min(data))+',', 'Largest gap', max(answer))

















# import sys
# k=int(input()) #전체 반의 개수
# data=[]
# for _ in range(k): #input 받은 데이터를 2차원 리스트 형태로 가져옴
#     data.append(list(map(int,sys.stdin.readline().split())))

# num=1
# for x in data:
#     x.sort()
#     print(f'Class {num}')
#     print('Max',max(x),',','Min',min(x),',','Largest gap')
#     num+=1
