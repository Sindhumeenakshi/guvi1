nu = int(raw_input())
lis = map(int,raw_input().split())
count = []
for i in range(len(lis)):
  count.append(lis.count(lis[i]))
for i in range(len(count)):
  if count[i] is 1:
    print lis[i]
