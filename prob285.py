#NOTE TODO need to solve it
import time
start = time.time()
from math import pi

score = 0
for i in xrange(1,11):
  prob = pi*( ((i-.5)**2 - (max(i-1.5,0))**2)/i**2)/4
  score += prob * i
  print prob, score

print score
print "Time Taken: ", time.time() - start
