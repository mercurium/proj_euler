import string
import time
start = time.time()



vals = (1,1,2)

count = 4
for i in xrange(500000):
  vals = (vals[1],vals[2],vals[1]+vals[2])
  val = (string.join(sorted(str(vals[2])[:9]), '') == '123456789', string.join(  sorted(  str(vals[2])[-9:]  ), '') == '123456789')
  if val == (True,True):
    print i+count
    break
  if val[0] == True:
    print "Front of ", i+count, "is pan"
  if val[1] == True:
    print "Back of ", i+count, "is pan"
    
print "Time Taken: ", time.time()-start
