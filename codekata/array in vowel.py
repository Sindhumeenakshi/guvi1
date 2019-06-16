lis=[str(x)  for x in input()]
li=['a','e','i','o','u']
c=0

for i in lis:
  if(i in li):
    c=1
if(c==1):
  print("yes")
else:
  print("no")
