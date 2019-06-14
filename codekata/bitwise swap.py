s,m=input().split()
s=int(s)
m=int(m)
s=s^m
m=s^m
s=s^m
print(s, end=' ')
print(m)
