#generic sieve to get the primes less than 10^6
temp_lst = [0]*10**6
primes_set = set([])
for i in xrange(3,len(temp_lst),2):
  if temp_lst[i] == 0:
    primes_set.add(i)
    for j in xrange(3*i,len(temp_lst),i*2):
      temp_lst[j] =1
del temp_lst


#http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
#This algorithm can be extended beyond what I have here but I rarely see the need for it so I didn't bother.
def miller_rabin(n):
  if n == 1: return False
  if n in primes_set: return True #doesn't work for n < 3
  
  for i in range(0,len(primes)): #save us some excessive calculations
    if n%primes[i] == 0:
      return False

  if n == 2 or n == 3: return True
  d,r = n-1, 0
  while d %2 == 0:
    r,d = r+1,d/2 #We'll have n-1 = 2^r * d
  
  if n >= 3825123056546413051: return -1 #too large of an input for us
  if n < 1373653: lstz = [2,3]
  elif n < 9080191: lstz = [31,73]
  elif n < 4759123141: lstz = [2,7,61]
  elif n < 2152302898747: lstz = [2,3,5,7,11]
  elif n < 3474749660383: lstz = [2,3,5,7,11,13]
  elif n < 341550071728321:  lstz = [2,3,5,7,11,13,17]
  elif n < 3825123056546413051: lstz = [2,3,5,7,11,13,17,19,23]

  def try_composite(a):
    val = pow(a,d,n)
    if val == 1:
      return False
    for i in range(r):
      if val == n-1:
        return False
      val = pow(val,2,n)
    return True # n is definitely composite
 
  for a in lstz:
    if try_composite(a):
      return False
 
  return True 
  
m_r = miller_rabin

