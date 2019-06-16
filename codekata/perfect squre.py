s,r=map(int,input().split())
d=s*r
for i in range(0,d+1):
  if(i**2==d):
    print('yes')
    break
else:
  print('no')
