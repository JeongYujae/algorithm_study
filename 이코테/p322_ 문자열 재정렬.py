#이코테_8 문자열 재정렬

from string import ascii_uppercase
alpha_list=list(ascii_uppercase)
list_a=[]
list_n=[]
data=input()
for x in data:
  if x in alpha_list:
    list_a.append(x)
  else:
    list_n.append(x)
list_a.sort()
list_n=list(map(int,list_n))

sum=0
for x in list_n:
  sum+=x
print("".join(list_a)+str(sum))
