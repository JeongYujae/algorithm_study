data=[] 
num=666 #최소값이 666이니까
n=int(input()) 

while True: #무한반복
    if '666' in str(num): #문자열로 바꾸고 '666'이 연속으로 있다면
        data.append(num) #조건에 만족하니까 -> data에 추가
    if len(data)==n: #원하는 번째의 수가 나오면
        print(data[-1]) #가장 최근에 추가된 값 반환
        break #while 문 끊어주고
    num+=1 #카운트를 올려준다
        
    