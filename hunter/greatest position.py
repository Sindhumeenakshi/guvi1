
i,j=map(int,input().split())

s=[int(x) for x in input().split()]
s.sort()
for k in range(len(s)):
  if(k==(i-j)):
    print(s[k])
    break
