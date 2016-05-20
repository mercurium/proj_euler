import time, math
START = time.time()
LIM   = 10**18

# I added a bit of custom logic for digit = 0 to account for the issue of leading zeroes.
def checkZero(val):
  digit  = 0
  strNum = str(val)
  numDig = len(strNum)
  count  = 0

  for nthDigit in xrange(0, numDig):
    currentDigit = int(strNum[nthDigit])
    tenPower     = numDig - nthDigit - 1
    prevCount    = strNum[:nthDigit].count(str(digit))  * 10 ** tenPower * currentDigit
    newDigits    = tenPower * 10 ** (tenPower-1) * currentDigit

    # we dont want to count leading zeroes like 0001 or 0011 (custom logic for digit = 0)
    if nthDigit == 0:
      newDigits -= 1111111111111111111111111110 % (10**tenPower)

    count        += int(prevCount + newDigits)
    if currentDigit > digit and (digit != 0 or nthDigit != 0 or numDig == 1):
      count += 10**tenPower
    if currentDigit == digit:
      count += 1
  return count

# This method doesn't work for digit = 0 because of leading zeroes. Use checkZero for that one.
# No reason why this one couldn't work for digit = 0, besides me wanting to clean up the code
def check(val, digit):
  strNum = str(val)
  numDig = len(strNum)
  count  = 0

  for nthDigit in xrange(0, numDig):
    currentDigit  = int(strNum[nthDigit])
    tenPower      = numDig - nthDigit - 1

    prevCount     = strNum[:nthDigit].count(str(digit))  * 10 ** tenPower * currentDigit
    newDigits     = tenPower * 10 ** (tenPower-1) * currentDigit
    count        += int(prevCount + newDigits)

    if currentDigit > digit:
      count += 10**tenPower
    elif currentDigit == digit:
      count += 1
  return count


answer = 0
for digit in xrange(1,10):
  x = 1
  while x < LIM:
    fx = check(x,digit)

    # if f(x) = x, then increment 1 since f(x+1) might also be a valid answer
    if fx == x:
      answer += x
      x      += 1
    # if f(x) - x = n, k > 0, then we need at least (x-fx) / numDig(x)
    elif fx < x:
      x += max(1, (x - fx) / (len(str(x))))
    # if f(x) > x, we need at least f(x) - x steps to get to another possible answer
    else:
      x += fx - x

print answer
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 156 is correct.

You are the 1518th person to have solved this problem.

Answer: 21295121502550
Time Taken: 0.292393922806 (pypy)

Okay, so here's the notes, in the hopes that when I visit this problem in a year, i'll still understand it :P

Two main parts to this problem: figuring out the value of f(x), as well as iterating through all possibilities of f(x) that could work.

For figuring out f(x), we can break it down into figuring out the value of each of the digits, and the range that they go through:
  Ex: for 1235, we figure out 0-999, 1000-1199, 1200 - 1229, and 1230 - 1235.
  For 0-999....9999 with d digits, each digit occurs 10^(d-1) times per slot, and there are d slots, so we have 10^(d-1) * d
  For 0-2999....999, it's the same thing, but we want to multiply by the leading digit D, since we iterate through it D times.
  So, it comes out to `10^(d-1) * d * D` for the iteration.

   Of course, if we have something like 1235, and we're counting 1's, then the 1200 - 1235 part has to include the leading 1. We can figure this out by doing str(1235)[:2].count('1') (take first two digits of 1235, then count number of 1s), and then multiplying by 35
   So we get:
    str(1235)[:2].count('1') * 35 for this part.
  Two more things to mention, if we're on the 10000 to 59999 part, and counting (1-5)'s, then we need to include 10000 more of those in the count for the leading digit that we didn't do before.

Second part: iterating and figuring out which numbers we want to check.
  As you can probably see if you run the code, there are many consecutive answers.
  If f(x) = x, then there's a non-zero chance that f(x+1) = x+1. Thus, if f(x) = x, we should check f(x+1)

  But, if f(x) > x, f(x) = x + k, then we know that f(j) > j for x <= j < k, since:
    `f(j) >= f(x) = x + k > x + j`
  This means that we can skip checking all of f(x+1), f(x+2), f(x+3),...f(x+k-1) since we won't have f(x) = x anyways.

  For f(x) < x, we know that f(x) can increase by at most the number of digits of x.
    f(1000,1) = 301, and with 4 digits, f(x) can increase by at most 4 each step, so we know the next (1000-301) / 4 steps are no good.
  Obviously we can do better, as no sequence grows by that much, but the current runtime is .2258 seconds on pypy, which is pretty darn good already. Improvements (which I will regret not making now) will come later when I need the efficiency



  Axioms:
    f(i) >= f(j) iff i >= j (it's a strictly nondecreasing sequence)


"""
