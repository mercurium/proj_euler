import time
from math import sqrt
start = time.time()

limit = 50
sqs = {}
for a in range(3, limit):
  for b in range(a%2+2,a,2):
    n = (a**2 + b**2)/2
    m = (a**2 - b**2)/2
    if n in sqs and m in sqs:
      sqs[n] += 1
      print a**2,b**2
    else: sqs[n] = 1

for key in sqs.keys():
  if sqs[key] > 1:
    print key
    
print "Time Taken: " + str(time.time()-start)
