import time
START = time.time()
SIZE  = 45

for x in xrange(0, SIZE+1):
  for y in xrange(0, x+1):
    for z in xrange(0, y+1):
      if x**2 + y**2 + z**2 == SIZE**2:
        print x,y,z
      elif x**2 + y**2 + z**2 > SIZE**2:
        break

print "Time Taken:", time.time() - START
