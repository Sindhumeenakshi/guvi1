n,e=map(int,input().split())
lis=[int(x) for x in input().split()]
c=0
for i in lis:
  if(i==e):
    c=c+1
print(c)
