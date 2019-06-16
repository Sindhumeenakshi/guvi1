s=input()
r=[]
for i in s:
  if(i.isnumeric()):
    r.append(i)
print(*r,sep='')
