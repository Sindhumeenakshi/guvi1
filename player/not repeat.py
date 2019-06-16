nu = int(raw_input())
lis = map(int,raw_input().split())
count = []
for j in range(len(lis)):
  count.append(lis.count(lis[j]))
for j in range(len(count)):
  if count[j] is 1:
    print lis[j]
