n,e=map(int,input().split())
lis=[int(x) for x in input().split()]
c=0
for i in lis:
  if(i==e):
    c=1
  
if(c==1):
  print("yes")
else:
  print("no")
