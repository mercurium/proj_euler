import sys
import time
start = time.time()


valz = int(sys.argv[1])

def factor_rec(val, count):
  while(val >= count):
    if val % count == 0:
       return count
    count = count + 1


def factor(val):
  if val == 1:
    return [1]
  temp = factor_rec(val, 2)
  return [temp] + factor(val/temp) 


print factor(valz)[:-1]
print "Time Taken: " + str(time.time()-start)
