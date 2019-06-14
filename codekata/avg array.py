n=int(input())
li=[int(i) for i in input().split()]
s=0
for j in li:
  s=s+j
k=s//n
print(k)
  
