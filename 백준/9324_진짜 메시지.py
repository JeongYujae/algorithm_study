n=int(input())
for i in range(n):
    word=input()
    # text: 각각의 알파벳 숫자 count 디폴트는 ok
    text,result=[0 for _ in range(26)], 'OK'
    # flag는 
    flag= False
    for i in range(len(word)):
        # flag가 true 라면 false로 바꿔두고 count 올려주기
        if flag:
            flag= False
            continue
        text[ord(word[i])-65]+=1
        # 같은 알바펫이 3개일때
        if text[ord(word[i])-65]==3:
            # i가 마지막 글자 -> fake(3개가 되었는데 그 위치가 마지막이면)
            if i == len(word)-1:
                result='FAKE'
                break
            # 3개면 다음 글자와 같아야되는데, 아니라면 -> fake
            elif word[i]!=word[i+1]:
                result='FAKE'
                break
            # 3개가 되었으면 flag를 true로 변경, count 초기화
            flag= True
            text[ord(word[i])-65]=0
    print(result)
     