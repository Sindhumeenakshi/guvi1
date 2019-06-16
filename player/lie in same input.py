d=input().split()
e=input().split()
f=input().split()
if(d[0]==e[0]==f[0] or (d[1]==e[1]==f[1] or (d[0]==d[1] and e[0]==e[1] and f[0]==f[1])):
    print('yes')
else:
    print('no')
