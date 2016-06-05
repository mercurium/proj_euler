import time, math
from primes import m_r, findNumLessThan
START = time.time()
SIZE  = 10**11

RELEVANT_SIZE = SIZE / 21125 # 21125 = 5^3 x 13^2

oneMod4Primes   = filter(lambda x: m_r(x), xrange(5,RELEVANT_SIZE+1,4))
threeMod4Primes = [2] + filter(lambda x: m_r(x), xrange(3,RELEVANT_SIZE+1,4))

large3Mod4PrimesIndex = findNumLessThan(threeMod4Primes, RELEVANT_SIZE**.5)
threeMod4Products     = set([1] + threeMod4Primes[large3Mod4PrimesIndex+1:])

for p in threeMod4Primes[large3Mod4PrimesIndex:0:-1] + [2]:
  for power in xrange(1,int(math.log(RELEVANT_SIZE,p)+1)):
    threeMod4Products = threeMod4Products.union( \
      filter((lambda x: x < RELEVANT_SIZE), \
             [ x*p**power for x in threeMod4Products]))

threeMod4Products = sorted(threeMod4Products)

def compute(power1,power2, power3=0):
  sumz = 0
  for prime1 in oneMod4Primes:
    if prime1**power1 * 5**power2 > SIZE:
      break
    for prime2 in oneMod4Primes:
      #print prime1, prime2, prime1**power1*prime2**power2
      if prime1 == prime2:
        continue
      if prime1**power1 * prime2**power2 > SIZE:
        break

      if power3 != 0:
        for prime3 in oneMod4Primes:
          if prime3 == prime1 or prime3 == prime2:
            continue
          if prime1**power1 * prime2**power2 * prime3**power3 > SIZE:
            break
          product      = prime1**power1 * prime2**power2 * prime3**power3
          numThatWork  = findNumLessThan(threeMod4Products, SIZE/product)
          sumz        += product * sum(threeMod4Products[:numThatWork+1])
      else:
        product      = prime1**power1 * prime2**power2
        numThatWork  = findNumLessThan(threeMod4Products, SIZE/product)
        sumz        += product * sum(threeMod4Products[:numThatWork+1])
  return sumz

sumz  = compute(10,2) + compute(7,3) + compute(3,2,1)
print "Answer:", sumz
print "Time Taken:", time.time() - START
"""
(1,2,3), (10,2), (7,3)


Congratulations, the answer you gave to problem 233 is correct.

You are the 1445th person to have solved this problem.

You have earned 1 new award:

  Fibonacci Fever: Solve the first twelve Fibonacci numbered problems


jchen@jchen-mbp 0:14:00 ~/Developer/proj_euler(master) % pypy -i prob233new.py
Answer: 271204031455541309
Time Taken: 8.02545189857

Okay, for this problem, very many important things to note:
  - a circle of radius N intersects with a point (a,b) iff a^2+b^2 = N^2 (pretty elementary)

  - right triangles of the form a^2+b^2=c^2 can be represented as:
    a = k(m^2-n^2)
    b = k(2mn)
    c = k(m^2+n^2)
    so all N must be a sum of squares

  - If (a,b) is a solution, so is (a,-b), (-a,b), (b,a), ...etc (8 solutions per pair a,b)

  - multiplying two sums of squares gives another sum of squares
    (a^2+b^2)(c^2+d^2) = (ac+bd)^2 + (ad-bc)^2

  - All odd primes of the form 4k+1 are sums of squares

  - if we have p,q as prime and sums of squares,
    p^a x q^b is a sum of squares and can be expressed in:
    2ab + a+b ways

  - if we have p,q,r as prime and sums of squares,
    p^a x q^b x r^c is a sum of squares and can be expressed in:
    4abc + 2(ab+bc+ac) + (a+b+c) ways

  Thus, if we want 420 solutions for N, with (N,0), (0,N), (-N,0), (0,-N),
    we need 416 other solutions, and since they come in groups of 8, we need the number of unique (a,b) pairs to be 52.

  Using the formula from above, we get:
    a=1, b=17: 2(1)(17) + (17) + 1 = 52
    a=2, b=10: 2(2)(10) + (10) + 2 = 52
    a=3, b=7:  2(3)(7)  + (7)  + 3 = 52
    a=1, b=2, c =3: 4(1)(2)(3) + 2(2+3+6) + (1+2+3) = 52
    a=52

  Since p^52 > 10^11 for all primes > 5, that's not a possibility. Similar case for p^17 * q. Thus, the only three cases we need to care about are (2,10), (3,7), and (1,2,3)


"""
