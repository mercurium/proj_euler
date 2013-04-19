import math


#generic sieve to get the primes less than 10^6
temp_lst = [0]*10**6
primes_set = set([])
for i in range(2,len(temp_lst)):
  if temp_lst[i] == 0:
    primes_set.add(i)
    for j in range(2*i,len(temp_lst),i):
      temp_lst[j] +=1


#first few primes
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,87,89,97,101]


def rep_sq(n, powz, mod): #same one as from my primes.py file
  if powz == 0: return 1
  if powz == 1: return n % mod
  
  
  val = int(math.log(powz,2))
  lst = [1,n] + [0] * val
  for i in range(2,len(lst)):
    lst[i] = lst[i-1]**2 % mod
  
  pows = [0] * (val+1)
  power = powz
  for i in range(0,len(pows)):
    pows[i] = power % 2
    power = power //2 
  product = 1
  for i in range(0,len(pows)):
    if pows[i] == 1:
      product = product * lst[i+1] % mod
  return product

#http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def miller_rabin(n): 
  if n == 1: return False
  if n in primes_set: return True #doesn't work for n < 3
  
  for i in range(0,len(primes)): #save us some excessive calculations
    if n%primes[i] == 0:
      return False
  
  d,r = n-1, 0
  while d %2 == 0:
    r+=1 
    d/= 2 #We'll have n-1 = 2^r * d
  
  
  if n >= 341550071728321: return -1 #too large of an input for us
  if n < 1373653: lstz = [2,3]
  elif n < 9080191: lstz = [31,73]
  elif n < 4759123141: lstz = [2,7,61]
  elif n < 2152302898747: lstz = [2,3,5,7,11]
  elif n < 3474749660383: lstz = [2,3,5,7,11,13]
  elif n < 341550071728321:  lstz = [2,3,5,7,11,13,17]
  
  for val in lstz: #we need to test every number for our given n
    sq_val = pow(val,d,n)
    if sq_val == 1 or sq_val == n-1:
      return True

    sq_val = sq_val**2 % n
    for i in range(1,r):
      if sq_val == n-1:
        return True
      sq_val = sq_val**2 % n
  return False
  
m_r = miller_rabin
