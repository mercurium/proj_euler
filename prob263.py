#NOTE TODO need to solve it
import time
from primes import pfactor_gen, factor_given_pfactor, get_divisors_given_pfactor
START = time.time()

SIZE = 10**6
pfactor = pfactor_gen(SIZE)

def factor(n):
  return factor_given_pfactor(n, pfactor)

def get_divisors(n):
  return get_divisors_given_pfactor(n, pfactor)

# This function is currently very slow for numbers with lots of factors =/
def practical_check(n):
  divs     = get_divisors(n)
  div_sums = set([0])
  for val in divs:
    div_sums.update(set([ val + num for num in div_sums]))

  div_sums = sorted(div_sums)[:n+1]
  print "On item:", n, "Time up to now:", time.time() - START
  return div_sums == range(n+1)
pc = practical_check


items = []
for i in xrange(21,SIZE-18,2):
  if pfactor[i] == i and pfactor[i+6] == i+6 and \
  pfactor[i+12] == i+12 and pfactor[i+18] == i+18:
    items += [i+9]
    #print i,i+6,i+12,i+18

print "Out of", SIZE, "items, there were", len(items), "which were prime-triples"

sumz = 0
count = 0
for item in items:
  n = item
  if all([pc(k) for k in xrange(n-8,n+9,4)]):
    count += 1
    sumz  += item
    print item
  if count == 4:
    break

print sumz
print "Time Taken:", time.time() - START



"""
These are some of the sets of 5 practical numbers
8 12 16 20 24
12 16 20 24 28
16 20 24 28 32
20 24 28 32 36
24 28 32 36 40
96 100 104 108 112
192 196 200 204 208
608 612 616 620 624
1472 1476 1480 1484 1488
2544 2548 2552 2556 2560
4088 4092 4096 4100 4104
8528 8532 8536 8540 8544
15088 15092 15096 15100 15104


"""
