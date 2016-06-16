import time, string
START = time.time()
from math import factorial as fa

SIZE = 150

def f(n):
    return sum([fa(int(i)) for i in str(n)])

def sf(n):
    return sum([int(i) for i in str(f(n))])

def backsolveFnDigSum(n):
  numSum = 0
  for i in xrange(9,0,-1):
    numOccur  = n/fa(i)
    numSum   += i * numOccur
    n         = n % fa(i)
  return numSum

def insert(dictStore, value):
  if len(value) == 0:
    return
  value = int(string.join([str(x) for x in value], ""))
  key   = sf(value)
  putInDict(dictStore, key, value)

def putInDict(dictStore, key, value):
  if key in dictStore:
    dictStore[key] = min(value, dictStore[key])
  else:
    # gets awfuly boring when you don't have some progress messages
    print "New key acquired!", key, f(value), value
    dictStore[key] = value

answers = dict()
def computeNums(digit, digLeft, digUsed):
  insert(answers, digUsed)
  if digLeft == 0 or digit == 10:
    return
  computeNums(digit+1, digLeft, digUsed)
  if digit == 9 or digit != digUsed.count(digit):
    computeNums(digit, digLeft-1, digUsed + [digit])

maxNumDig = 42
computeNums(1,maxNumDig, [])
sumz = 0

# Part 1
for key in sorted(answers.keys()):
  sumz += sum([int(x) for x in str(answers[key])])

# Part 2: see explanation below
for i in xrange(max(answers.keys())+1, SIZE+1):
  sfVal = int(str(i%9) + '9' * (i/9))
  sumz += backsolveFnDigSum(sfVal)

print "Answer:", sumz
print "Time Taken:", time.time() - START



"""

Congratulations, the answer you gave to problem 254 is correct.
You are the 666th person to have solved this problem.

Answer: 8184523820510
Time Taken: 112.573365927

Okay, cool. For this problem, we can semi-brute force the problem until ~ g(45) = 12378889 (or maybe g(50) with 14 digits, but really...), but this isn't good enough for g(150), which has ~192901234580 digits (+/- 50ish).
  However, we know that with digits a,b,c,d, with a <= b <= c <= d,
    -we know that f(abcd) = f(dcba) = f(abdc) = ...etc, because we're just summing up the factorial of the digits. However, abcd is the minimal amount for these.
    - With that information, if we know f(n) and want to find the minimal n, f(n) is simply a sum of factorials of digits, and thus we can find it by modding out the factorials.
      Ex: 12345 = 2fa(7) + 3fa(6) + 4fa(4) + fa(3) + fa(2) + fa(1), and thus the minimal f(n) = 12345 is 123444466677.

    (Part 2)
    - Since we can easily compute sf(n) from f(n), and can find a f(n) for a sf(n),
      - Ex: sf(n) = 13, f(n) = 49 satisfies this, so n could be 144
    if we can find the smallest f(n) for each sf(n), then we're done.

    Thankfully, since sf(n) is a sum of digits, if sf(n) = 100, then we know we need at least 11 digits of 9 and one 1 to make it.
    Since f(n) = 199999999999 is a huge n, requiring at least 551146 9's, we know that the minimal n is probably going to have
    f(n) = 199999999999 since any other f(n) for which sf(n) = 100 is going to require many more digits.

    Thus, f(n) = (n%9) + '9' * (n/9) for n > 63, and we can backsolve to get n from f(n), which gives us our answer. Woot!

"""
