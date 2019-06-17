s,r=map(int,input().split())
lis=[int(x) for x in input().split()]
c=0
for i in lis:
  if(i==r):
    c=1
if(c==1):print("Yes")
else:
  print("No")
