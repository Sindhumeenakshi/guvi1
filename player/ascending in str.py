li=[x for x in input().split()]
li.sort()
li.sort(key=len)
print(*li,end=" ")
