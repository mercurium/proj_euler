import time, math
from primes import get_primes, factor_given_pfactor, pfactor_gen, get_divisors_given_pfactor
START = time.time()
SIZE  = 10**8

primesList  = get_primes(SIZE)
pfactorList = pfactor_gen(SIZE)
primeSet    = set(primesList)

def factor(n):
  return factor_given_pfactor(n, pfactorList)

def divisors(n):
  return get_divisors_given_pfactor(n, pfactorList)

answers = set()
for p in primesList:
  divs = divisors(p+1)
  for div1 in divs:
    for div2 in divs:
      if div1 <= div2:
        continue
      top    = ((p+1) * div1) / div2 - 1
      bottom = ((p+1) * div2) / div1 - 1
      if top > SIZE:
        continue 
      if top in primeSet and bottom in primeSet:
        answers.add((top, p, bottom))

print sum([x[0] +x[1] + x[2] for x in answers])
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 518 is correct.

You are the 719th person to have solved this problem.

Answer:     100315739184392
Time Taken: 798.381823063


  10^2: 1035
  10^3: 75019
  10^4: 4225228

"""
