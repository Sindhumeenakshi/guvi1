a= int(input())
lis=['a','e','i','o','u','A','E','I','O','U']
n = input()
for j in range(0,len(lis)):
    n= n.replace(lis[j],'')
print(n[::-1])
