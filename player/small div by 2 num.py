s,i = map(int,raw_input().split())
for j in range(1,100001):
  if j%s==0 and j%i==0:
    print j
    break
