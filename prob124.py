import time
start = time.time()
lst = [1]*100001

for i in range(1,len(lst)):
  if lst[i] == 1:
    for j in range(i,len(lst),i):
      lst[j] *= i


for i in range(1,len(lst)):
  lst[i] = (lst[i],str(i))
print lst[:10]
lst = lst[1:]

lst.sort()
val = lst[9999][0]


lst2 = []
for j in range(9990,10010):
  if lst[j][0] == val:
    print j
    lst2 += [int(lst[j][1])]
lst2.sort()
print lst2
print "Time Taken: " + str(time.time()-start)
