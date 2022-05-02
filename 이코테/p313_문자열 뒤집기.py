#이코테 _3 문자열 뒤집기

s=list(input())
count=0
for x in range(len(s)-1):
  if s[x]!=s[x+1]:
    count+=1
print((count+1)//2)