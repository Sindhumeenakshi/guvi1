lis=[str(x) for x in input()]
if(lis[0]=='(' and lis[-1]==')'):
    if(lis.count('(')==lis.count(')')):
        print("yes")
    else:
        print("no")
else:
    print("no")
