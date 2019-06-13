l,e=input().split()
l=int(l)
e=int(e)

for i in range(l+1,e):
    t=i
    r=0

    while(t>0):
        e=t%10
        t=t//10
        s=e**3
        r=r+s
        if(i==r):
            print(i,end=' ')
