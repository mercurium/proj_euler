from itertools import permutations
import string, time

START = time.time()
BASE  = 12

def base10toN(num, base):
  number = []

  while num > 0:
    number.append( num % base )
    num /= base
  return number # should be number[::-1], but i'm just using the digits anyways

def digOfBaseN(num, base):
  number = set()
  while num > 0:
    number.add( num % base )
    num /= base
  return number

sumz  = 0
count = 0
for num in permutations(string.hexdigits[:BASE]):
  if num[0] == '0':
    continue
  number = int(string.join(num, ''), BASE)

  goodResult = True
  for base in xrange(BASE-1, 4, -1):
    if digOfBaseN(number, base) != set(range(base)):
      goodResult = False
      break

  if goodResult:
    print number
    sumz  += number
    count += 1
    if count == 10:
      break

print sumz
print "Time taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 571 is correct.

You are the 94th person to have solved this problem.


30510390701978
Time taken: 376.866847992 # can probably make this faster, but mehhh

So... I brute forced this lol. Create every possible arrangement in base 12, then check if it works base 2-11. Voila, you get your answer.
"""
