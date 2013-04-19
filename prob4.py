import string
import time
start = time.time()

def reverse(num):
  return int(str(num)[::-1])

for a in range(999, 900, -1):
  for b in range(999,a,-1):
    c = a * b
    if  reverse(c) == c:
      print c, a, b
      break

print "Time Taken: " + str(time.time()-start)
