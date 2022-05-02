data=[]
while True:
    word=input()
    if word=='0':
        break
    else:
        data.append(word)

for x in data:
    if x==x[::-1]:
        print('yes')
    else:
        print('no')
