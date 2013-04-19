import time
import string
start = time.time()
from itertools import product
import string
#strategy i was going for was to try all numbers less than 1 billion and see if it had even digits... obviously not the best choice xD.

odds = set()
for dig in xrange(0,3):
  for i in product('13579',repeat = dig):
    odds.add(string.join(i,''))
for i in product('13579',repeat= ):
  odds.add('1'+string.join(i,''))

print len(odds)
print "Time Taken: " + str(time.time()-start)
def dig_check(n):
  return n in odds

"""
count = 0
for j in xrange(0,3):
  for i in xrange(10**j,10**(j+1)):
    if i % 10 != 0:
      n = str(i + int(str(i)[::-1]))
      if dig_check(n):
        print i
        count += 1
  #print count, 10**(j+1)

print "Time Taken: " + str(time.time()-start)
"""
