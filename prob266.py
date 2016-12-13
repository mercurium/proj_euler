#NOTE TODO need to solve it
import time
START = time.time()
from primes import factor, get_primes, primes


prime_list = primes[:42]

# [::-1] ############# reversing the list of primes so that we add bigger items on first.
prime_list = prime_list[::-1]
print prime_list, len(prime_list)

prod = [1]
for prime in prime_list:
  prod.append(prod[-1] * prime)

PROD_LIM = [int(p**.5) for p in prod]

def recurse(prod, pos, prime_lst,lim, ratio):
  if prod > lim:
    return -1
  if pos == len(prime_lst):
    return prod


  ###### Attempting to short cut out of any solutions that aren't optimal... =/...
    prod2 = prod
    for i in prime_lst[pos:] :
        prod2 *= i
    if prod2*1.0 / lim < ratio:
        return -1


  no_add = recurse(prod,pos+1, prime_lst, lim, ratio)
  added =  recurse(prod * prime_lst[pos], pos+1,prime_lst, lim, ratio)

  val_no_add, val_add = lim - no_add, lim - added
  if val_no_add < val_add:
    return no_add
  return added

ratio = .5
for iteration in xrange(1,len(PROD_LIM)):
  ans = recurse(1,0, prime_list[:iteration],PROD_LIM[iteration], ratio)
  print "The optimal answer is:", PROD_LIM[iteration], prime_list[iteration-1], iteration
  print "The answer is:", ans, factor(ans)
  print "The new ratio is:", ratio
  print "Time now is:", time.time() - START, '\n'
  ratio = ans*1.0/PROD_LIM[iteration]


print "Time Taken:", time.time() - start
