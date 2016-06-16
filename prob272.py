#NOTE TODO need to solve it
import time
from primes import get_primes, factor

START      = time.time()
MAX_SIZE   = 10**11
LIM        = MAX_SIZE / (7*13*19*31)

prime_lst  = get_primes(LIM)
prime_lst  = filter( (lambda x: x % 3 == 1), prime_lst)
other_nums = range(LIM)

for prime in prime_lst:
  for i in xrange(prime, len(other_nums), prime):
    other_nums[prime] = 0

def test(n):
  return sum(filter(lambda x: x==1, [x**3 % n for x in xrange(n)])) == 3


SIZE = 1000
count = [0] * 6
for i in xrange(4,SIZE):
  if test(i):
    #print i, factor(i)
    count[i%6] += 1

print count, len(filter(lambda x: x < SIZE, prime_lst))

print len(prime_lst)

sumz       = 0
loop_count = 0

for a in xrange(len(prime_lst)):
  break
  item1 = prime_lst[a]
  if item1**5 > MAX_SIZE:
    break
  for b in xrange(a+1,len(prime_lst)):
    item2 = prime_lst[b]
    if item1*item2**4 > MAX_SIZE:
      break
    for c in xrange(b+1,len(prime_lst)):
      item3 = prime_lst[c]
      if item1 * item2 * item3**3 > MAX_SIZE:
        break
      for d in xrange(c+1,len(prime_lst)):
        item4 = prime_lst[d]
        if item1 * item2 * item3 * item4**2 > MAX_SIZE:
          break
        for e in xrange(d+1,len(prime_lst)):
          item5 = prime_lst[e]
          prod  = item1 * item2 * item3 * item4 * item5
          if prod >= MAX_SIZE:
            break
          sumz       += prod * sum(other_nums[:MAX_SIZE/prod+1])
          loop_count += MAX_SIZE/prod
          #print item1, item2, item3, item4, item5, MAX_SIZE/prod
  print a, item1, loop_count
print sumz, loop_count



print "Time Taken:", time.time() - START
