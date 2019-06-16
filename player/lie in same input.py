s,r=map(int,input().split())
a,b=map(int,input().split())
q,r=map(int,input().split())
if s==r or a==b or q==r:
    print("yes")
elif s==a==q or r==b==r:
    print("yes")
else:
    print("no")
