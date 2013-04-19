import math
import time
start = time.time()

def prime357(n):
  if n % 3 == 0 or n% 5 == 0 or n%7 == 0:
    return False
  return True


limit = 10**6

lst = [2,3,5,7] + filter(prime357,xrange(11,limit))


print "Time Taken: ", time.time() - start

lst = [0]* 10**6
prime_set = set([])
for i in range(2,len(lst)):
  if lst[i] == 0:
    prime_set.add(i)
    for j in range(2*i,len(lst),i):
      lst[j]+= 1


prime_lst = list(prime_set)







print "Time Taken: ", time.time() - start
