a = input()
y=0
for j in a:
    if j.isdigit():
        y=y+1
if y == len(a):
    print("yes")
else:
    print("no")
