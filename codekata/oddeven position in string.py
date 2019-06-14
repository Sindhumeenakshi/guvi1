n=(input())
n=list(n)
n[::2],n[1::2]=n[1::2],n[::2]
print(*n,sep='')
