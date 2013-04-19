size = 10**6
sumz = 0
lst = range(size+1)
for i in xrange(2,len(lst)):
  if lst[i] == i:
    for j in xrange(i,len(lst),i):
      lst[j] = (i-1)*lst[j]/i
