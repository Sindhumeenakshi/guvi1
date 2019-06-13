n=int(input())
s=[int(i) for i in input().split()]
s.sort()
e=s[int(n/2)]
print(e)
