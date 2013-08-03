import time
import string
start = time.time()


items = set()
for i in xrange(1,10):
  for j in xrange(123,9876):
    n = str(i) + str(j) + str(i*j)
    if string.join(sorted(str(n)),'') == '123456789':
      items.add(i*j)
      print i, j, i*j

for i in xrange(1,99):
  for j in xrange(123,988):
    n = str(i) + str(j) + str(i*j)
    if string.join(sorted(str(n)),'') == '123456789':
      items.add(i*j)
      print i, j, i*j
print sum(items)
print "Time taken: " + str(time.time()-start)
