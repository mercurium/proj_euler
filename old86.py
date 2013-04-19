import math
import time

start = time.time()

def find_count(maxz):
  square_set = set([])
  for i in range(0,int(maxz * math.sqrt(5) +1) ):
    square_set.add(i**2)
  sq_l = [x**2 for x in xrange(0,maxz*2+1)]
  count = 0
  for i in xrange(1,maxz+1):
    val = i**2
    newset = set([ x - val for x in sq_l])
    newerset = newset.intersection(square_set)
    for num in newerset:
      if num < 4 * val:
        count += (num**.5)//2
  return maxz, count

#for i in range(1,11,1):
#  print find_count(i)

print find_count(100)
print "Time Taken: ", time.time() - start



