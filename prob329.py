import time
start = time.time()
from bitarray import bitarray

primes = bitarray('11'+'0' *499)
for i in xrange(2,501):
  if primes[i] == 0:
    for j in xrange(2*i,501,i):
      primes[j] = 1


seq = bitarray('000011000100101')
squares = [0] + [1] * 500
new = [0] * 501
div = 3**15 * 500 * 2**15


for i in xrange(0,15):
  new[2] += squares[1]*2
  new[499] += squares[500]*2
  for j in xrange(2,500):
    new[j-1] += squares[j]
    new[j+1] += squares[j]
  
  for j in xrange(1,501):
    if seq[i] == primes[j]:
      new[j] *= 2
  squares = new[:]
  new = [0]*501

a = sum(squares)
while a %2 == 0:
  a /=2
  div /=2  
print str(a) + '/' + str(div)

print "Time Taken:", time.time() - start
