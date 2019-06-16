si=int(input())
if si>0:
  for x in range(2,si):
    if(si%x==0):
      print("no")
      break
  else:
      print("yes")
else:
  print("no")
