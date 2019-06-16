n,m=map(int,input().split())
def gcd(n,m):
    if(m==0):
        return n
    else:
        return gcd(m,n%m)
r=gcd(n,m)
print(r)
