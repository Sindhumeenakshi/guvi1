s,r=map(str,input().split())
le=len(S)
a={}
c=0
for V in range(le):
    if(s[V] not in a.keys()):
        a[s[V]]=r[V]
    else:
        if(a[s[V]]==r[V]):
            continue
        else:
            c=1
            break
if(c==1):
    print("no")
else:
    print("yes")
