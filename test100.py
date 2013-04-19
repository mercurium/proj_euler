import time
from math import sqrt

start = time.time()
N = 1000000
m = sqrt(2)/2. #m for multiplier

i = 2
while True:
  a = int(m *i)
  if (a*(a+1)*2) == i*(i-1):
    print a+1, i
  i+=1

print "Time Taken: " + str(time.time() - start)

