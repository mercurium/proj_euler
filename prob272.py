#NOTE TODO need to solve it
import time, math
from primes import get_primes, factor

START      = time.time()
MAX_SIZE   = 10**11
LIM        = MAX_SIZE / (7*13*19*9)

prime_lst  = get_primes(LIM)
prime_lst  = sorted([9] + filter( (lambda x: x % 3 == 1), prime_lst))
other_nums = range(LIM)

for prime in prime_lst:
  for i in xrange(prime, len(other_nums), prime):
    other_nums[prime] = 0

def test(n):
  return sum(filter(lambda x: x==1, [x**3 % n for x in xrange(n)]))

def getAnswer(currentProd, currentIndex, numLeft):
  if numLeft == 0:
    return currentProd * sum(other_nums[1:MAX_SIZE/currentProd + 1])

  sumz = 0
  for index in xrange(currentIndex, len(prime_lst)):
    if currentProd * prime_lst[index]**numLeft > MAX_SIZE:
      break
    if currentIndex == 0:
      print index

    currentPrime = prime_lst[index]
    if currentPrime != 9:
      for i in xrange(1, int(math.log(MAX_SIZE / currentProd, currentPrime) + 1 )):
        sumz += getAnswer(currentProd * currentPrime**i, index + 1, numLeft - 1)
    else:
      for i in xrange(2, int(math.log(MAX_SIZE / currentProd, 3) + 1 )):
        sumz += getAnswer(currentProd * 3**i, index + 1, numLeft - 1)

  return sumz

print len(prime_lst)
print getAnswer(1,0,5)


print "Time Taken:", time.time() - START

"""
Answer: 13157952743404478203  ? Maybe..

Need to have 5 numbers, 9, or a prime = 1 mod 3, and any number of powers on them.


"""
