m=input()
a=m[0]
for i in m:
    if (m.count(a)<m.count(i)):
        a=i
print(a)
