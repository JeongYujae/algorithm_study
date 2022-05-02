#이코테_7 럭키 스트레이트

n=list(input())
data=list(map(int,n))
sum_x=0
sum_y=0
for x in range(len(data)//2):
  sum_x+=data[x]

for y in range(len(data)//2,len(data)):
  sum_y+=data[y]

if sum_x==sum_y:
  print('LUCKY')
else:
  print('READY')