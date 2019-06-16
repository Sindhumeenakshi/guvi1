b= int(input())
if(b>1):
  for j in range(2,b):
    if (b%j==0):
      print ("yes")
      break
  else:
    print ("no")
else:
  print ("no")
