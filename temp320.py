#solve n/p+n/p^2 +... + n/p^k >= 1234567890 for all p < m for m in range 10 to size...
#or equivalently... n(1/p+1/p^2+1/p^3+...)
#(1/p + 1/p^2 + 1/p^3 + ... ) = 1/(p-1)
#so we can use n = val / (1/p + 1/p^2 + 1/p^3 + ... etc)
# ---> n = val / (1/(p-1) ) --> n = val * (p-1) + stuff to be 0 mod p


import time
from bitarray import bitarray
start = time.time()

val = 1234567890
sumz = 0
size = 10**3

prime_set = set([])
lst = bitarray('0'*(size +1))
for i in xrange(3,len(lst),2):
  if lst[i] == 0:
    prime_set.add(i)
    for j in range(2*i,len(lst),i):
      lst[j]= 1
prime_lst = list(prime_set)
prime_lst.sort()

print "Time Taken:", time.time()- start

def cfp(p,val): #cfp = compute for prime
  valz = val * (p-1)
  valz += (p - valz) % valz
  comp = 0
  counter = p
  while counter <= valz
    comp += valz/counter
    counter *= p
  if comp == val: return valz
  valz += (val-comp) * p# - ((val-comp)/p) * p
  
  return valz


def cfp2(n, val): #compute for power of 2
  sumz,comp = 0,2
  while comp < n:
    sumz += n/comp
    comp *= 2
  return sumz * val + sumz * val %2


#3,4  5,6  7,8,9,10  11,12  13,14,15,16
sumz = 0
for i in xrange(0,len(prime_lst)):
  #this is the last prime that we have to deal with
  if i == len(prime_lst)-1: 
    sumz += (size - prime_lst[i]+1) * cfp(prime_lst[i],val)
    print prime_lst[i], size - prime_lst[i]+1
  else: #otherwise we're not done yet... :[
    sumz += cfp(prime_lst[i],val) * (prime_lst[i+1]-prime_lst[i])
    print prime_lst[i], prime_lst[i+1] - prime_lst[i]
sumz = sumz - (2*cfp(3,val) + 2* cfp(5,val) + 3*cfp(7,val))

print sumz
print "Time Taken:", time.time()- start
