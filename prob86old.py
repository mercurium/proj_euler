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
    for j in xrange(1,i+1):
      for k in xrange(1,j+1):
        big = i
        small = j+k
        if (sq_l[small]+sq_l[big]) in square_set:
          count +=1
          print i,j,k
        if count >= 10**6:
          return i,count
  return maxz, count

for i in range(1,11,1):
  print find_count(i)

#print find_count(200)
print "Time Taken: ", time.time() - start



