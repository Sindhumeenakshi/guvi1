n=int(input())
t=n
r=0
while(n>0):
  e=n%10
  n=n//10
  s=e**3
  r=r+s
if(t==r):
  print("yes")
else:
  print("no")


