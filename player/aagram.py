q=int(input())
d=0
i=[]
for u in range(q):
    i.append(input())
for u in range(q):
    if sorted(i[u])==sorted('kabali'):
        d=d+1
print(d)        
