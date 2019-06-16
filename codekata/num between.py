n=int(input())
C=0
l,r=map(int,input().split())
for i in range(l+1,r):
  if(i==n):
    c=1
if(c==1):   
  print("yes")
else:
  print("no")
