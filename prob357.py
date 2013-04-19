#Okay, so we know that if there's a square in the number, then it fails. Aka, if n = (d^2)a, then d + n/d = d+ da = d(a+1) = not prime

#It is also necessary for each number to have a factor of 2...
#also any number = -1 mod p doesn't work either... xD

#first few numbers are... 2,6,10,22,30

#got 1739488931516, apparently wrong?
#1739616366215 is right YESSS :D :D :D 
#Time Taken:  897.442189217


import time
from primes import *
from bitarray import bitarray

num_for_small = 200 #the primes we use to do the filtering
small_cap = primes[num_for_small] 
small_cap = small_cap - small_cap %4 + 2


#this is the primes we use in the set of primes to save time
prime_set_lim = 10**6 
size = 10**7 # size of the problem 


#prime set generator
temp_lst = bitarray(prime_set_lim)
prime_set = set([])
for i in range(2,len(temp_lst)):
  if temp_lst[i] == 0:
    prime_set.add(i)
    for j in range(2*i,len(temp_lst),i):
      temp_lst[j] = True
start = time.time()

small_primes=primes[:num_for_small]


#generates the divisors less than sqrt(n)
def half_divisors(n):
   if n == 0: return []
   elif n == 1: return [1]
   else:
      divs = []
      for divisor in range(1, int(math.sqrt(n)+1)):
         if n % divisor == 0:
            divs.append(divisor)
      divs.sort()
      return divs

#we don't even need to check if n is prime since n is even

#if n isn't square free or is -1 mod prime, then we can ignore it.
def div357(n):
  for prime in small_primes:
    if n% (prime**2) == 0 or n% prime == prime-1 or (n/2 + 2 != prime and (n/2 +2)%prime ==0):
      return False
  return True
  
#using this method is not too bad...
def slow_test(n):
  lst = half_divisors(n)
  for num in lst:
    if (num + n/num) < prime_set_lim:
      if (num + n/num) not in prime_set:
        return False
    else:
      if not m_r(num + n/num):
        return False
  return True


#this is just the command to filter the numbers
vals = set([])
test_vals = [1]+range(2,small_cap,4) + filter(div357, xrange(small_cap, size,4))
print len(test_vals)
print "Time Taken: ", time.time() - start


#then we do the actual testing to get rid of numbers that don't work
#for i in ([1]+ xrange(2,10000,4)):
for i in test_vals:
  if slow_test(i):
    vals.add(i)

vals = list(vals)
#vals.sort()
#print vals
print sum(vals), len(vals)

print "Time Taken: ", time.time() - start


#The filter removes all but 767,642 of the numbers out of 10^8 choices...
#my program says that there's a total of ____ numbers included, for a total sum of ______ and a running time of ________


