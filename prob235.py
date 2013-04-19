#The positive part is...
#pos = 900 * (1-pow(r,5000))/ (1-r)
from math import log
import time
start = time.time()
from primes import *

def test(r):
  return (299 + 201*r**5000 - 300*r - 200*r**(5001) )*9./(1-r)**2

def t(r):
  print log(-1* test(r),10)
  print log(6*10**11,10)

def test2(r):
 return (-14100*r**5001 + 14103 * r**5000 - 900 *r + 897)/(1-r)**2

def t2(r):
 print math.log(abs(test2(r)),10)
 print math.log(6*10**11,10)
"""
r = 1
target = -6 * 10**11

temp = r
for dig in range(1,5):
  minz = float('inf')
  min_dig = 0
  for diz in range(0,10):
    temp = r + diz/ 10.**dig
    sumz = 0
    for i in range(1,5001):
      val = (900.-3. * i) * temp**(i-1.)
      sumz += val
    if abs(sumz - target ) < minz:
      minz = abs(sumz-target)
      min_dig = diz
  r = r + min_dig/10.**dig
  print r
print r
print "time elapsed = " + str(time.time()-start)

"""

#900- 900r^n - 900r + 900r^(n+1) - 3n*r^(n+1) + 3 (n+1)r^n - 3
#= 897 - 900r^n - 900r + 900r^(n+1) - 1500r^(n+1) + 1503r^n
#= 897 + 603r^n - 900r + 600r^(n+1)
#= 299 + 201r^n - 300r - 200r^(n+1) = -2 * 10^11 * (1-r)^2

#guestimate answer: 1.002322108633

#LOL so i just figured out the formula and kept trying out numbers
#1.002322108632876 is the 15 digit approximation
