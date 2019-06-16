n,m=map(int,input().split())
lis=[]
for i in range(1,m+1):
  if(n%i==0 and m%i==0):
    lis.append(i)
print(max(lis))
