a,b=map(int,input().split()) 
e=input()
n=list(map(int,input().split()))
H=list(map(int,input().split()))
b=[]
for i in range(b):
    n.append(H[i])
    b.append(max(n))
print(*b)
