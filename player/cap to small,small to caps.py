n=input()
for i in n:
  if(i==i.lower()):
    print(i.capitalize(),end="")
  else:
    print(i.lower(),end='')
