#so the method of finding if something is square free is pretty simple. If it doesn't divide any of the primes less than n/2, then that number is square free. We could probably do better by eliminating some numbers, but this is good enough for now

import time
import math

start = time.time()

#2,3,5,7,11,13,17,19,23 squared
prime_sqz = [4,9,25,49,121,169,289,361,529]

def sq_free(n):
  for prime in prime_sqz:
    if n % prime == 0:
      return False
  return True


size = 51

lst = [[1]*(x+1) for x in range(0,51)]

for i in range(1,len(lst)):
  for j in range(0,i):
    if j != 0 and j != len(lst[i])-1:
      lst[i][j] = lst[i-1][j]+lst[i-1][j-1]
print "time taken: " + str(time.time()-start)

answer = set([1])
for i in range(1,len(lst)):
  for j in range(1,len(lst[i])-1):
    if sq_free(lst[i][j]):
      answer.add(lst[i][j])

print sum(answer)
print "time taken: " + str(time.time()-start)





