su,i = map(int,raw_input().split())
for k in range(1,100001):
  if k%su==0 and k%i==0:
    print k
    break
