w=8
h=12
a=[1,2,1]
cnt=0
for i in range(h):
    target=i%3
    cnt+=a[target]
answer=(w*h)-cnt