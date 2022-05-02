from string import ascii_uppercase

n=int(input())
alpha=list(ascii_uppercase)
# c_data=[]
# for _ in range(n):
#     data=input()
#     for x in alpha:
#         c_data.append(data.count(x))
#     print(c_data)
d=[0]*26
for _ in range(n):
    data=list(input())
    data_n=data
    for x in data:
        d[ord(x)-95]+=1
        if d[ord(x)-95] ==3:
            data[int(d[ord(x)-95] ==3)+1]

            
    

    