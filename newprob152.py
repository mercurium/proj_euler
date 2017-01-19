import time
START = time.time()
from primes import primes

MAX_SIZE =80

print "Time Taken:", time.time() - START



"""
Let's start off by figuring out which numbers we can exclude completely... All primes > 40. Probably all primes > 20. Main thing is that we need to get rid of all additional factors besides powers of two.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  1/17^2 + 1/(17*4)^2 =

  Primes to exclude:
  17,19,23,29,31,
  37,41,43,47,53,
  59,61,67,71,73,79

  Numbers to exclude:
  17,19,23,29,31
  34,37,38,41,43
  46,47,51,53,57
  58,59,61,62,67
  68,69,71,73,74
  76,79,
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  Primes we can include:
  2,3,5,7,11,13

  16*25 + 16 + 25 = 441 = 21^2
  16*9 + 16 + 9   = 169 = 13^2
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  Other numbers we can probably exclude:
  If a number has a power of a prime, it's probably going to be hard to get rid of.

  25,50,75,49,
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

1,4,9,16,25,36,49,64,81,100,121,144

3,7,13,21,31,43,57,73,91,111,133


  (ab)^2 + a^2 + b^2 = ?
  = a^2(b^2 + 1) + b^2
  = (a^2+1)(b^2+1) - 1

  a^2(a+1)^2 + a^2 + (a+1)^2
  = (a^2 + a + 1)^2


"""
