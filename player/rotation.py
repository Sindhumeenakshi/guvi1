i = list(map(int,input().split()))
j = list(map(int,input().split()))
for k in range(0,len(a2)):
    print(j[(((len(j)-i[1])+k)%len(j))],end=' ')
