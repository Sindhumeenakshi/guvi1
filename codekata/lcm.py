l,m=map(int,input().split())

if(l>m):
    min1=l
else:
    min1=m
while(1):
    if(min1%l==0 and min1%m==0):
        print(min1)
        break
    min1=min1+1
