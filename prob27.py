from primes import *

true, false = True, False
#we know that since n^2+an+b = prime has to include the 0 case
#b has to be positive and prime. Also n has to be odd or else:
#we get odd *odd + odd*even + odd = even = not prime

#Time Taken: 9.46837615967


import time
start = time.time()

a_lst = range(-1,-1000,-2)
b_lst = primes[12:168]


a_lst2 = []
b_lst2 = []

max = 0
for a in a_lst:
  for b in b_lst:
    if b > 1000:
      print 'rawr'
      break
    n = 1
    while True:
      if n**2 + n*a + b < 0:
        break
      elif not mr(n):
        n+=1
      elif mr(n**2 + n*a + b):
        n+=1
      else: break
    if 40 < n: 
      max = n-1
      print max, a, b
      a_lst2 += [a]
      b_lst2 += [b]

print 'ON TO PHASE 2. YAY!'
max = 0
for i in range(0,len(a_lst2)):
  n = 1
  while n < 80:
    if mr(n**2 + n*a_lst2[i] + b_lst2[i]):
      n+=1
    else:
      print n
      break
  if max < n-1:
    max = n-1
    print max, a_lst2[i], b_lst2[i]


print max

print "Time Taken: " + str(time.time()-start)
