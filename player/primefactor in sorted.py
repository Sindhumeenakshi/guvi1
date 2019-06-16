b=int(input())
m=[]
c=0
for j in range(2,b+1):
  if(b%j)==0:
    m.append(j)
for j in m:
  c=0
  for k in range(1,j+1,1):
    if (j%k)==0:
      c=c+1
  if c==2:
    print (j,end=" ")
