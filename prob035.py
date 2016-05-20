import time
from bitarray import bitarray
START = time.time()
SIZE = 10**6


def rot_check(item):
  j = len(str(item))  
  for i in xrange(0,j):
    if prime_checking_lst[item/10**i + (item % 10**i)*(10**(j-i))] != 0: # Checking if all of the rotations are prime
      return False
  return True

prime_checking_lst = bitarray('0' * SIZE) 

count = 0
for i in xrange(2,len(prime_checking_lst)): #this marks the nonprimes
  if prime_checking_lst[i] == 0:
    for j in xrange(i**2,len(prime_checking_lst),i):
      prime_checking_lst[j] = 1 #prime_checking_lst[j] is marked as not prime

for i in xrange(2,len(prime_checking_lst)):
  if prime_checking_lst[i] == 0 and rot_check(i):
    count+=1
print count
print "Time Taken:", time.time() - START
